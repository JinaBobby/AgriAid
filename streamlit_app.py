# streamlit_app.py
import streamlit as st
from utils.recommend_crop import recommend_crop

st.set_page_config(page_title="AgriAid 🌱", layout="centered")

st.title("🌾 AgriAid - Smart Crop Recommender")
st.markdown("Enter soil and environmental conditions to get the best crop recommendation!")

# Input sliders / fields
N = st.slider("Nitrogen (N)", 0, 140, 50)
P = st.slider("Phosphorus (P)", 5, 145, 50)
K = st.slider("Potassium (K)", 5, 205, 50)
temperature = st.slider("Temperature (°C)", 10.0, 45.0, 25.0)
humidity = st.slider("Humidity (%)", 10.0, 100.0, 50.0)
ph = st.slider("pH Level", 3.5, 9.5, 6.5)
rainfall = st.slider("Rainfall (mm)", 20.0, 300.0, 100.0)

if st.button("🌱 Recommend Crop"):
    try:
        features = [N, P, K, temperature, humidity, ph, rainfall]
        crop = recommend_crop(features)
        st.success(f"✅ Recommended Crop: **{crop.upper()}**")
    except Exception as e:
        st.error(f"❌ Error: {e}")
