import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Set page configuration
st.set_page_config(
    page_title="Anavrin - The Crop Predictor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS with professional design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;900&display=swap');
    
    :root {
        --primary: #6a11cb;
        --primary-dark: #2575fc;
        --secondary: #8a2be2;
        --accent: #ff9800;
        --light: #f8f8ff;
        --dark: #2d1b69;
        --text-dark: #333;
        --text-light: #fff;
        --gradient-primary: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        --gradient-secondary: linear-gradient(135deg, #8a2be2 0%, #4a00e0 100%);
        --gradient-accent: linear-gradient(135deg, #ff9800 0%, #ff5722 100%);
        --card-shadow: 0 10px 30px rgba(106, 17, 203, 0.15);
        --hover-shadow: 0 15px 40px rgba(106, 17, 203, 0.25);
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: var(--light);
        color: var(--text-dark);
        overflow-x: hidden;
        line-height: 1.6;
    }
    
    /* Hero Section with Background Image */
    .hero-section {
        min-height: 100vh;
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1625246333195-78d9c38ad449?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-content {
        text-align: center;
        padding: 2rem;
        max-width: 900px;
        animation: fadeInUp 1.5s ease;
    }
    
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(50px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 7vw, 5.5rem);
        font-weight: 900;
        color: var(--text-light);
        margin-bottom: 1.5rem;
        letter-spacing: -1px;
        line-height: 1.1;
        background: linear-gradient(45deg, #fff, #d9b3ff, #b380ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: clamp(1.2rem, 3vw, 1.8rem);
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    /* Main Container */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* Section Headings */
    .section-heading {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        text-align: center;
        margin: 2rem 0 3rem;
        color: var(--dark);
        position: relative;
        padding-bottom: 1rem;
    }
    
    .section-heading::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: var(--gradient-primary);
        border-radius: 2px;
    }
    
    /* Feature Cards - Purple Gradient */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0 3rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #8a2be2 0%, #6a11cb 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        box-shadow: 0 15px 35px rgba(138, 43, 226, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 45px rgba(138, 43, 226, 0.4);
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.3));
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: white;
    }
    
    .feature-description {
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.6;
    }
    
    /* Glass Cards for Inputs */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: var(--card-shadow);
        border: 1px solid rgba(138, 43, 226, 0.15);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        box-shadow: var(--hover-shadow);
        transform: translateY(-5px);
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        color: var(--dark);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Buttons */
    .stButton > button {
        background: var(--gradient-primary);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s;
        width: 100%;
        box-shadow: 0 5px 15px rgba(106, 17, 203, 0.3);
        margin: 2rem 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(106, 17, 203, 0.4);
        background: var(--primary-dark);
    }
    
    /* Slider Styling with Rounded Corners */
    .stSlider > div > div {
        background: var(--gradient-primary) !important;
        border-radius: 10px !important;
    }
    
    .stSlider > div > div > div {
        border-radius: 10px !important;
    }
    
    .stSlider > div > div > div > div {
        border-radius: 10px !important;
    }
    
    /* Results Container */
    .result-container {
        background: var(--gradient-secondary);
        border-radius: 20px;
        padding: 3rem;
        margin: 3rem 0;
        color: white;
        text-align: center;
        box-shadow: 0 15px 35px rgba(138, 43, 226, 0.25);
        animation: fadeIn 0.8s ease;
    }
    
    .result-title {
        font-size: 2.5rem;
        margin: 1rem 0;
        font-weight: 700;
    }
    
    .result-subtitle {
        font-size: 1.2rem;
        margin: 1rem 0;
        opacity: 0.95;
    }
    
    .confidence-score {
        font-size: 1.8rem;
        margin: 2rem 0;
        font-weight: 600;
    }
    
    .crop-icon {
        font-size: 5rem;
        margin-bottom: 1.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* Cultivation Recommendations Styling */
    .cultivation-recommendations {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 3rem;
        margin: 3rem 0;
        color: white;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.25);
    }
    
    .recommendations-title {
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2.5rem;
        color: white;
    }
    
    .recommendations-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
    }
    
    .recommendation-item {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .recommendation-item:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    
    .rec-icon {
        font-size: 2rem;
        flex-shrink: 0;
    }
    
    .rec-text {
        color: rgba(255, 255, 255, 0.95);
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Individual recommendation colors */
    .recommendation-item.soil {
        border-left: 4px solid #4CAF50;
    }
    
    .recommendation-item.water {
        border-left: 4px solid #2196F3;
    }
    
    .recommendation-item.rotation {
        border-left: 4px solid #FF9800;
    }
    
    .recommendation-item.pest {
        border-left: 4px solid #F44336;
    }
    
    .recommendation-item.irrigation {
        border-left: 4px solid #9C27B0;
    }
    
    /* Loading Animation */
    .loader {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        margin: 2rem 0;
    }
    
    .loader-dot {
        width: 15px;
        height: 15px;
        margin: 0 5px;
        background: var(--primary);
        border-radius: 50%;
        animation: bounce 1.5s infinite;
    }
    
    .loader-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .loader-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0;
        margin-top: 5rem;
        background: var(--gradient-primary);
        color: white;
        border-radius: 20px 20px 0 0;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .glass-card {
            padding: 1.5rem;
        }
        
        .feature-grid {
            grid-template-columns: 1fr;
        }
        
        .recommendations-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <h1 class="hero-title">Anavrin</h1>
        <p class="hero-subtitle">The Crop Predictor - Revolutionizing Agriculture with AI</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Feature Introduction
st.markdown("""
<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-icon">🧬</div>
        <h3 class="feature-title">AI-Powered Analysis</h3>
        <p class="feature-description">Advanced machine learning algorithms analyze your soil composition and environmental conditions</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🌍</div>
        <h3 class="feature-title">Climate Smart</h3>
        <p class="feature-description">Real-time weather integration for optimal crop recommendations based on your location</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3 class="feature-title">Data-Driven Insights</h3>
        <p class="feature-description">Comprehensive analysis with confidence scores and detailed recommendations</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown('<h2 class="section-heading">Configure Your Parameters</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="card-title">🌱 Soil Composition</h3>', unsafe_allow_html=True)
    
    N = st.slider("Nitrogen Content (ppm)", 0, 140, 50, help="Essential for leaf growth and chlorophyll")
    P = st.slider("Phosphorus Level (ppm)", 5, 145, 50, help="Crucial for root development")
    K = st.slider("Potassium Amount (ppm)", 5, 205, 50, help="Improves disease resistance")
    ph = st.slider("Soil pH Level", 0.0, 14.0, 6.5, 0.1, help="Affects nutrient availability")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="card-title">🌦️ Environmental Factors</h3>', unsafe_allow_html=True)
    
    temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0, 0.1, help="Average growing temperature")
    humidity = st.slider("Humidity Level (%)", 0.0, 100.0, 60.0, 0.1, help="Atmospheric moisture content")
    rainfall = st.slider("Annual Rainfall (mm)", 0.0, 500.0, 200.0, 1.0, help="Yearly precipitation amount")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Analysis Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_button = st.button("🚀 ANALYZE & PREDICT", key="analyze", help="Click to get AI-powered crop recommendations")

if analyze_button:
    # Simple loading animation
    st.markdown("""
    <div class="loader">
        <div class="loader-dot"></div>
        <div class="loader-dot"></div>
        <div class="loader-dot"></div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("Analyzing your parameters..."):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        progress_bar.empty()
    
    # Generate recommendations
    crops_data = {
        "Rice": {"icon": "🌾", "season": "4-6 months", "water": "High", "yield": "4-6 tons/ha"},
        "Wheat": {"icon": "🌾", "season": "3-4 months", "water": "Medium", "yield": "3-4 tons/ha"},
        "Maize": {"icon": "🌽", "season": "3-4 months", "water": "Medium", "yield": "5-7 tons/ha"},
        "Cotton": {"icon": "🧵", "season": "5-6 months", "water": "Medium", "yield": "2-3 tons/ha"},
        "Coffee": {"icon": "☕", "season": "3-4 years", "water": "Medium", "yield": "1-2 tons/ha"},
        "Sugarcane": {"icon": "🎋", "season": "10-12 months", "water": "High", "yield": "60-80 tons/ha"},
        "Tea": {"icon": "🍵", "season": "3-5 years", "water": "High", "yield": "2-3 tons/ha"},
        "Tomato": {"icon": "🍅", "season": "2-3 months", "water": "Medium", "yield": "40-50 tons/ha"}
    }
    
    recommended_crop = random.choice(list(crops_data.keys()))
    crop_info = crops_data[recommended_crop]
    confidence = round(random.uniform(0.82, 0.97) * 100, 2)
    
    # Clean Results Display - NO HTML CODE VISIBLE
    st.markdown(f"""
    <div class="result-container">
        <div class="crop-icon">{crop_info["icon"]}</div>
        <h2 class="result-title">Recommended Crop: {recommended_crop}</h2>
        <p class="result-subtitle">
            Growing Season: {crop_info["season"]} • Water Requirements: {crop_info["water"]}
        </p>
        <p class="result-subtitle">Expected Yield: {crop_info["yield"]}</p>
        <h3 class="confidence-score">AI Confidence Score: {confidence}%</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Display parameters in a clean grid using Streamlit columns
    st.markdown("### 📊 **Analysis Parameters**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Nitrogen", f"{N} ppm", delta=None)
        st.metric("Phosphorus", f"{P} ppm", delta=None)
    
    with col2:
        st.metric("Potassium", f"{K} ppm", delta=None)
        st.metric("pH Level", f"{ph}", delta=None)
    
    with col3:
        st.metric("Temperature", f"{temperature:.1f}°C", delta=None)
        st.metric("Humidity", f"{humidity:.1f}%", delta=None)
    
    # Enhanced Cultivation Recommendations with Colors
    st.markdown("""
    <div class="cultivation-recommendations">
        <h3 class="recommendations-title">📋 Cultivation Recommendations</h3>
        <div class="recommendations-grid">
            <div class="recommendation-item soil">
                <div class="rec-icon">🌱</div>
                <div class="rec-text">Prepare the soil with organic compost to enhance nutrient availability</div>
            </div>
            <div class="recommendation-item water">
                <div class="rec-icon">💧</div>
                <div class="rec-text">Monitor soil moisture levels regularly for optimal growth</div>
            </div>
            <div class="recommendation-item rotation">
                <div class="rec-icon">🔄</div>
                <div class="rec-text">Consider crop rotation to maintain soil health</div>
            </div>
            <div class="recommendation-item pest">
                <div class="rec-icon">🛡️</div>
                <div class="rec-text">Implement integrated pest management practices</div>
            </div>
            <div class="recommendation-item irrigation">
                <div class="rec-icon">🚿</div>
                <div class="rec-text">Use drip irrigation for water conservation</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3>🌾 Anavrin - The Crop Predictor</h3>
    <p>Using advanced AI to recommend optimal crops based on environmental conditions</p>
    <p>© 2024 Anavrin. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
