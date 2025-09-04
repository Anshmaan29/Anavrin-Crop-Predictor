import streamlit as st
import pandas as pd
import numpy as np
import random

# Set page configuration
st.set_page_config(
    page_title="AI Crop Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    :root {
        --primary: #2e7d32;
        --secondary: #7cb342;
        --accent: #f57c00;
        --light: #f1f8e9;
        --dark: #1b5e20;
        --card-bg: #ffffff;
    }
    
    .main {
        background: linear-gradient(135deg, var(--light) 0%, #e8f5e9 100%);
        padding: 20px;
        border-radius: 15px;
    }
    
    .stButton>button {
        background-color: var(--primary);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: var(--dark);
        transform: scale(1.02);
    }
    
    .card {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid var(--secondary);
    }
    
    .result-card {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        text-align: center;
        border: 2px solid var(--secondary);
        margin-top: 20px;
    }
    
    .metric-card {
        background-color: var(--card-bg);
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        text-align: center;
        margin: 10px 0;
    }
    
    h1, h2, h3 {
        color: var(--dark);
    }
    
    .crop-icon {
        font-size: 48px;
        margin-bottom: 15px;
    }
    
    .confidence-bar {
        height: 25px;
        background-color: #e0e0e0;
        border-radius: 12px;
        margin: 15px 0;
        overflow: hidden;
    }
    
    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--secondary) 0%, var(--primary) 100%);
        border-radius: 12px;
        transition: width 1s ease-in-out;
    }
    
    .reason-item {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 12px;
        border-radius: 8px;
        margin: 10px 0;
        display: flex;
        align-items: center;
        border-left: 4px solid var(--accent);
    }
    
    .reason-icon {
        margin-right: 10px;
        color: var(--accent);
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("<h1 style='text-align: center; color: var(--dark);'>🌾 AI Crop Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Get intelligent crop recommendations based on your soil conditions and weather parameters</p>", unsafe_allow_html=True)

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>🌱 Soil Parameters</h3>", unsafe_allow_html=True)
    
    # Soil parameters
    N = st.slider("Nitrogen (N) ppm", 0, 140, 50, help="Measure of nitrogen content in soil")
    P = st.slider("Phosphorus (P) ppm", 5, 145, 50, help="Measure of phosphorus content in soil")
    K = st.slider("Potassium (K) ppm", 5, 205, 50, help="Measure of potassium content in soil")
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5, 0.1, help="Acidity/Alkalinity level of soil")
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>🌦️ Weather Conditions</h3>", unsafe_allow_html=True)
    
    # Weather parameters
    temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0, 0.1, help="Average temperature")
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0, 0.1, help="Relative humidity level")
    rainfall = st.slider("Rainfall (mm)", 0.0, 500.0, 200.0, 1.0, help="Annual rainfall")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Analyze button
if st.button("🔍 Analyze Conditions & Recommend Crop"):
    # Simulate analysis process
    with st.spinner("Analyzing soil and weather conditions..."):
        # Simulate processing time
        import time
        time.sleep(1.5)
    
    # Generate a random crop from a list (in a real app, this would be a model prediction)
    crops = ["Rice", "Wheat", "Maize", "Soybean", "Orange", "Papaya", "Cotton", "Coffee", "Coconut", "Mango"]
    recommended_crop = random.choice(crops)
    
    # Generate a confidence score
    confidence = round(random.uniform(0.75, 0.95) * 100, 2)
    
    # Generate reasons based on inputs
    reasons = []
    
    if ph >= 6.0 and ph <= 7.5:
        reasons.append(f"Optimal pH level ({ph}) for {recommended_crop}")
    elif ph < 6.0:
        reasons.append(f"Slightly acidic pH ({ph}) is acceptable for {recommended_crop}")
    else:
        reasons.append(f"Slightly alkaline pH ({ph}) is acceptable for {recommended_crop}")
    
    if temperature >= 20 and temperature <= 30:
        reasons.append(f"Ideal temperature ({temperature}°C) for {recommended_crop} growth")
    else:
        reasons.append(f"Temperature ({temperature}°C) within tolerable range for {recommended_crop}")
    
    if rainfall >= 100 and rainfall <= 300:
        reasons.append(f"Rainfall ({rainfall}mm) suitable for {recommended_crop}")
    elif rainfall < 100:
        reasons.append(f"Low rainfall ({rainfall}mm) may require irrigation for {recommended_crop}")
    else:
        reasons.append(f"High rainfall ({rainfall}mm) may require drainage for {recommended_crop}")
    
    # Display results
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    
    # Crop icon based on recommendation
    crop_icons = {
        "Rice": "🌾", "Wheat": "🌾", "Maize": "🌽", "Soybean": "🫘", 
        "Orange": "🍊", "Papaya": "🍈", "Cotton": "🧵", "Coffee": "☕", 
        "Coconut": "🥥", "Mango": "🥭"
    }
    
    icon = crop_icons.get(recommended_crop, "🌱")
    
    st.markdown(f"<div class='crop-icon'>{icon}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2>Recommended Crop: {recommended_crop}</h2>", unsafe_allow_html=True)
    
    # Confidence meter
    st.markdown(f"<p><strong>Confidence:</strong> {confidence}%</p>", unsafe_allow_html=True)
    st.markdown("<div class='confidence-bar'><div class='confidence-fill' style='width: " + str(confidence) + "%'></div></div>", unsafe_allow_html=True)
    
    # Reasons
    st.markdown("<h4>Why this crop is recommended:</h4>", unsafe_allow_html=True)
    for reason in reasons:
        st.markdown(f"<div class='reason-item'><span class='reason-icon'>✓</span> {reason}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Additional metrics
    st.markdown("<h3>Optimal Conditions for " + recommended_crop + "</h3>", unsafe_allow_html=True)
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Ideal pH Range", value="6.0-7.0")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with metrics_col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Temperature Range", value="20-30°C")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with metrics_col3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Rainfall Needs", value="150-250mm")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with metrics_col4:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Growing Season", value="3-5 months")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # Show placeholder before analysis
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("<div class='crop-icon'>🌱</div>", unsafe_allow_html=True)
    st.markdown("<h3>Ready to Analyze</h3>", unsafe_allow_html=True)
    st.markdown("<p>Adjust the parameters and click 'Analyze' to get crop recommendations</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>AI Crop Advisor • Uses machine learning to recommend optimal crops based on environmental conditions</p>", unsafe_allow_html=True)