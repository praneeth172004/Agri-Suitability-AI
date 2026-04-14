"""
Market Price Service
Fetches crop prices and calculates ROI
"""
from prediction_app.models import CropPrice
from datetime import date, timedelta
from decimal import Decimal

class MarketService:
    """Service to handle crop market prices and ROI calculations"""
    
    # Mock market data (In production, fetch from AGMARKNET or other APIs)
    MOCK_PRICES = {
        'Rice': {'price': 2500, 'market': 'Delhi Mandi'},
        'Wheat': {'price': 2200, 'market': 'Punjab Mandi'},
        'Corn (Maize)': {'price': 1800, 'market': 'Maharashtra Mandi'},
        'Cotton': {'price': 6500, 'market': 'Gujarat Mandi'},
        'Sugarcane': {'price': 3200, 'market': 'UP Mandi'},
        'Soybean': {'price': 4500, 'market': 'MP Mandi'},
        'Groundnut': {'price': 5500, 'market': 'Andhra Mandi'},
        'Millets': {'price': 2800, 'market': 'Karnataka Mandi'},
        'Barley': {'price': 1600, 'market': 'Rajasthan Mandi'},
        'Pulses': {'price': 6000, 'market': 'Maharashtra Mandi'},
    }
    
    def get_crop_price(self, crop_name, region='India'):
        """Get current price for a crop"""
        # Try to get from database first
        try:
            price_record = CropPrice.objects.filter(
                crop_name=crop_name,
                region=region
            ).first()
            
            if price_record and (date.today() - price_record.date).days < 7:
                return {
                    'crop': crop_name,
                    'price': float(price_record.price_per_quintal),
                    'market': price_record.market_name,
                    'date': price_record.date
                }
        except:
            pass
        
        # Fallback to mock data
        if crop_name in self.MOCK_PRICES:
            data = self.MOCK_PRICES[crop_name]
            
            # Save to database
            try:
                CropPrice.objects.get_or_create(
                    crop_name=crop_name,
                    market_name=data['market'],
                    region=region,
                    defaults={'price_per_quintal': Decimal(data['price'])}
                )
            except:
                pass
            
            return {
                'crop': crop_name,
                'price': data['price'],
                'market': data['market'],
                'date': date.today()
            }
        
        return None
    
    def calculate_roi(self, crop_name, area_hectares, estimated_yield_per_hectare=25):
        """
        Calculate ROI for a crop
        area_hectares: Land area in hectares
        estimated_yield_per_hectare: Quintals per hectare (default: 25)
        """
        price_data = self.get_crop_price(crop_name)
        
        if not price_data:
            return None
        
        # Calculations
        total_yield_quintals = area_hectares * estimated_yield_per_hectare
        revenue = total_yield_quintals * price_data['price']
        
        # Estimated costs (simplified)
        seed_cost = area_hectares * 5000  # ₹5000 per hectare
        fertilizer_cost = area_hectares * 8000  # ₹8000 per hectare
        labor_cost = area_hectares * 12000  # ₹12000 per hectare
        other_costs = area_hectares * 5000  # ₹5000 per hectare
        
        total_cost = seed_cost + fertilizer_cost + labor_cost + other_costs
        profit = revenue - total_cost
        roi_percentage = (profit / total_cost) * 100 if total_cost > 0 else 0
        
        return {
            'crop': crop_name,
            'area_hectares': area_hectares,
            'estimated_yield': total_yield_quintals,
            'price_per_quintal': price_data['price'],
            'revenue': round(revenue, 2),
            'total_cost': round(total_cost, 2),
            'profit': round(profit, 2),
            'roi_percentage': round(roi_percentage, 2),
            'market': price_data['market']
        }
    
    def get_all_prices(self, region='India'):
        """Get prices for all crops"""
        prices = []
        for crop_name in self.MOCK_PRICES.keys():
            price_data = self.get_crop_price(crop_name, region)
            if price_data:
                prices.append(price_data)
        return prices
