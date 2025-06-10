import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load your dataset
df = pd.read_csv("C:/Users/Jina/OneDrive/Desktop/agriAid/Crop_recommendation.csv")

# Features and target
X = df.drop("label", axis=1)
y = df["label"]

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
os.makedirs("model", exist_ok=True)
with open("model/crop_predictor.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model/crop_predictor.pkl")
