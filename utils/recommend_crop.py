# utils/recommend_crop.py
import pickle
import pandas as pd

with open("model/crop_predictor.pkl", "rb") as f:
    model = pickle.load(f)


columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

def recommend_crop(data):
    
    df = pd.DataFrame([data], columns=columns)
    prediction = model.predict(df)
    return prediction[0]
