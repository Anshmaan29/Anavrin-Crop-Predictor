# 🌾 AI Crop Recommendation System

An AI-powered web app that recommends the **best crop to grow** based on soil and weather conditions.  
Built with **Python, scikit-learn, and Streamlit** for the [Smart India Hackathon (SIH)].

---

## ✨ Features
- 📊 Input soil & weather data (N, P, K, temperature, humidity, pH, rainfall)
- 🤖 Machine Learning model trained on [Crop Recommendation Dataset]
- ⚡ Real-time crop prediction with confidence score
- 🎨 Clean Streamlit UI with sliders and result cards
- 🖥️ Deployable on localhost or cloud (Streamlit Cloud / Heroku / Render)

---

## 📂 Project Structure
ai-crop-reco/
│── app.py # Streamlit app (UI + prediction)
│── train.py # Training script (builds the ML model)
│── requirements.txt # Dependencies
│── data/
│ └── Crop_recommendation.csv # Dataset
│── .gitignore
│── README.md


📌 Future Upgrades
🌍 Deploy online (Streamlit Cloud / Render / Heroku)
📱 Mobile-friendly UI
🛰️ Add live weather API for auto-inputs
🌱 Multi-crop recommendation with yield prediction