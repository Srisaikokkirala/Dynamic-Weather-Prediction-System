import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Weather Prediction System",
    layout="centered"
)

# Title
st.title(" Dynamic Weather Prediction System")
st.write("Predict **Temperature** using Humidity, Wind Speed and Pressure")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("weather_prediction_model.pkl")

model = load_model()

st.subheader("Enter Weather Details")

# Inputs
humidity = st.slider(
    "Humidity (0 - 1)",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

wind_speed = st.number_input(
    "Wind Speed (km/h)",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

pressure = st.number_input(
    "Pressure (millibars)",
    min_value=900.0,
    max_value=1100.0,
    value=1013.0
)

# Predict button
if st.button("Predict Temperature"):
    input_data = pd.DataFrame(
        [[humidity, wind_speed, pressure]],
        columns=['Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']
    )

    prediction = model.predict(input_data)

    st.success(f" Predicted Temperature: **{prediction[0]:.2f} °C**")
