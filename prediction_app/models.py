from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    """Extended user profile with role-based access"""
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='farmer')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    @property
    def is_admin(self):
        return self.role == 'admin'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Auto-create a UserProfile when a new User is created"""
    if created:
        UserProfile.objects.get_or_create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()

class LandParcel(models.Model):
    """Model to store user's land parcels for tracking"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='land_parcels')
    name = models.CharField(max_length=200, help_text="Name of the land parcel (e.g., 'North Field')")
    region = models.CharField(max_length=100)
    area_hectares = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.region}"


class SavedPrediction(models.Model):
    """Model to store user's prediction history"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_predictions')
    land_parcel = models.ForeignKey(LandParcel, on_delete=models.SET_NULL, null=True, blank=True, related_name='predictions')
    
    # Prediction details
    prediction_date = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=100)
    temperature = models.FloatField()
    rainfall = models.FloatField()
    soil_type = models.CharField(max_length=100)
    
    # Results
    predicted_suitability = models.CharField(max_length=50)
    model_used = models.CharField(max_length=50)
    accuracy = models.FloatField(null=True, blank=True)
    
    # Optional: Store suggested crops
    suggested_crops = models.TextField(blank=True, help_text="Comma-separated list of suggested crops")
    
    class Meta:
        ordering = ['-prediction_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.region} - {self.predicted_suitability} ({self.prediction_date.strftime('%Y-%m-%d')})"


class SoilHealthRecord(models.Model):
    """Model to track soil health over time"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='soil_records')
    land_parcel = models.ForeignKey(LandParcel, on_delete=models.SET_NULL, null=True, blank=True, related_name='soil_tests')
    
    # Test details
    recorded_date = models.DateTimeField(auto_now_add=True)
    test_date = models.DateField(help_text="Date when soil sample was taken")
    
    # Soil parameters
    ph_level = models.DecimalField(max_digits=3, decimal_places=1, help_text="pH level (0-14)")
    nitrogen_level = models.DecimalField(max_digits=6, decimal_places=2, help_text="Nitrogen in ppm")
    phosphorus_level = models.DecimalField(max_digits=6, decimal_places=2, help_text="Phosphorus in ppm")
    potassium_level = models.DecimalField(max_digits=6, decimal_places=2, help_text="Potassium in ppm")
    organic_matter = models.DecimalField(max_digits=5, decimal_places=2, help_text="Organic matter %")
    soil_moisture = models.DecimalField(max_digits=5, decimal_places=2, help_text="Soil moisture %")
    
    # Additional info
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-test_date']
    
    def __str__(self):
        return f"{self.user.username} - Soil Test ({self.test_date})"
    
    def get_soil_quality_score(self):
        """Calculate overall soil quality score (0-100)"""
        # Ideal ranges
        ph_score = 100 if 6.0 <= float(self.ph_level) <= 7.5 else 50
        n_score = min(100, (float(self.nitrogen_level) / 50) * 100)
        p_score = min(100, (float(self.phosphorus_level) / 30) * 100)
        k_score = min(100, (float(self.potassium_level) / 40) * 100)
        om_score = min(100, (float(self.organic_matter) / 5) * 100)
        
        return round((ph_score + n_score + p_score + k_score + om_score) / 5, 1)


class CropPrice(models.Model):
    """Model to store crop market prices"""
    crop_name = models.CharField(max_length=100)
    market_name = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    price_per_quintal = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in INR per quintal")
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        unique_together = ['crop_name', 'market_name', 'date']
    
    def __str__(self):
        return f"{self.crop_name} - ₹{self.price_per_quintal}/quintal ({self.date})"
