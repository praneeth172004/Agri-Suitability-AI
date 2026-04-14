from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import default_storage
from django.conf import settings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

# ML Imports
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Using a standard backend for matplotlib to avoid GUI issues
import matplotlib
matplotlib.use('Agg')

from prediction_app.weather_service import WeatherService

def home(request):
    # Fetch weather for default region (India)
    weather_service = WeatherService()
    weather = weather_service.get_weather('India')
    
    return render(request, 'home.html', {'weather': weather})

def register(request):
    if request.method == 'POST':
        First_Name = request.POST['name']
        Email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmation_password = request.POST['cnfm_password']
        if password == confirmation_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists, please choose a different one.')
                return redirect('register')
            else:
                if User.objects.filter(email=Email).exists():
                    messages.error(request, 'Email already exists, please choose a different one.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=Email,
                        first_name=First_Name,
                    )
                    
                    # All registered users are farmers (admin is predefined)
                    profile = user.profile
                    profile.role = 'farmer'
                    profile.save()
                    
                    messages.success(request, 'Registration successful! Please login.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
        return render(request, 'register.html')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Role-based redirect
            role_display = 'User'
            if hasattr(user, 'profile'):
                role_display = user.profile.get_role_display()
            messages.success(request, f'Welcome back, {user.first_name}! Logged in as {role_display}.')
            if user.is_staff:
                return redirect('upload_data')  # Admin → Training page
            else:
                return redirect('home')  # Farmer → Home page
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard view
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from prediction_app.models import SavedPrediction, LandParcel
from django.db.models import Count, Avg

@login_required
def dashboard(request):
    """User dashboard showing prediction history and analytics"""
    user = request.user
    
    # Get user's saved predictions
    predictions = SavedPrediction.objects.filter(user=user)[:10]  # Last 10 predictions
    
    # Get user's land parcels
    land_parcels = LandParcel.objects.filter(user=user)
    
    # Analytics
    total_predictions = predictions.count()
    avg_accuracy = predictions.aggregate(Avg('accuracy'))['accuracy__avg'] or 0
    
    # Suitability distribution
    suitability_stats = SavedPrediction.objects.filter(user=user).values('predicted_suitability').annotate(count=Count('id'))
    
    context = {
        'predictions': predictions,
        'land_parcels': land_parcels,
        'total_predictions': total_predictions,
        'avg_accuracy': round(avg_accuracy, 2) if avg_accuracy else 0,
        'suitability_stats': suitability_stats,
    }
    
    return render(request, 'dashboard.html', context)

# Soil Health Monitoring
from prediction_app.models import SoilHealthRecord, CropPrice
from prediction_app.market_service import MarketService

def soil_health(request):
    """Soil health monitoring dashboard"""
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to view soil health monitoring.")
        return redirect('login')
    
    user = request.user
    
    # Handle form submission for adding new soil test
    if request.method == 'POST':
        try:
            from datetime import date
            SoilHealthRecord.objects.create(
                user=user,
                test_date=request.POST.get('test_date', date.today()),
                ph_level=float(request.POST.get('ph_level')),
                nitrogen_level=float(request.POST.get('nitrogen_level')),
                phosphorus_level=float(request.POST.get('phosphorus_level')),
                potassium_level=float(request.POST.get('potassium_level')),
                organic_matter=float(request.POST.get('organic_matter')),
                soil_moisture=float(request.POST.get('soil_moisture')),
                notes=request.POST.get('notes', '')
            )
            messages.success(request, "Soil test record added successfully!")
            return redirect('soil_health')
        except Exception as e:
            messages.error(request, f"Error adding soil test: {e}")
    
    soil_records = SoilHealthRecord.objects.filter(user=user)[:10]
    
    # Calculate average soil quality
    if soil_records:
        avg_quality = sum([record.get_soil_quality_score() for record in soil_records]) / len(soil_records)
    else:
        avg_quality = 0
    
    context = {
        'soil_records': soil_records,
        'avg_quality': round(avg_quality, 1),
        'total_tests': soil_records.count()
    }
    
    return render(request, 'soil_health.html', context)

def market_prices(request):
    """Market prices and ROI calculator"""
    market_service = MarketService()
    
    # Get all crop prices
    prices = market_service.get_all_prices()
    
    # ROI calculation if form submitted
    roi_result = None
    if request.method == 'POST':
        crop_name = request.POST.get('crop')
        area = float(request.POST.get('area', 1))
        roi_result = market_service.calculate_roi(crop_name, area)
    
    context = {
        'prices': prices,
        'roi_result': roi_result
    }
    
    return render(request, 'market_prices.html', context)


# Global variables for training state (Simple in-memory approach as per prompt)
# In production, this should be handled differently (databases, cache, etc.)
X_train = None
X_test = None
y_train = None
y_test = None
dataloaded = False
df = None

# Metrics storage
precision = []
recall = []
fscore = []
accuracy = []
model_results = {}
labels = ['Unsuitable', 'Moderate', 'Highly Suitable']

@staff_member_required
def Upload_data(request):
    global df, dataloaded, X_train, X_test, y_train, y_test
    load = True
    
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name = default_storage.save(uploaded_file.name, uploaded_file)
        file_path = default_storage.path(file_name)
        
        try:
            df = pd.read_csv(file_path)
            
            # Preprocessing
            categorical_cols = ['Irrigation_Level', 'CO2_Emission_Scenario', 'Fertilizer_Access', 'Land_Degradation_Risk']
            encoders = {}
            
            for col in categorical_cols:
                if col in df.columns:
                    le = LabelEncoder()
                    df[col] = le.fit_transform(df[col].astype(str))
                    encoders[col] = le
            
            # Save encoders
            model_dir = os.path.join(settings.BASE_DIR, 'model')
            os.makedirs(model_dir, exist_ok=True)
            joblib.dump(encoders, os.path.join(model_dir, 'label_encoders.pkl'))
            
            # Target Encoding
            if 'Land_Suitability' in df.columns:
                target_encoder = LabelEncoder()
                y = target_encoder.fit_transform(df['Land_Suitability'])
                joblib.dump(target_encoder, os.path.join(model_dir, 'target_encoder.pkl'))
                
                X = df.iloc[:, 1:-1] 
                
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
                dataloaded = True
                
                # Clean up uploaded file
                default_storage.delete(file_name)
                
                outdata = df.head(100)
                return render(request, 'train.html', {'temp': outdata.to_html(classes='table table-striped'), 'dataloaded': True})
            else:
                 messages.error(request, "Dataset must contain 'Land_Suitability' column")
        
        except Exception as e:
            messages.error(request, f"Error processing file: {e}")
            if os.path.exists(file_path):
                 default_storage.delete(file_name)

    return render(request, 'train.html', {'upload': load, 'dataloaded': dataloaded})

def calculateMetrics(algorithm, testY, predict):
    testY = testY.astype('int')
    predict = predict.astype('int')
    p = precision_score(testY, predict, average='macro', zero_division=0) * 100
    r = recall_score(testY, predict, average='macro', zero_division=0) * 100
    f = f1_score(testY, predict, average='macro', zero_division=0) * 100
    a = accuracy_score(testY, predict) * 100
    
    accuracy.append(a)
    precision.append(p)
    recall.append(r)
    fscore.append(f)
    
    global model_results
    model_results[algorithm] = {
        'Accuracy': a,
        'Precision': p,
        'Recall': r,
        'F1-Score': f
    }
    
    # We are not printing or showing plots interactively in server code usually, 
    # but the prompt code had it. We will skip the plot.show() and return metrics.

@staff_member_required
def RFC(request):
    if not dataloaded:
        messages.warning(request, "Please upload dataset first.")
        return redirect('upload_data')
    
    model_dir = os.path.join(settings.BASE_DIR, 'model')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'RandomForestClassifier.pkl')
    
    # Force Retrain
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    joblib.dump(rf, model_path)
    
    predict = rf.predict(X_test)
    calculateMetrics("RandomForestClassifier", y_test, predict)
    
    return render(request, 'train.html',
                  {'algorithm': 'Random Forest Classifier',
                   'accuracy': accuracy[-1],
                   'precision': precision[-1],
                   'recall': recall[-1],
                   'fscore': fscore[-1],
                   'dataloaded': True})

