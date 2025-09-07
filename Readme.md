# 🌾 Anavrin - AI Crop Recommendation System

## 🎯 **About The Project**

**Anavrin** is an intelligent crop recommendation system that leverages machine learning to help farmers make data-driven decisions about crop selection. By analyzing soil composition, environmental factors, and weather conditions, the system provides personalized crop recommendations with confidence scores to optimize agricultural productivity.

### **🌟 Key Highlights**
- 🤖 **AI-Powered Predictions** using Random Forest & SVM algorithms
- 📊 **Interactive Dashboard** with real-time parameter adjustment
- 🎨 **Modern UI Design** with responsive layout and gradient themes
- ⚡ **Instant Results** with 85%+ accuracy confidence scores
- 📱 **Mobile-Friendly** interface for field use

---





---

## ✨ **Features**

### 🔬 **Core Functionality**
- **Soil Analysis**: N-P-K nutrient level assessment
- **Climate Integration**: Temperature, humidity, and rainfall analysis  
- **pH Optimization**: Soil acidity/alkalinity recommendations
- **Multi-Crop Support**: 22+ crop varieties including cereals, legumes, and cash crops
- **Confidence Scoring**: ML model reliability indicators

### 🎨 **User Experience**  
- **Intuitive Sliders**: Easy parameter input with helpful tooltips
- **Real-time Updates**: Instant predictions as you adjust parameters
- **Visual Results**: Beautiful gradient cards with crop icons
- **Cultivation Tips**: Actionable farming recommendations
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile

### 🛠️ **Technical Features**
- **Fast Processing**: Sub-second prediction times
- **Scalable Architecture**: Cloud-ready deployment
- **Data Validation**: Input sanitization and error handling
- **Performance Monitoring**: Built-in analytics and logging

---

## 🚀 **Tech Stack**

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Frontend** | Streamlit, HTML5, CSS3, JavaScript |
| **Backend** | Python 3.8+, Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Random Forest, SVM |
| **Deployment** | Streamlit Community Cloud, Docker |
| **Version Control** | Git, GitHub |
| **Data Processing** | Pandas, NumPy, Matplotlib |

</div>

---

## 📊 **Dataset Information**

- **Source**: [Kaggle Crop Recommendation Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)
- **Size**: 2,200+ records across 22 crop types
- **Features**: 7 environmental parameters (N, P, K, temperature, humidity, pH, rainfall)
- **Accuracy**: 95%+ on test data with Random Forest classifier

---

## 🔧 **Installation & Setup**

### **Prerequisites**
- Python 3.8 or higher
- pip package manager
- Git (optional)

### **Local Development**

1. **Clone the repository**
git clone https://github.com/Anshmaan29/anavrin-crop-predictor.git cd anavrin-crop-predictor

2. **Create virtual environment**
python -m venv crop_env source crop_env/bin/activate  # On Windows: crop_env\Scripts\activate


3. **Install dependencies**
pip install -r requirements.txt


4. **Run the application**
streamlit run app.py


5. **Open browser and navigate to** `http://localhost:8501`

---

## 📖 **Usage Guide**

### **Step 1: Input Parameters**
- Adjust **Nitrogen (N)** content using the slider (0-140 ppm)
- Set **Phosphorus (P)** levels (5-145 ppm)  
- Configure **Potassium (K)** amounts (5-205 ppm)
- Input **soil pH** value (0-14 scale)
- Set **temperature** in Celsius (-10°C to 50°C)
- Adjust **humidity** percentage (0-100%)
- Input **rainfall** data in mm (0-500mm)

### **Step 2: Get Recommendations**
- Click the **"🚀 ANALYZE & PREDICT"** button
- View your recommended crop with confidence score
- Read detailed cultivation recommendations
- Check expected yield and growing season info

### **Step 3: Implement Suggestions**
- Follow the provided cultivation tips
- Monitor the recommended environmental conditions
- Apply suggested farming practices

---


---

## 🤖 **Model Performance**

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| **Random Forest** | **96.4%** | 95.8% | 96.2% | 96.0% |
| SVM | 94.2% | 93.7% | 94.1% | 93.9% |
| Logistic Regression | 91.8% | 90.9% | 91.2% | 91.0% |

---

## 🌐 **Live Demo**

🔗 **[View Live Application](anavrin.streamlit.app)**

Experience the full functionality of Anavrin with our deployed version. No installation required!

---

## 🤝 **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.

### **Development Setup**
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🔮 **Future Enhancements**

- [ ] 🌍 **Weather API Integration** - Real-time weather data
- [ ] 📱 **Mobile App** - Native Android/iOS application  
- [ ] 🗺️ **Location-Based Recommendations** - GPS integration
- [ ] 📈 **Yield Prediction** - Estimated crop output forecasting
- [ ] 🌱 **Multi-Season Planning** - Crop rotation suggestions
- [ ] 💰 **Market Price Integration** - Economic viability analysis
- [ ] 🌊 **Water Management** - Irrigation optimization
- [ ] 🏆 **Gamification** - Achievement system for farmers

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 **Author**

**Anshmaan Singh**
- 📧 Email: [anshmaansingh@icloud.com]


---



<div align="center">

### 🌟 **Star this repository if it helped you!**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/anavrin-crop-predictor.svg?style=social&label=Star)](https://github.com/yourusername/anavrin-crop-predictor)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/anavrin-crop-predictor.svg?style=social&label=Fork)](https://github.com/yourusername/anavrin-crop-predictor/fork)

**Made with ❤️ for farmers and agriculture enthusiasts**

</div>

