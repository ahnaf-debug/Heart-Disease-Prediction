import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and expected columns
model = joblib.load("D:/ML projects/Heart Disease/Model/logistic_heart.pkl")
scaler = joblib.load("D:/ML projects/Heart Disease/Model/scaler.pkl")
expected_columns = joblib.load("D:/ML projects/Heart Disease/Model/columns.pkl")

st.title("Heart Stroke Prediction")
st.markdown("Provide the following details to check your heart stroke risk:")

# Collect user input
st.title("Heart Disease Risk Predictor")
st.markdown("Fill in your details in simple terms:")

# User-friendly mappings
sex_map = {"Male": "M", "Female": "F"}
chest_pain_map = {
    "Typical Angina (chest pain during activity)": "TA",
    "Atypical Angina (mild or unusual chest pain)": "ATA",
    "Non-Anginal Pain (not related to heart)": "NAP",
    "No Chest Pain": "ASY"
}
resting_ecg_map = {
    "Normal": "Normal",
    "ST Abnormality": "ST",
    "Left Ventricular Hypertrophy": "LVH"
}
exercise_angina_map = {
    "Yes (pain during exercise)": "Y",
    "No": "N"
}
st_slope_map = {
    "Upward (normal)": "Up",
    "Flat (moderate risk)": "Flat",
    "Downward (high risk)": "Down"
}

# Collect user input 
age = age = st.slider("Age", 18, 100, 40, help="Your current age in years")

sex = st.selectbox("Gender", list(sex_map.keys()))
sex = sex_map[sex]

chest_pain = st.selectbox("Chest Pain Type", list(chest_pain_map.keys()))
chest_pain = chest_pain_map[chest_pain]

resting_bp = st.number_input("Blood Pressure (mm Hg)", 80, 200, 120)

cholesterol = st.number_input("Cholesterol Level (mg/dL)", 100, 600, 200)

fasting_bs_option = st.selectbox(
    "High Blood Sugar (Fasting > 120 mg/dL)?",
    ["No", "Yes"]
)

fasting_bs = 1 if fasting_bs_option == "Yes" else 0
resting_ecg = st.selectbox("ECG Result", list(resting_ecg_map.keys()))
resting_ecg = resting_ecg_map[resting_ecg]

max_hr = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)

exercise_angina = st.selectbox("Chest Pain During Exercise?", list(exercise_angina_map.keys()))
exercise_angina = exercise_angina_map[exercise_angina]

oldpeak = st.slider(
    "ST Depression (Heart Stress Level)",
    0.0, 6.0, 1.0,
    help="Higher value may indicate more stress on the heart"
)

st_slope = st.selectbox("Heart Test Result (ST Slope)", list(st_slope_map.keys()))
st_slope = st_slope_map[st_slope]

# When Predict is clicked
if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")