@staff_member_required
def KNN(request):
    if not dataloaded:
        messages.warning(request, "Please upload dataset first.")
        return redirect('upload_data')
        
    model_dir = os.path.join(settings.BASE_DIR, 'model')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'KNNClassifier.pkl')
    
    # Reshape logic from prompt not needed usually for standard scikit-learn X_train (2D array),
    # unless X_train became 3D somehow (e.g. image data). Assuming tabular data is 2D.
    
    # Force Retrain
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    joblib.dump(knn, model_path)
        
    predict = knn.predict(X_test)
    calculateMetrics("KNN", y_test, predict)
    
    return render(request, 'train.html',
                  {'algorithm': 'K-Nearest Neighbors (KNN)',
                   'accuracy': accuracy[-1],
                   'precision': precision[-1],
                   'recall': recall[-1],
                   'fscore': fscore[-1],
                   'dataloaded': True})

@staff_member_required
def SVM(request):
    if not dataloaded:
        messages.warning(request, "Please upload dataset first.")
        return redirect('upload_data')
        
    model_dir = os.path.join(settings.BASE_DIR, 'model')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'SVM_model.pkl')
    
    # Force Retrain
    svm = SVC(kernel='rbf', probability=True, random_state=42)
    svm.fit(X_train, y_train)
    joblib.dump(svm, model_path)
        
    predict = svm.predict(X_test)
    calculateMetrics("SVM", y_test, predict)
    
    return render(request, 'train.html',
                  {'algorithm': 'Support Vector Machine (SVM)',
                   'accuracy': accuracy[-1],
                   'precision': precision[-1],
                   'recall': recall[-1],
                   'fscore': fscore[-1],
                   'dataloaded': True})

