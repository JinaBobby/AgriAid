# streamlit_app.py
import streamlit as st
from utils.recommend_crop import recommend_crop
from utils.fertilizer_logic import recommend_fertilizer

st.title("🌾 AgriAid - Crop & Fertilizer Recommendation")

st.header("Enter Soil and Environmental Parameters")

N =st.slider("Nitrogen (N)", 0, 140)
P =st.slider("Phosphorus (p)", 5, 145)
K =st.slider("Potassium (K)", 5, 205)
temperature = st.slider("Temperature (°C)", 10.0, 45.0)
humidity = st.slider("Humidity (%)", 10.0, 100.0)
ph = st.slider("Soil pH", 3.5, 9.5)
rainfall = st.slider("Rainfall (mm)", 20.0, 300.0)

if st.button("Recommend Crop"):
    crop = recommend_crop([N, P, K, temperature, humidity, ph, rainfall])

    st.success(f"Recommended Crop: 🌱 **{crop.capitalize()}**")

if st.button("Fertilizer Advice"):
    advice =recommend_fertilizer(N, P, K)
    st.info(f"💡 {advice}")
