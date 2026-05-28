import streamlit as st
import pickle
import numpy as np

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Custom HTML Title
st.markdown("""
<h1 style='text-align: center; color: white;'>
🏠 Bengaluru House Price Prediction
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Input Section
st.markdown("## Enter House Details")

col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input("Total Square Feet", min_value=500)

with col2:
    bath = st.number_input("Bathrooms", min_value=1)

bhk = st.slider("BHK", 1, 10)

# Predict Button
if st.button("Predict Price"):

    features = np.array([[sqft, bath, bhk]])

    prediction = model.predict(features)

    st.success(f"🏡 Estimated Price: ₹ {prediction[0]:.2f} Lakhs")