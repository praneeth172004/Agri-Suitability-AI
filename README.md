# Agri-Suitability AI 🌿

**Agri-Suitability AI** is an intelligent, machine learning-powered platform designed to revolutionize agricultural decision-making. By analyzing soil metrics, climate data, and market trends, it provides farmers with actionable insights into land suitability, crop selection, and soil health management.

![Project Banner](https://img.shields.io/badge/Agri-Suitability%20AI-4CAF50?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 🚀 Features

### 1. Land Suitability Prediction
Leverages robust Machine Learning models (Random Forest, SVM, KNN) to classify land suitability based on:
*   **Soil Quality Index**
*   **Annual Rainfall**
*   **Temperature**
*   **Irrigation Levels**
*   **CO2 Emission Scenarios**

### 2. Intelligent Crop Suggestions
Dynamically recommends the best crops (Rice, Wheat, Corn, etc.) for a specific land parcel by matching environmental conditions with crop physiological requirements.

### 3. Agri-Bot (Gen-AI Assistant)
An integrated chatbot powered by **Google Gemini Flash** that provides instant answers to farming queries, soil management tips, and agricultural best practices.

### 4. Soil Health Monitoring
Track and visualize soil metrics over time, including pH levels, Nitrogen (N), Phosphorus (P), Potassium (K), and Organic Matter. Includes a "Soil Quality Score" algorithm.

### 5. Market Pulse & ROI Calculator
*   **Live Market Prices**: Stay updated with the latest crop prices across different regions.
*   **ROI Estimator**: Calculate potential returns on investment based on crop type and land area.

### 6. Admin Analytics Dashboard
A dedicated space for administrators to:
*   Upload and preprocess new agricultural datasets.
*   Train, evaluate, and compare multiple ML models.
*   Visualize model performance (Accuracy, Precision, Recall, F1-Score).

### 7. Digital Report Generation
Generate and download professional PDF reports of land suitability assessments for record-keeping or loan applications.

---

## 🛠️ Technology Stack

*   **Framework**: [Django](https://www.djangoproject.com/) (Backend)
*   **AI/ML**: [Scikit-Learn](https://scikit-learn.org/), [Joblib](https://joblib.readthedocs.io/), [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
*   **Generative AI**: [Google Gemini Pro Flash](https://ai.google.dev/)
*   **Visualization**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [Plotly](https://plotly.com/)
*   **PDF Engine**: [xhtml2pdf](https://github.com/xhtml2pdf/xhtml2pdf)
*   **Database**: SQLite (Default) / PostgreSQL (Production ready)

---

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.10+
*   Git

### 1. Clone the Repository
```bash
git clone https://github.com/praneeth172004/Agri-Suitability-AI.git
cd Agri-Suitability-AI
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory and add your credentials:
```env
SECRET_KEY=your_django_secret_key
DEBUG=True
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User
```bash
python manage.py createsuperuser
```

### 7. Start the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📊 Project Structure
```text
Agri-Suitability-AI/
├── crop_prediction/      # Django Settings & WSGI
├── prediction_app/       # Core Business Logic (Views, Models, Utils)
│   ├── market_service.py # API for market prices
│   ├── weather_service.py# API for weather data
│   ├── chatbot/          # Gemini integration
│   └── ...
├── model/                # Saved ML Models (.pkl files)
├── templates/            # HTML Views
├── static/               # CSS, JS, and Images
├── media/                # User-uploaded files
└── manage.py             # Entry point
```

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed for the betterment of the farming community.** 🚜🌾
