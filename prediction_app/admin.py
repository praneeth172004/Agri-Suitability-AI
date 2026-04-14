from django.contrib import admin
from prediction_app.models import UserProfile, LandParcel, SavedPrediction, SoilHealthRecord, CropPrice

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')

@admin.register(LandParcel)
class LandParcelAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'region', 'area_hectares')

@admin.register(SavedPrediction)
class SavedPredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'region', 'predicted_suitability', 'model_used', 'prediction_date')
    list_filter = ('predicted_suitability', 'model_used')

@admin.register(SoilHealthRecord)
class SoilHealthRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'test_date', 'ph_level', 'nitrogen_level')

@admin.register(CropPrice)
class CropPriceAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'market_name', 'price_per_quintal', 'date')
