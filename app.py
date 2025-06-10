# app.py
from utils.recommend_crop import recommend_crop

def main():
    print("\n🌾 Welcome to AgriAid - Crop Recommendation System 🌱\n")

    try:
        N = float(input("Enter Nitrogen content (N): "))
        P = float(input("Enter Phosphorus content (P): "))
        K = float(input("Enter Potassium content (K): "))
        temperature = float(input("Enter Temperature (°C): "))
        humidity = float(input("Enter Humidity (%): "))
        ph = float(input("Enter pH value: "))
        rainfall = float(input("Enter Rainfall (mm): "))

        features = [N, P, K, temperature, humidity, ph, rainfall]
        crop = recommend_crop(features)
        print(f"\n✅ Recommended Crop: 🌿 {crop}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
