import requests
from django.core.cache import cache
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Region coordinates (latitude, longitude)
REGION_COORDINATES = {
    'Andhra Pradesh': (15.9129, 79.7400),
    'Telangana': (18.1124, 79.0193),
    'India': (20.5937, 78.9629),  # Center of India
}

class WeatherService:
    """Service to fetch weather data from OpenWeatherMap API"""
    
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, region):
        """
        Fetch current weather for a region
        Returns: dict with weather data or None if error
        """
        if not self.api_key:
            logger.warning("OpenWeatherMap API key not configured")
            return None
        
        # Check cache first (cache for 30 minutes)
        cache_key = f"weather_{region}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
        
        # Get coordinates
        coords = REGION_COORDINATES.get(region)
        if not coords:
            logger.error(f"No coordinates found for region: {region}")
            return None
        
        lat, lon = coords
        
        try:
            # Make API request
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric'  # Celsius
            }
            
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant weather info
            weather_info = {
                'temperature': round(data['main']['temp'], 1),
                'feels_like': round(data['main']['feels_like'], 1),
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'wind_speed': round(data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                'pressure': data['main']['pressure'],
                'region': region
            }
            
            # Cache for 30 minutes
            cache.set(cache_key, weather_info, 1800)
            
            return weather_info
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data: {e}")
            return None
        except (KeyError, ValueError) as e:
            logger.error(f"Error parsing weather data: {e}")
            return None