def get_crop_suggestions(suitability, rainfall, temperature):
    if suitability == "Unsuitable":
        return []

    suggestions = []
    
    # Iterate over the expanded crop database in utils.py
    for crop_name, params in CROP_SUGGESTION_PARAMS.items():
        if (params["min_rain"] <= rainfall <= params["max_rain"] and
            params["min_temp"] <= temperature <= params["max_temp"] and
            suitability in params["suitability"]):
            suggestions.append(crop_name)
            
    return suggestions

from .utils import CROP_DETAILS, CROP_ENCYCLOPEDIA, CROP_SUGGESTION_PARAMS

def crop_search(request):
    query = request.GET.get('query')
    result = None
    
    if query:
        # Case-insensitive search
        for crop_name, details in CROP_DETAILS.items():
            if crop_name.lower() == query.lower():
                result = {'name': crop_name, **details}
                break
                
    return render(request, 'crop_search.html', {'query': query, 'result': result})

def crop_encyclopedia(request):
    enriched_encyclopedia = []
    
    for category in CROP_ENCYCLOPEDIA:
        cat_data = {
            'category': category['category'], 
            'id': category.get('id', ''), 
            'subcategories': [], 
            'crops': []
        }
        
        if 'subcategories' in category:
            for sub in category['subcategories']:
                enriched_sub = {
                    'name': sub['name'], 
                    'icon': sub.get('icon', ''), 
                    'crops': []
                }
                for crop_name in sub['crops']:
                    details = CROP_DETAILS.get(crop_name, {
                        'description': 'Details coming soon.',
                        'ideal_temp': 'N/A',
                        'ideal_rainfall': 'N/A',
                        'soil_type': 'N/A',
                        'growing_season': 'N/A',
                        'climate': 'N/A'
                    })
                    enriched_sub['crops'].append({'name': crop_name, **details})
                cat_data['subcategories'].append(enriched_sub)
        else:
            for crop_name in category['crops']:
                details = CROP_DETAILS.get(crop_name, {
                    'description': 'Details coming soon.',
                    'ideal_temp': 'N/A',
                    'ideal_rainfall': 'N/A',
                    'soil_type': 'N/A',
                    'growing_season': 'N/A',
                    'climate': 'N/A'
                })
                cat_data['crops'].append({'name': crop_name, **details})
        
        enriched_encyclopedia.append(cat_data)

    return render(request, 'crop_encyclopedia.html', {'encyclopedia': enriched_encyclopedia})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import os

