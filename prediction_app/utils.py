
# Dictionary containing crop details for the "Crop Encyclopedia" feature
CROP_DETAILS = {
    # --- CEREALS ---
    "Rice": {
        "description": "Staple food for over half the world's population.",
        "ideal_temp": "20°C - 35°C",
        "ideal_rainfall": "100-300 cm",
        "soil_type": "Clayey or Clay Loam",
        "growing_season": "Kharif (Monsoon)",
        "climate": "Hot and Humid"
    },
    "Wheat": {
        "description": "Major staple globally; requires cool growing season.",
        "ideal_temp": "10°C - 25°C",
        "ideal_rainfall": "50-100 cm",
        "soil_type": "Well-drained Loam",
        "growing_season": "Rabi (Winter)",
        "climate": "Cool and Moist"
    },
    "Maize (Corn)": {
        "description": "Queen of Cereals; used for food, feed, and fuel.",
        "ideal_temp": "21°C - 27°C",
        "ideal_rainfall": "50-100 cm",
        "soil_type": "Old Alluvial / Loam",
        "growing_season": "Kharif/Rabi",
        "climate": "Warm"
    },
    "Barley": {
        "description": "Hardy cereal; used for malt and fodder.",
        "ideal_temp": "12°C - 25°C",
        "ideal_rainfall": "40-90 cm",
        "soil_type": "Sandy Loam",
        "growing_season": "Rabi",
        "climate": "Cool"
    },
    "Millets (Jowar, Bajra, Ragi)": {
        "description": "Nutri-cereals; drought resistant and hardy.",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "30-60 cm",
        "soil_type": "Poor/Sandy/Red soils",
        "growing_season": "Kharif",
        "climate": "Hot/Dry"
    },
     "Sorghum (Jowar)": {
        "description": "Drought-hardy cereal, staple in dry regions.",
        "ideal_temp": "26°C - 33°C",
        "ideal_rainfall": "30-100 cm",
        "soil_type": "Loamy/Sandy",
        "growing_season": "Kharif/Rabi",
        "climate": "Warm/Arid"
    },
    "Pearl millet (Bajra)": {
        "description": "Highly drought-tolerant; good for sandy soils.",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "25-60 cm",
        "soil_type": "Sandy/Light",
        "growing_season": "Kharif",
        "climate": "Hot/Dry"
    },
    "Finger millet (Ragi)": {
        "description": "Rich in calcium; staple in southern India.",
        "ideal_temp": "20°C - 30°C",
        "ideal_rainfall": "50-100 cm",
        "soil_type": "Red/Loam / Sandy",
        "growing_season": "Kharif",
        "climate": "Tropical/Sub-tropical"
    },

    # --- PULSES ---
    "Chickpea (Gram)": {
        "description": "King of pulses; rich in protein.",
        "ideal_temp": "20°C - 25°C",
        "ideal_rainfall": "40-45 cm",
        "soil_type": "Sandy Loam / Clay Loam",
        "growing_season": "Rabi",
        "climate": "Cool/Dry"
    },
    "Pigeon pea (Arhar/Tur)": {
        "description": "Major protein source; drought tolerant.",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "60-100 cm",
        "soil_type": "Sandy Loam / Loam",
        "growing_season": "Kharif",
        "climate": "Warm/Tropical"
    },
    "Lentil (Masur)": {
         "description": "Nutritious pulse, fixes nitrogen.",
         "ideal_temp": "18°C - 30°C",
         "ideal_rainfall": "30-50 cm",
         "soil_type": "Loam / Clay",
         "growing_season": "Rabi",
         "climate": "Cool"
    },
    "Green gram (Moong)": {
        "description": "Short duration pulse, digestible protein.",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "60-90 cm",
        "soil_type": "Loam / Sandy Loam",
        "growing_season": "Kharif/Summer",
        "climate": "Warm"
    },

    # --- OILSEEDS ---
    "Groundnut (Peanut)": {
        "description": "Major oilseed; nitrogen fixer.",
        "ideal_temp": "20°C - 30°C",
        "ideal_rainfall": "50-100 cm",
        "soil_type": "Sandy Loam (Well drained)",
        "growing_season": "Kharif",
        "climate": "Tropical/Sub-tropical"
    },
    "Mustard": {
        "description": "Key oilseed crop of Rabi season.",
        "ideal_temp": "10°C - 25°C",
        "ideal_rainfall": "60-100 cm",
        "soil_type": "Loam / Clay Loam",
        "growing_season": "Rabi",
        "climate": "Cool"
    },
    "Soybean": {
        "description": "High protein and oil content.",
        "ideal_temp": "20°C - 30°C",
        "ideal_rainfall": "60-100 cm",
        "soil_type": "Fertile Loam",
        "growing_season": "Kharif",
        "climate": "Warm/Humid"
    },
    "Sunflower": {
        "description": "Photo-insensitive; adaptable oilseed.",
        "ideal_temp": "20°C - 25°C",
        "ideal_rainfall": "50-100 cm",
        "soil_type": "Loam",
        "growing_season": "All Seasons",
        "climate": "Cool/Warm"
    },

    # --- CASH & FIBRE ---
    "Sugarcane": {
        "description": "Main source of sugar; long duration crop.",
        "ideal_temp": "21°C - 27°C",
        "ideal_rainfall": "75-150 cm",
        "soil_type": "Deep Rich Loamy Soil",
        "growing_season": "Year-round (Tropical)",
        "climate": "Hot/Humid"
    },
    "Cotton": {
        "description": "White Gold; premier fibre crop.",
        "ideal_temp": "21°C - 30°C",
        "ideal_rainfall": "50-100 cm",
        "soil_type": "Black Cotton Soil (Regur)",
        "growing_season": "Kharif",
        "climate": "Tropical/Sub-tropical"
    },
    "Jute": {
        "description": "Golden Fibre; eco-friendly packaging material.",
        "ideal_temp": "24°C - 35°C",
        "ideal_rainfall": "150-250 cm",
        "soil_type": "Riverine Alluvial",
        "growing_season": "Kharif",
        "climate": "Hot/Humid"
    },

    # --- PLANTATION ---
    "Tea": {
        "description": "Queen of beverages; processed leaves.",
        "ideal_temp": "20°C - 30°C",
        "ideal_rainfall": "150-300 cm (well distributed)",
        "soil_type": "Laterite/Acidic Loam",
        "growing_season": "Perennial",
        "climate": "Warm/Humid"
    },
    "Coffee": {
        "description": "Popular beverage; shade loving.",
        "ideal_temp": "15°C - 28°C",
        "ideal_rainfall": "150-250 cm",
        "soil_type": "Well-drained Loam",
        "growing_season": "Perennial",
        "climate": "Tropical Highlands"
    },
    "Rubber": {
        "description": "Source of natural latex.",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": ">200 cm",
        "soil_type": "Laterite/Deep Loam",
        "growing_season": "Perennial",
        "climate": "Equatorial/Tropical"
    },

    # --- HORTICULTURE ---
    "Mango": {
        "description": "King of Fruits.",
        "ideal_temp": "24°C - 30°C",
        "ideal_rainfall": "89-100 cm",
        "soil_type": "Alluvial / Laterite",
        "growing_season": "Summer",
        "climate": "Tropical"
    },
    "Banana": {
        "description": "Energy rich fruit; year round availability.",
        "ideal_temp": "15°C - 35°C",
        "ideal_rainfall": "High moisture needed",
        "soil_type": "Rich Loamy",
        "growing_season": "Year-round",
        "climate": "Tropical"
    },
    "Tomato": {
        "description": "Widely used vegetable; requires support.",
        "ideal_temp": "18°C - 25°C",
        "ideal_rainfall": "Moderate",
        "soil_type": "Loam / Sandy Loam",
        "growing_season": "Rabi/Kharif",
        "climate": "Warm"
    },
    "Potato": {
        "description": "Major tuber crop; staple vegetable.",
        "ideal_temp": "15°C - 20°C",
        "ideal_rainfall": "Moderate",
        "soil_type": "Sandy Loam",
        "growing_season": "Rabi",
        "climate": "Cool"
    },
    "Onion": {
        "description": "Essential culinary ingredient.",
        "ideal_temp": "13°C - 24°C",
        "ideal_rainfall": "Moderate",
        "soil_type": "Sandy Loam",
        "growing_season": "Rabi/Kharif",
        "climate": "Temperate"
    }
    # Add defaults for others if needed in view logic
}

