# model/trainer.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load dataset
df = pd.read_csv('data/Crop_recommendation.csv')

# Features and labels
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
os.makedirs('model', exist_ok=True)
with open('model/crop_predictor.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as crop_predictor.pkl")
