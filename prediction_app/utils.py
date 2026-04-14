
# --- CROP SUGGESTION PARAMETERS ---
# Used by the ML prediction logic to match environmental conditions
# Total: 100+ Crops
CROP_SUGGESTION_PARAMS = {
    # --- CEREALS & GRAINS ---
    "Rice": {"min_rain": 1000, "max_rain": 2500, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Wheat": {"min_rain": 500, "max_rain": 900, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Maize (Corn)": {"min_rain": 500, "max_rain": 800, "min_temp": 18, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Barley": {"min_rain": 300, "max_rain": 600, "min_temp": 12, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Sorghum": {"min_rain": 400, "max_rain": 750, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Pearl Millet (Bajra)": {"min_rain": 400, "max_rain": 600, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Finger Millet (Ragi)": {"min_rain": 500, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Oats": {"min_rain": 500, "max_rain": 1000, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Rye": {"min_rain": 400, "max_rain": 900, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Buckwheat": {"min_rain": 400, "max_rain": 700, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},

    # --- PULSES & LEGUMES ---
    "Chickpea": {"min_rain": 300, "max_rain": 500, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Pigeon Pea": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Lentil": {"min_rain": 300, "max_rain": 500, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Black Gram": {"min_rain": 600, "max_rain": 1000, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Green Gram": {"min_rain": 600, "max_rain": 1000, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Horse Gram": {"min_rain": 300, "max_rain": 900, "min_temp": 25, "max_temp": 30, "suitability": ["Moderate", "Unsuitable"]}, # Very hardy
    "Cowpea": {"min_rain": 400, "max_rain": 1000, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Kidney Bean": {"min_rain": 500, "max_rain": 1000, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "French Bean": {"min_rain": 900, "max_rain": 1200, "min_temp": 18, "max_temp": 28, "suitability": ["Highly Suitable"]},
    "Peas": {"min_rain": 400, "max_rain": 800, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},

    # --- OILSEED CROPS ---
    "Soybean": {"min_rain": 500, "max_rain": 900, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Groundnut": {"min_rain": 500, "max_rain": 750, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Sunflower": {"min_rain": 400, "max_rain": 700, "min_temp": 20, "max_temp": 28, "suitability": ["Highly Suitable", "Moderate"]},
    "Rapeseed/Mustard": {"min_rain": 500, "max_rain": 800, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Sesame": {"min_rain": 500, "max_rain": 800, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Linseed": {"min_rain": 450, "max_rain": 750, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Castor": {"min_rain": 500, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Safflower": {"min_rain": 300, "max_rain": 600, "min_temp": 15, "max_temp": 30, "suitability": ["Moderate", "Unsuitable"]},

    # --- CASH & PLANTATION CROPS ---
    "Sugarcane": {"min_rain": 1000, "max_rain": 2000, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Cotton": {"min_rain": 500, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Jute": {"min_rain": 1500, "max_rain": 2000, "min_temp": 24, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Tea": {"min_rain": 1500, "max_rain": 2500, "min_temp": 15, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Coffee": {"min_rain": 1200, "max_rain": 2000, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Rubber": {"min_rain": 2000, "max_rain": 3000, "min_temp": 25, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Coconut": {"min_rain": 1500, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Oil Palm": {"min_rain": 2000, "max_rain": 3000, "min_temp": 24, "max_temp": 28, "suitability": ["Highly Suitable"]},
    "Cashew": {"min_rain": 1000, "max_rain": 2000, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Arecanut": {"min_rain": 2000, "max_rain": 4000, "min_temp": 14, "max_temp": 36, "suitability": ["Highly Suitable"]},
    "Tobacco": {"min_rain": 500, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Cocoa": {"min_rain": 1500, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},

    # --- FRUITS ---
    "Mango": {"min_rain": 750, "max_rain": 1500, "min_temp": 24, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Banana": {"min_rain": 1200, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Citrus": {"min_rain": 1000, "max_rain": 2000, "min_temp": 15, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Grapes": {"min_rain": 500, "max_rain": 1000, "min_temp": 15, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Apple": {"min_rain": 750, "max_rain": 1200, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable"]},
    "Papaya": {"min_rain": 1200, "max_rain": 2000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Guava": {"min_rain": 1000, "max_rain": 2000, "min_temp": 23, "max_temp": 28, "suitability": ["Highly Suitable", "Moderate"]},
    "Pomegranate": {"min_rain": 500, "max_rain": 800, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Pineapple": {"min_rain": 1000, "max_rain": 1500, "min_temp": 22, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Strawberry": {"min_rain": 600, "max_rain": 1200, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Watermelon": {"min_rain": 400, "max_rain": 600, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Muskmelon": {"min_rain": 400, "max_rain": 600, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Jackfruit": {"min_rain": 1500, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Litchi": {"min_rain": 1200, "max_rain": 1500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Sapota (Chiku)": {"min_rain": 1200, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Custard Apple": {"min_rain": 500, "max_rain": 800, "min_temp": 20, "max_temp": 30, "suitability": ["Moderate", "Unsuitable"]},
    "Pear": {"min_rain": 750, "max_rain": 1000, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Peach": {"min_rain": 750, "max_rain": 1000, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Plum": {"min_rain": 750, "max_rain": 1000, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Apricot": {"min_rain": 750, "max_rain": 1000, "min_temp": 7, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Cherry": {"min_rain": 750, "max_rain": 1200, "min_temp": 7, "max_temp": 20, "suitability": ["Highly Suitable"]},
    "Kiwi": {"min_rain": 1000, "max_rain": 1500, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Dragon Fruit": {"min_rain": 500, "max_rain": 1500, "min_temp": 20, "max_temp": 35, "suitability": ["Moderate", "Unsuitable"]},

    # --- VEGETABLES ---
    "Potato": {"min_rain": 500, "max_rain": 800, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Tomato": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Onion": {"min_rain": 500, "max_rain": 700, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Chili": {"min_rain": 600, "max_rain": 1200, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Brinjal": {"min_rain": 750, "max_rain": 1200, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Okra": {"min_rain": 750, "max_rain": 1000, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Cabbage": {"min_rain": 500, "max_rain": 700, "min_temp": 15, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Cauliflower": {"min_rain": 500, "max_rain": 700, "min_temp": 15, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Carrot": {"min_rain": 500, "max_rain": 800, "min_temp": 15, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Spinach": {"min_rain": 400, "max_rain": 800, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Radish": {"min_rain": 400, "max_rain": 800, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Turnip": {"min_rain": 400, "max_rain": 800, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Beetroot": {"min_rain": 400, "max_rain": 800, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Garlic": {"min_rain": 500, "max_rain": 800, "min_temp": 15, "max_temp": 20, "suitability": ["Highly Suitable", "Moderate"]},
    "Pumpkin": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Cucumber": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Bottle Gourd": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Bitter Gourd": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Ridge Gourd": {"min_rain": 600, "max_rain": 1000, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Sweet Corn": {"min_rain": 500, "max_rain": 800, "min_temp": 18, "max_temp": 27, "suitability": ["Highly Suitable", "Moderate"]},
    "Broccoli": {"min_rain": 500, "max_rain": 1000, "min_temp": 15, "max_temp": 20, "suitability": ["Highly Suitable"]},
    "Lettuce": {"min_rain": 400, "max_rain": 800, "min_temp": 10, "max_temp": 20, "suitability": ["Highly Suitable"]},
    "Bell Pepper (Capsicum)": {"min_rain": 600, "max_rain": 1200, "min_temp": 18, "max_temp": 25, "suitability": ["Highly Suitable"]},

    # --- SPICES & CONDIMENTS ---
    "Turmeric": {"min_rain": 1000, "max_rain": 1500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Ginger": {"min_rain": 1000, "max_rain": 1500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Black Pepper": {"min_rain": 2000, "max_rain": 3000, "min_temp": 20, "max_temp": 32, "suitability": ["Highly Suitable"]},
    "Cardamom": {"min_rain": 1500, "max_rain": 2500, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Cloves": {"min_rain": 1500, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Cinnamon": {"min_rain": 1750, "max_rain": 3500, "min_temp": 25, "max_temp": 35, "suitability": ["Highly Suitable"]},
    "Cumin": {"min_rain": 300, "max_rain": 2700, "min_temp": 20, "max_temp": 30, "suitability": ["Moderate", "Unsuitable"]},
    "Coriander": {"min_rain": 500, "max_rain": 1000, "min_temp": 10, "max_temp": 29, "suitability": ["Highly Suitable", "Moderate"]},
    "Fenugreek (Methi)": {"min_rain": 400, "max_rain": 800, "min_temp": 10, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Nutmeg": {"min_rain": 1500, "max_rain": 2500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Fennel": {"min_rain": 500, "max_rain": 800, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Ajwain": {"min_rain": 400, "max_rain": 700, "min_temp": 20, "max_temp": 30, "suitability": ["Moderate", "Unsuitable"]},
    "Vanilla": {"min_rain": 2000, "max_rain": 3000, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},

    # --- MEDICINAL & HERBAL ---
    "Aloe Vera": {"min_rain": 300, "max_rain": 800, "min_temp": 13, "max_temp": 27, "suitability": ["Moderate", "Unsuitable"]},
    "Ashwagandha": {"min_rain": 500, "max_rain": 800, "min_temp": 20, "max_temp": 35, "suitability": ["Moderate", "Unsuitable"]},
    "Neem": {"min_rain": 450, "max_rain": 1200, "min_temp": 20, "max_temp": 40, "suitability": ["Moderate", "Unsuitable"]},
    "Tulsi (Holy Basil)": {"min_rain": 600, "max_rain": 1200, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Stevia": {"min_rain": 1400, "max_rain": 1500, "min_temp": 20, "max_temp": 32, "suitability": ["Highly Suitable"]},
    "Amla (Indian Gooseberry)": {"min_rain": 600, "max_rain": 1000, "min_temp": 15, "max_temp": 45, "suitability": ["Highly Suitable", "Moderate"]},
    "Brahmi": {"min_rain": 800, "max_rain": 1500, "min_temp": 20, "max_temp": 30, "suitability": ["Highly Suitable"]},
    "Lemongrass": {"min_rain": 1500, "max_rain": 2500, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Moringa (Drumstick)": {"min_rain": 300, "max_rain": 1500, "min_temp": 25, "max_temp": 40, "suitability": ["Moderate", "Unsuitable"]},

    # --- FLOWERS (FLORICULTURE) ---
    "Rose": {"min_rain": 600, "max_rain": 1000, "min_temp": 15, "max_temp": 28, "suitability": ["Highly Suitable"]},
    "Jasmine": {"min_rain": 800, "max_rain": 1500, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Marigold": {"min_rain": 500, "max_rain": 1000, "min_temp": 18, "max_temp": 30, "suitability": ["Highly Suitable", "Moderate"]},
    "Orchid": {"min_rain": 1500, "max_rain": 2500, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
    "Hibiscus": {"min_rain": 1000, "max_rain": 1500, "min_temp": 20, "max_temp": 35, "suitability": ["Highly Suitable", "Moderate"]},
    "Tulip": {"min_rain": 500, "max_rain": 800, "min_temp": 5, "max_temp": 15, "suitability": ["Highly Suitable"]},
    "Lavender": {"min_rain": 300, "max_rain": 700, "min_temp": 10, "max_temp": 30, "suitability": ["Moderate", "Unsuitable"]},
    "Chrysanthemum": {"min_rain": 500, "max_rain": 1000, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable", "Moderate"]},
    "Lily": {"min_rain": 600, "max_rain": 1200, "min_temp": 15, "max_temp": 25, "suitability": ["Highly Suitable"]},
}

# --- CROP ENCYCLOPEDIA DETAILS ---
CROP_DETAILS = {
    # Cereals
    "Rice": {"description": "Staple food for over half the world.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "1000-2500 mm", "soil_type": "Clayey", "growing_season": "Kharif", "climate": "Hot/Humid"},
    "Wheat": {"description": "Major staple; requires cool growing season.", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "500-900 mm", "soil_type": "Loam", "growing_season": "Rabi", "climate": "Cool/Moist"},
    "Maize (Corn)": {"description": "Queen of Cereals; versatile crop.", "ideal_temp": "18°C - 30°C", "ideal_rainfall": "500-800 mm", "soil_type": "Loam", "growing_season": "Kharif/Rabi", "climate": "Warm"},
    "Barley": {"description": "Hardy cereal; used for malt/fodder.", "ideal_temp": "12°C - 25°C", "ideal_rainfall": "300-600 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Sorghum": {"description": "Drought-hardy cereal for dry regions.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "400-750 mm", "soil_type": "Loamy/Sandy", "growing_season": "Kharif/Rabi", "climate": "Warm/Arid"},
    "Pearl Millet (Bajra)": {"description": "Drought-tolerant; good for sandy soils.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "400-600 mm", "soil_type": "Sandy", "growing_season": "Kharif", "climate": "Hot/Dry"},
    "Finger Millet (Ragi)": {"description": "Rich in calcium; staple in South India.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Red/Loam", "growing_season": "Kharif", "climate": "Tropical"},
    "Oats": {"description": "Healthy grain; primarily used as fodder/health food.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Well-drained Loam", "growing_season": "Rabi", "climate": "Cool/Moist"},
    "Rye": {"description": "Hardy grain; grows in poor soils.", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "400-900 mm", "soil_type": "Sandy/Light", "growing_season": "Rabi", "climate": "Cool"},
    "Buckwheat": {"description": "Pseudo-cereal; fast growing and gluten-free.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "400-700 mm", "soil_type": "Poor/Acidic", "growing_season": "Summer/Kharif", "climate": "Cool/Moist"},

    # Pulses
    "Chickpea": {"description": "King of pulses; protein rich.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "300-500 mm", "soil_type": "Sandy/Clay Loam", "growing_season": "Rabi", "climate": "Cool/Dry"},
    "Pigeon Pea": {"description": "Major pulse; drought tolerant.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Kharif", "climate": "Warm"},
    "Lentil": {"description": "Nutritious and fast cooking.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "300-500 mm", "soil_type": "Loam/Clay", "growing_season": "Rabi", "climate": "Cool"},
    "Black Gram": {"description": "Rich in minerals; short duration.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Loam/Clay", "growing_season": "Kharif", "climate": "Warm"},
    "Green Gram": {"description": "Digestible protein; versatile pulse.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Loam/Sandy", "growing_season": "Kharif", "climate": "Warm"},
    "Horse Gram": {"description": "Extremely drought-hardy legume.", "ideal_temp": "25°C - 30°C", "ideal_rainfall": "300-900 mm", "soil_type": "All soil types", "growing_season": "Kharif/Rabi", "climate": "Arid"},
    "Cowpea": {"description": "Multi-purpose legume; black-eyed pea.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "400-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Kharif", "climate": "Warm"},
    "Kidney Bean": {"description": "Popular pulse; requires consistent moisture.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Rich Loam", "growing_season": "Rabi", "climate": "Cool/Temperate"},
    "French Bean": {"description": "Mainly grown as a vegetable/pulse.", "ideal_temp": "18°C - 28°C", "ideal_rainfall": "900-1200 mm", "soil_type": "Well-drained Loam", "growing_season": "Rabi/Kharif", "climate": "Warm/Moderate"},
    "Peas": {"description": "Cool season pulse; soil improver.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "400-800 mm", "soil_type": "Rich Loam", "growing_season": "Rabi", "climate": "Cool"},

    # Oilseeds
    "Soybean": {"description": "High protein and oil content.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-900 mm", "soil_type": "Fertile Loam", "growing_season": "Kharif", "climate": "Warm/Humid"},
    "Groundnut": {"description": "Major oilseed; nitrogen fixer.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-750 mm", "soil_type": "Sandy Loam", "growing_season": "Kharif", "climate": "Tropical"},
    "Sunflower": {"description": "Photo-insensitive oilseed.", "ideal_temp": "20°C - 28°C", "ideal_rainfall": "400-700 mm", "soil_type": "Loam", "growing_season": "All Seasons", "climate": "Cool/Warm"},
    "Rapeseed/Mustard": {"description": "Key oilseed of Rabi season.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "500-800 mm", "soil_type": "Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Sesame": {"description": "Ancient drought-resistant oilseed.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "500-800 mm", "soil_type": "Well-drained", "growing_season": "Kharif", "climate": "Warm"},
    "Linseed": {"description": "Source of oil and fibre (flax).", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "450-750 mm", "soil_type": "Clay Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Castor": {"description": "Non-edible oil; high industrial value.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-1000 mm", "soil_type": "All types", "growing_season": "Kharif/Rabi", "climate": "Warm"},
    "Safflower": {"description": "Very drought-hardy oilseed.", "ideal_temp": "15°C - 30°C", "ideal_rainfall": "300-600 mm", "soil_type": "Deep Clay/Loam", "growing_season": "Rabi", "climate": "Arid"},

    # Cash/Plantation
    "Sugarcane": {"description": "Main source of sugar.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "1000-2000 mm", "soil_type": "Deep Loam", "growing_season": "Year-round", "climate": "Hot/Humid"},
    "Cotton": {"description": "White Gold; premier fibre.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Black Soil", "growing_season": "Kharif", "climate": "Tropical"},
    "Jute": {"description": "Golden Fibre; eco-friendly.", "ideal_temp": "24°C - 35°C", "ideal_rainfall": "1500-2000 mm", "soil_type": "Riverine Alluvial", "growing_season": "Kharif", "climate": "Hot/Humid"},
    "Tea": {"description": "Queen of beverages.", "ideal_temp": "15°C - 30°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Acidic Loam", "growing_season": "Perennial", "climate": "Warm/Humid"},
    "Coffee": {"description": "Popular beverage; shade loving.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "1200-2000 mm", "soil_type": "Well-drained Loam", "growing_season": "Perennial", "climate": "Tropical Highlands"},
    "Rubber": {"description": "Source of natural latex.", "ideal_temp": "25°C - 30°C", "ideal_rainfall": "2000-3000 mm", "soil_type": "Laterite", "growing_season": "Perennial", "climate": "Tropical"},
    "Coconut": {"description": "Tree of life.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Coastal/Alluvial", "growing_season": "Perennial", "climate": "Equatorial"},
    "Oil Palm": {"description": "Highest oil yield per hectare.", "ideal_temp": "24°C - 28°C", "ideal_rainfall": "2000-3000 mm", "soil_type": "Rich Deep soil", "growing_season": "Perennial", "climate": "Tropical"},
    "Cashew": {"description": "Valuable nut crop; grows in poor soils.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "1000-2000 mm", "soil_type": "Sandy/Laterite", "growing_season": "Perennial", "climate": "Tropical"},
    "Arecanut": {"description": "Palm nut; common in coastal regions.", "ideal_temp": "14°C - 36°C", "ideal_rainfall": "2000-4000 mm", "soil_type": "Laterite/Red", "growing_season": "Perennial", "climate": "Coastal/Humid"},
    "Tobacco": {"description": "High value cash crop.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Warm"},
    "Cocoa": {"description": "Source of chocolate.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Rich Loam", "growing_season": "Perennial", "climate": "Tropical"},

    # Fruits
    "Mango": {"description": "King of Fruits; summer delicacy.", "ideal_temp": "24°C - 30°C", "ideal_rainfall": "750-1500 mm", "soil_type": "Alluvial", "growing_season": "Summer", "climate": "Tropical"},
    "Banana": {"description": "Energy rich fruit; year-round.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1200-2500 mm", "soil_type": "Rich Loamy", "growing_season": "Year-round", "climate": "Tropical"},
    "Citrus": {"description": "Vitamin C rich; Oranges, Lemons.", "ideal_temp": "15°C - 30°C", "ideal_rainfall": "1000-2000 mm", "soil_type": "Deep well-drained", "growing_season": "Year-round", "climate": "Sub-tropical"},
    "Grapes": {"description": "Vine fruit for table/wine.", "ideal_temp": "15°C - 30°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Summer", "climate": "Temperate"},
    "Apple": {"description": "Hilly region fruit.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "750-1200 mm", "soil_type": "Loam", "growing_season": "Autumn", "climate": "Cool"},
    "Papaya": {"description": "Digestive fruit; fast growing.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1200-2000 mm", "soil_type": "Well-drained Loam", "growing_season": "Year-round", "climate": "Tropical"},
    "Guava": {"description": "Adaptable tropical fruit.", "ideal_temp": "23°C - 28°C", "ideal_rainfall": "1000-2000 mm", "soil_type": "All types", "growing_season": "Summer/Winter", "climate": "Tropical"},
    "Pomegranate": {"description": "Hardy fruit for dry areas.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "500-800 mm", "soil_type": "Deep Loam", "growing_season": "Winter/Summer", "climate": "Arid/Semi-arid"},
    "Pineapple": {"description": "Exotic tropical fruit.", "ideal_temp": "22°C - 30°C", "ideal_rainfall": "1000-1500 mm", "soil_type": "Acidic Sandy Loam", "growing_season": "Year-round", "climate": "Tropical"},
    "Strawberry": {"description": "Delicate berry fruit.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "600-1200 mm", "soil_type": "Rich Sandy Loam", "growing_season": "Winter/Spring", "climate": "Temperate"},
    "Watermelon": {"description": "Summer hydration fruit.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "400-600 mm", "soil_type": "Sandy", "growing_season": "Summer", "climate": "Hot/Dry"},
    "Muskmelon": {"description": "Fragrant summer fruit.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "400-600 mm", "soil_type": "Sandy", "growing_season": "Summer", "climate": "Hot/Dry"},
    "Jackfruit": {"description": "Largest tree-borne fruit.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Rich Deep soil", "growing_season": "Summer", "climate": "Tropical"},
    "Litchi": {"description": "Sweet pulpy summer fruit.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1200-1500 mm", "soil_type": "Alluvial", "growing_season": "Summer", "climate": "Sub-tropical"},
    "Sapota (Chiku)": {"description": "Delicious sugar-rich fruit.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1200-2500 mm", "soil_type": "All types/Coastal", "growing_season": "Year-round", "climate": "Coastal/Tropical"},
    "Custard Apple": {"description": "Hardy fruit for marginal lands.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy/Rocky", "growing_season": "Winter", "climate": "Tropical"},
    "Pear": {"description": "Crisp fruit for cool climates.", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "750-1000 mm", "soil_type": "Deep Loam", "growing_season": "Autumn", "climate": "Cool"},
    "Peach": {"description": "Soft drupe fruit.", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "750-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Summer", "climate": "Temperate"},
    "Plum": {"description": "Succulent drupe fruit.", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "750-1000 mm", "soil_type": "Well-drained", "growing_season": "Summer", "climate": "Temperate"},
    "Apricot": {"description": "Nutritious stone fruit.", "ideal_temp": "7°C - 25°C", "ideal_rainfall": "750-1000 mm", "soil_type": "Good drainage", "growing_season": "Summer", "climate": "Cool"},
    "Cherry": {"description": "Valuable stone fruit.", "ideal_temp": "7°C - 20°C", "ideal_rainfall": "750-1200 mm", "soil_type": "Deep Loam", "growing_season": "Summer", "climate": "Cool"},
    "Kiwi": {"description": "Exotic high-value fruit.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "1000-1500 mm", "soil_type": "Rich Loam", "growing_season": "Winter/Spring", "climate": "Temperate"},
    "Dragon Fruit": {"description": "Exotic cactus fruit; very hardy.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "500-1500 mm", "soil_type": "Sandy/Well-drained", "growing_season": "Year-round", "climate": "Arid/Tropical"},

    # Vegetables
    "Potato": {"description": "Major tuber; global staple.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Tomato": {"description": "Versatile kitchen vegetable.", "ideal_temp": "20°C - 25°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Loam", "growing_season": "All Seasons", "climate": "Warm"},
    "Onion": {"description": "Essential culinary staple.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "500-700 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi/Kharif", "climate": "Temperate"},
    "Chili": {"description": "Spice and vegetable.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "600-1200 mm", "soil_type": "Loam", "growing_season": "All Seasons", "climate": "Warm"},
    "Brinjal": {"description": "Eggplant; hardy vegetable.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "750-1200 mm", "soil_type": "Rich Loam", "growing_season": "All Seasons", "climate": "Warm"},
    "Okra": {"description": "Lady's finger; warm season.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "750-1000 mm", "soil_type": "Loam", "growing_season": "Summer/Kharif", "climate": "Hot"},
    "Cabbage": {"description": "Leafy winter vegetable.", "ideal_temp": "15°C - 20°C", "ideal_rainfall": "500-700 mm", "soil_type": "Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Cauliflower": {"description": "Winter flower vegetable.", "ideal_temp": "15°C - 20°C", "ideal_rainfall": "500-700 mm", "soil_type": "Rich Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Carrot": {"description": "Vitamin A rich root.", "ideal_temp": "15°C - 20°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Spinach": {"description": "Iron-rich leafy green.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "400-800 mm", "soil_type": "Rich Loam", "growing_season": "Winter", "climate": "Cool"},
    "Radish": {"description": "Fast-growing root vegetable.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "400-800 mm", "soil_type": "Sandy", "growing_season": "Winter", "climate": "Cool"},
    "Turnip": {"description": "Cool season hearty root.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "400-800 mm", "soil_type": "Loam", "growing_season": "Winter", "climate": "Cool"},
    "Beetroot": {"description": "Nutritious deep-red root.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "400-800 mm", "soil_type": "Loam", "growing_season": "Winter", "climate": "Cool/Moderate"},
    "Garlic": {"description": "Essential medicinal spice.", "ideal_temp": "15°C - 20°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Cool"},
    "Pumpkin": {"description": "Large vine-borne vegetable.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Summer/Kharif", "climate": "Warm"},
    "Cucumber": {"description": "Cooling salad vegetable.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Summer", "climate": "Warm"},
    "Bottle Gourd": {"description": "Easy to digest vegetable.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Sandy Loam", "growing_season": "Summer/Kharif", "climate": "Warm"},
    "Bitter Gourd": {"description": "Medicinal bitter vegetable.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Loam", "growing_season": "Summer/Kharif", "climate": "Hot"},
    "Ridge Gourd": {"description": "Fibrous healthy vegetable.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Loam", "growing_season": "Summer/Kharif", "climate": "Warm"},
    "Sweet Corn": {"description": "Delicious early-harvest grain.", "ideal_temp": "18°C - 27°C", "ideal_rainfall": "500-800 mm", "soil_type": "Rich Loam", "growing_season": "Summer/Rabi", "climate": "Warm"},
    "Broccoli": {"description": "Superfood flower vegetable.", "ideal_temp": "15°C - 20°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Rich Loam", "growing_season": "Winter", "climate": "Cool"},
    "Lettuce": {"description": "Primary salad leafy green.", "ideal_temp": "10°C - 20°C", "ideal_rainfall": "400-800 mm", "soil_type": "Rich/Sandy", "growing_season": "Winter", "climate": "Cool"},
    "Bell Pepper (Capsicum)": {"description": "Crunchy salad vegetable.", "ideal_temp": "18°C - 25°C", "ideal_rainfall": "600-1200 mm", "soil_type": "Rich Loam", "growing_season": "Rabi/Kharif", "climate": "Moderate"},

    # Spices
    "Turmeric": {"description": "Golden spice; medicinal value.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1000-1500 mm", "soil_type": "Sandy Loam", "growing_season": "Year-round", "climate": "Tropical"},
    "Ginger": {"description": "Aromatic rhizome.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1000-1500 mm", "soil_type": "Rich Loam", "growing_season": "Year-round", "climate": "Tropical"},
    "Black Pepper": {"description": "King of Spices.", "ideal_temp": "20°C - 32°C", "ideal_rainfall": "2000-3000 mm", "soil_type": "Laterite", "growing_season": "Perennial", "climate": "Humid Tropical"},
    "Cardamom": {"description": "Queen of Spices.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Forest Loam", "growing_season": "Perennial", "climate": "Warm/Humid"},
    "Cloves": {"description": "Aromatic flower buds.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Rich soil", "growing_season": "Perennial", "climate": "Humid Tropical"},
    "Cinnamon": {"description": "Fragrant tree bark spice.", "ideal_temp": "25°C - 35°C", "ideal_rainfall": "1750-3500 mm", "soil_type": "Sandy Loam", "growing_season": "Perennial", "climate": "Tropical"},
    "Cumin": {"description": "Essential seed spice.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "300-2700 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Arid"},
    "Coriander": {"description": "Leaf and seed spice.", "ideal_temp": "10°C - 29°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Loam", "growing_season": "Winter/Rabi", "climate": "Cool/Dry"},
    "Fenugreek (Methi)": {"description": "Herb and spice legume.", "ideal_temp": "10°C - 25°C", "ideal_rainfall": "400-800 mm", "soil_type": "Well-drained", "growing_season": "Rabi", "climate": "Cool"},
    "Nutmeg": {"description": "Perennial tree spice.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Clay Loam", "growing_season": "Perennial", "climate": "Tropical"},
    "Fennel": {"description": "Aromatic digestive spice.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy Loam", "growing_season": "Rabi", "climate": "Moderate"},
    "Ajwain": {"description": "Spicy digestive seed.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "400-700 mm", "soil_type": "All types", "growing_season": "Rabi", "climate": "Dry"},
    "Vanilla": {"description": "Aromatic bean from orchid.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "2000-3000 mm", "soil_type": "Humus rich", "growing_season": "Perennial", "climate": "Tropical"},

    # Medicinal
    "Aloe Vera": {"description": "Succulent for skin and health.", "ideal_temp": "13°C - 27°C", "ideal_rainfall": "300-800 mm", "soil_type": "Sandy", "growing_season": "Year-round", "climate": "Arid"},
    "Ashwagandha": {"description": "Important Ayurvedic herb.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy/Light", "growing_season": "Kharif/Rabi", "climate": "Warm"},
    "Neem": {"description": "Powerful medicinal tree.", "ideal_temp": "20°C - 40°C", "ideal_rainfall": "450-1200 mm", "soil_type": "All soils", "growing_season": "Perennial", "climate": "Arid/Tropical"},
    "Tulsi (Holy Basil)": {"description": "Revered medicinal herb.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "600-1200 mm", "soil_type": "Loam", "growing_season": "Year-round", "climate": "Tropical"},
    "Stevia": {"description": "Natural zero-calorie sweetener.", "ideal_temp": "20°C - 32°C", "ideal_rainfall": "1400-1500 mm", "soil_type": "Loam", "growing_season": "Year-round", "climate": "Warm/Sunny"},
    "Amla (Indian Gooseberry)": {"description": "Richest Vitamin C source.", "ideal_temp": "15°C - 45°C", "ideal_rainfall": "600-1000 mm", "soil_type": "All/Hardy", "growing_season": "Winter/Summer", "climate": "Arid/Tropical"},
    "Brahmi": {"description": "Memory-enhancing herb.", "ideal_temp": "20°C - 30°C", "ideal_rainfall": "800-1500 mm", "soil_type": "Marshy/Wet", "growing_season": "Year-round", "climate": "Humid"},
    "Lemongrass": {"description": "Essential oil herb.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Sandy/Loam", "growing_season": "Year-round", "climate": "Tropical"},
    "Moringa (Drumstick)": {"description": "Nutritional superfood tree.", "ideal_temp": "25°C - 40°C", "ideal_rainfall": "300-1500 mm", "soil_type": "All/Sandy Loam", "growing_season": "Year-round", "climate": "Hot/Dry"},

    # Flowers
    "Rose": {"description": "Symbol of love; major cut flower.", "ideal_temp": "15°C - 28°C", "ideal_rainfall": "600-1000 mm", "soil_type": "Rich Loam", "growing_season": "Winter/Spring", "climate": "Temperate"},
    "Jasmine": {"description": "Fragrant ornamental flower.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "800-1500 mm", "soil_type": "Well-drained", "growing_season": "Summer/Monsoon", "climate": "Warm"},
    "Marigold": {"description": "Common festive flower.", "ideal_temp": "18°C - 30°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Loam", "growing_season": "All Seasons", "climate": "Warm"},
    "Orchid": {"description": "Exotic high-value flower.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "1500-2500 mm", "soil_type": "Bark/Moss/Rich", "growing_season": "Year-round", "climate": "Humid"},
    "Hibiscus": {"description": "Tropical ornamental flower.", "ideal_temp": "20°C - 35°C", "ideal_rainfall": "1000-1500 mm", "soil_type": "Well-drained", "growing_season": "Summer/Monsoon", "climate": "Tropical"},
    "Tulip": {"description": "Winter bulb flower.", "ideal_temp": "5°C - 15°C", "ideal_rainfall": "500-800 mm", "soil_type": "Sandy", "growing_season": "Winter", "climate": "Cold"},
    "Lavender": {"description": "Aromatic medicinal flower.", "ideal_temp": "10°C - 30°C", "ideal_rainfall": "300-700 mm", "soil_type": "Sandy/Rocky", "growing_season": "Summer", "climate": "Mediterranean"},
    "Chrysanthemum": {"description": "Autumn-flowering ornamental.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "500-1000 mm", "soil_type": "Rich Loam", "growing_season": "Winter/Autumn", "climate": "Moderate"},
    "Lily": {"description": "Elegant bulb flower.", "ideal_temp": "15°C - 25°C", "ideal_rainfall": "600-1200 mm", "soil_type": "Rich Loam", "growing_season": "Spring/Summer", "climate": "Moderate"},
}

CROP_ENCYCLOPEDIA = [
    {
        "category": "Food Crops",
        "subcategories": [
            {
                "name": "Cereals & Grains",
                "icon": "🌾",
                "crops": ["Rice", "Wheat", "Maize (Corn)", "Barley", "Sorghum", "Pearl Millet (Bajra)", "Finger Millet (Ragi)", "Oats", "Rye", "Buckwheat", "Sweet Corn"]
            },
            {
                "name": "Pulses & Legumes",
                "icon": "🌱",
                "crops": ["Chickpea", "Pigeon Pea", "Lentil", "Black Gram", "Green Gram", "Horse Gram", "Cowpea", "Kidney Bean", "French Bean", "Peas"]
            }
        ]
    },
    {
        "category": "Oilseed Crops",
        "id": "oilseeds",
        "crops": ["Groundnut", "Mustard", "Soybean", "Sunflower", "Sesame", "Linseed", "Castor", "Safflower"]
    },
    {
        "category": "Cash & Plantation Crops",
        "id": "cash",
        "crops": ["Sugarcane", "Cotton", "Jute", "Tobacco", "Tea", "Coffee", "Cocoa", "Rubber", "Coconut", "Oil Palm", "Cashew", "Arecanut", "Vanilla"]
    },
    {
        "category": "Horticultural Crops",
        "subcategories": [
            {
                "name": "Fruits",
                "icon": "🍎",
                "crops": ["Mango", "Banana", "Citrus", "Grapes", "Apple", "Papaya", "Guava", "Pomegranate", "Pineapple", "Strawberry", "Watermelon", "Muskmelon", "Jackfruit", "Litchi", "Sapota (Chiku)", "Custard Apple", "Pear", "Peach", "Plum", "Apricot", "Cherry", "Kiwi", "Dragon Fruit"]
            },
            {
                "name": "Vegetables",
                "icon": "🥦",
                "crops": ["Potato", "Tomato", "Onion", "Chili", "Brinjal", "Okra", "Cabbage", "Cauliflower", "Carrot", "Garlic", "Spinach", "Radish", "Turnip", "Beetroot", "Pumpkin", "Cucumber", "Bottle Gourd", "Bitter Gourd", "Ridge Gourd", "Broccoli", "Lettuce", "Bell Pepper (Capsicum)"]
            }
        ]
    },
    {
        "category": "Spices & Spicery",
        "id": "spices",
        "crops": ["Turmeric", "Ginger", "Black Pepper", "Cardamom", "Cloves", "Cinnamon", "Cumin", "Coriander", "Fenugreek (Methi)", "Nutmeg", "Fennel", "Ajwain"]
    },
    {
        "category": "Medicinal & Herbal",
        "id": "medicinal",
        "crops": ["Aloe Vera", "Ashwagandha", "Neem", "Tulsi (Holy Basil)", "Stevia", "Amla (Indian Gooseberry)", "Brahmi", "Lemongrass", "Moringa (Drumstick)"]
    },
    {
        "category": "Floriculture (Flowers)",
        "id": "flowers",
        "crops": ["Rose", "Jasmine", "Marigold", "Orchid", "Hibiscus", "Tulip", "Lavender", "Chrysanthemum", "Lily"]
    }
]