CROP_ENCYCLOPEDIA = [
    {
        "category": "Food Crops",
        "subcategories": [
            {
                "name": "Cereals (Staple crops)",
                "icon": "🌾",
                "crops": ["Rice", "Wheat", "Maize (Corn)", "Barley", "Sorghum (Jowar)", "Pearl millet (Bajra)", "Finger millet (Ragi)"]
            },
            {
                "name": "Pulses (Legumes)",
                "icon": "🌱",
                "crops": ["Chickpea (Gram)", "Pigeon pea (Arhar/Tur)", "Green gram (Moong)", "Lentil (Masur)"]
            }
        ]
    },
    {
        "category": "Oilseed Crops",
        "id": "oilseeds",
        "crops": ["Groundnut (Peanut)", "Mustard", "Soybean", "Sunflower"]
    },
    {
        "category": "Cash & Fibre Crops",
        "id": "cash",
        "crops": ["Sugarcane", "Cotton", "Jute"]
    },
    {
        "category": "Plantation Crops",
        "id": "plantation",
        "crops": ["Tea", "Coffee", "Rubber"]
    },
    {
        "category": "Horticultural Crops",
        "subcategories": [
            {
                "name": "Fruits",
                "icon": "🍎",
                "crops": ["Mango", "Banana"]
            },
            {
                "name": "Vegetables",
                "icon": "🥦",
                "crops": ["Potato", "Tomato", "Onion"]
            }
        ]
    }
]
