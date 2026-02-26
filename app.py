import streamlit as st
import pickle
import numpy as np

# Load model 
model = pickle.load(open("diamond_knn_model.pkl", "rb"))

st.set_page_config(page_title="Diamond Price Prediction", layout="centered")

st.title("💎 Diamond Price Prediction App")
st.write("Enter diamond details to predict the price.")

# ---- User Inputs ---- #

carat = st.number_input("Carat", min_value=0.1, max_value=5.0, value=0.5)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])
depth = st.number_input("Depth", min_value=40.0, max_value=80.0, value=60.0)
table = st.number_input("Table", min_value=40.0, max_value=95.0, value=55.0)
x = st.number_input("Length (x)", min_value=0.1, max_value=15.0, value=5.0)
y = st.number_input("Width (y)", min_value=0.1, max_value=15.0, value=5.0)
z = st.number_input("Depth (z)", min_value=0.1, max_value=10.0, value=3.0)

# Create Pandas DataFrame
import pandas as pd

input_data = pd.DataFrame({
    "carat": [carat],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z],
    "cut": [cut],
    "color": [color],
    "clarity": [clarity]
})

# ---- Prediction ---- #

if st.button("Predict Price"):
     
    prediction = model.predict(input_data)
    
    # If you used log transformation
    final_price = np.expm1(prediction[0])
    
    st.success(f"💰 Predicted Diamond Price: ${round(final_price, 2)}")