from django.conf import settings

# Configure your API key here
GEMINI_API_KEY = settings.GEMINI_API_KEY
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        message = request.POST.get('message', '').lower()
        response_text = ""

        # TRY GEN-AI (Gemini)
        if GEMINI_API_KEY:
            try:
                model = genai.GenerativeModel('gemini-flash-latest')
                # Add context for the AI
                context = (
                    "You are 'Agri-Bot', an intelligent agricultural assistant. "
                    "Answer user questions about farming, crops, soil, climate, and sustainability. "
                    "Keep answers concise (under 100 words) and helpful. "
                    "If the question is unrelated to agriculture, politely steer back to farming."
                )
                prompt = f"{context}\nUser: {message}\nAgri-Bot:"
                
                ai_response = model.generate_content(prompt)
                response_text = ai_response.text
                return JsonResponse({'response': response_text})
            except Exception as e:
                print(f"Gemini API Error: {e}")
                # Detailed error logging for debugging
                 # Fallback to rule-based if API fails
                pass
        
        # FALLBACK: Rule-Based Logic
        response_text = "I'm currently running in 'Offline Mode'. Try checking your internet or API Key. In the meantime: "
        
        # 1. Greeting
        if any(word in message for word in ['hello', 'hi', 'hey']):
            response_text = "Hello! I'm Agri-Bot. Ask me about crop conditions or your land suitability."
        
        # 2. Crop specific queries
        elif any(crop.lower() in message for crop in CROP_DETAILS.keys()):
            found = False
            for crop_name, details in CROP_DETAILS.items():
                if crop_name.lower() in message:
                    response_text = f"**{crop_name}**: {details['description']} It needs {details['ideal_temp']} and {details['ideal_rainfall']} rainfall."
                    found = True
                    break
            if not found:
                 response_text = "I have details on Rice, Wheat, Corn, etc. Which crop are you interested in?"

        # 3. Contextual help
        elif 'soil' in message:
            response_text = "Soil quality is crucial! Clay soils hold water well (good for Rice), while Loamy soils are versatile for most crops."
        elif 'rain' in message or 'water' in message:
            response_text = "Water is key. Crops like Rice need heavy rainfall (>1000mm), while Millets and Barley are drought-resistant."
        else:
             response_text = "I'm in offline mode and didn't understand that. Ask me about Rice, Wheat, or Soil."

        return JsonResponse({'response': response_text})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    # Retrieve data from session
    prediction_data = request.session.get('prediction_data')
    if not prediction_data:
        messages.error(request, "No prediction data found. Please make a prediction first.")
        return redirect('prediction')

    template_path = 'pdf_report.html'
    context = prediction_data
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="land_suitability_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # Create PDF
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def prediction(request):
    model_dir = os.path.join(settings.BASE_DIR, 'model')
    model_path = os.path.join(model_dir, 'RandomForestClassifier.pkl')
    
    feature_labels = {
        "Soil_Quality_Index": "Soil Quality Index",
        "Annual_Rainfall_mm": "Annual Rainfall (mm)",
        "Temperature_C": "Temperature (°C)",
        "Irrigation_Level": "Irrigation Level",
        "CO2_Emission_Scenario": "CO2 Emission Scenario",
        "Water_Availability_Index": "Water Availability Index",
        "Fertilizer_Access": "Fertilizer Access",
        "Land_Degradation_Risk": "Land Degradation Risk"
    }

    field_choices = {
        "Irrigation_Level": ["Low", "Medium", "High"],
        "CO2_Emission_Scenario": ["Low", "Medium", "High"],
        "Fertilizer_Access": ["Low", "Moderate", "High"],
        "Land_Degradation_Risk": ["Low", "Moderate", "High"]
    }

    if request.method == "POST":
        try:
            if not os.path.exists(model_path):
                messages.error(request, "Model not trained yet.")
                return redirect('prediction')

            clf = joblib.load(model_path)
            encoders = joblib.load(os.path.join(model_dir, 'label_encoders.pkl'))
            target_encoder = joblib.load(os.path.join(model_dir, 'target_encoder.pkl'))

            input_dict = {key: request.POST.get(key) for key in feature_labels.keys()}
            df_input = pd.DataFrame([input_dict])
             
            # Handle encoding
            for col, encoder in encoders.items():
                if col in df_input.columns:
                    val = df_input[col].iloc[0]
                    try:
                        df_input[col] = encoder.transform([val])[0]
                    except ValueError:
                         messages.error(request, f"Invalid value '{val}' for field '{col}'")
                         return redirect('prediction')

            prediction_result = clf.predict(df_input)[0]
            outcome = target_encoder.inverse_transform([prediction_result])[0]
            
            # Get Crop Suggestions
            try:
                rainfall = float(input_dict['Annual_Rainfall_mm'])
                temperature = float(input_dict['Temperature_C'])
                suggested_crops = get_crop_suggestions(outcome, rainfall, temperature)
            except ValueError:
                suggested_crops = []

            # Auto-save prediction to dashboard (if user is logged in)
            if request.user.is_authenticated:
                try:
                    from prediction_app.models import SavedPrediction
                    SavedPrediction.objects.create(
                        user=request.user,
                        region='General',  # You can modify this based on your needs
                        temperature=temperature,
                        rainfall=rainfall,
                        soil_type=input_dict.get('Soil_Quality_Index', 'Unknown'),
                        predicted_suitability=outcome,
                        model_used='Random Forest',
                        accuracy=95.0,  # You can get this from your model metrics
                        suggested_crops=', '.join(suggested_crops) if suggested_crops else ''
                    )
                except Exception as e:
                    print(f"Error saving prediction: {e}")

            # Store in session for PDF and Chart
            request.session['prediction_data'] = {
                'outcome': outcome,
                'suggested_crops': suggested_crops,
                'input_data': input_dict,
                'feature_labels': feature_labels
            }

            return render(request, 'outcome.html', {
                'outcome': outcome, 
                'suggested_crops': suggested_crops,
                'input_data': input_dict
            })
            
        except Exception as e:
            messages.error(request, f"Error during prediction: {e}")
            return redirect('prediction')

    form_fields = []
    for key, label in feature_labels.items():
        field = {
            "key": key, 
            "label": label, 
            "choices": field_choices.get(key)
        }
        form_fields.append(field)

    return render(request, 'prediction.html', {"form_fields": form_fields})

