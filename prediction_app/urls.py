from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('soil-health/', views.soil_health, name='soil_health'),
    path('market-prices/', views.market_prices, name='market_prices'),
    path('upload_data/', views.Upload_data, name='upload_data'),
    path('train_rfc/', views.RFC, name='train_rfc'),
    path('train_knn/', views.KNN, name='train_knn'),
    path('train_svm/', views.SVM, name='train_svm'),
    path('prediction/', views.prediction, name='prediction'),
    path('download_report/', views.generate_pdf, name='download_report'),
    path('crop_search/', views.crop_search, name='crop_search'),
    path('encyclopedia/', views.crop_encyclopedia, name='crop_encyclopedia'),
    path('analysis/', views.analysis_graph, name='analysis'),
    path('chat/', views.chatbot_response, name='chatbot'),
]
