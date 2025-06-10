def recommend_fertilizer(crop_name):
    fertilizer_map = {
        "rice": "Urea + Potash",
        "wheat": "NPK 20-20-0",
        "maize": "DAP + Urea",
        "sugarcane": "Organic compost + Urea",
        "cotton": "Phosphate rich organic manure",
        "groundnut": "Gypsum + DAP",
    }

    return fertilizer_map.get(crop_name.lower(), "Generic NPK fertilizer")