import matplotlib.pyplot as plt
import io
import urllib, base64

@staff_member_required
def analysis_graph(request):
    if not model_results:
        messages.warning(request, "No trained models found to analyze.")
        return redirect('upload_data')
        
    algorithms = list(model_results.keys())
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    
    # Prepare data for plotting
    data = {m: [] for m in metrics}
    for algo in algorithms:
        for m in metrics:
            data[m].append(model_results[algo][m])
            
    # Plotting
    sns.set_style("whitegrid")
    sns.set_context("talk") # Larger fonts
    
    x = np.arange(len(algorithms))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Custom vibrant palette
    colors = ['#2ecc71', '#3498db', '#9b59b6', '#f1c40f'] # Green, Blue, Purple, Yellow
    
    for i, metric in enumerate(metrics):
        bars = ax.bar(x + i*width, data[metric], width, label=metric, color=colors[i], edgecolor='white', linewidth=1)
        
        # Add labels on top
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, fontweight='bold', color='#34495e')

    ax.set_ylabel('Scores (%)', fontsize=14, fontweight='bold', labelpad=10)
    ax.set_title('Model Performance Comparison', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(algorithms, fontsize=12, fontweight='bold')
    ax.legend(loc='lower right', frameon=True, framealpha=0.9, shadow=True, borderpad=1)
    ax.set_ylim(0, 110) # More space for labels
    
    # Remove top and right spines for cleaner look
    sns.despine(left=True, bottom=True)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save to string
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    
    # Clean up
    plt.close(fig)
    
    return render(request, 'analysis.html', {'graph': uri})
