# utils/recommend_crop.py
import pickle
import os

# Load model
model_path = os.path.join("model", "crop_predictor.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

def recommend_crop(features):
    # features should be a list: [N, P, K, temperature, humidity, ph, rainfall]
    prediction = model.predict([features])
    return prediction[0]
