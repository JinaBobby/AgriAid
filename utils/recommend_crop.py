import pickle
import os

    # Load model
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Get absolute path to project root
model_path = os.path.join(PROJECT_ROOT, "model", "crop_predictor.pkl")

print(f"Attempting to load model from: {model_path}")  # DEBUG
print(f"Model file exists: {os.path.exists(model_path)}")  # DEBUG

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

with open(model_path, "rb") as f:
    model = pickle.load(f)

def recommend_crop(features):
    prediction = model.predict([features])
    return prediction[0]
    
