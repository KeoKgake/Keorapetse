# Create Streamlit App
import streamlit as st
import pickle
import pandas as pd

# Load the saved model
pickle_in = open('best_model.sav', 'rb')
model =pickle.load(pickle_in)

# Title
st.title('Heart Disease Prediction')

# User inputs
age = st.number_input('Age')
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
trestbps = st.number_input('Resting Blood Pressure')
chol = st.number_input('Cholesterol')
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
restecg = st.selectbox('Resting ECG', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
thalach = st.number_input('Maximum Heart Rate Achieved')
exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
oldpeak = st.number_input('ST Depression Induced by Exercise')
slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3'])
thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

# Predict
if st.button('Predict'):
    # Map categorical values to numerical values
    sex = 0 if sex == 'Male' else 1
    cp = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'].index(cp)
    fbs = 1 if fbs == 'True' else 0
    restecg = ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'].index(restecg)
    exang = 1 if exang == 'Yes' else 0
    slope = ['Upsloping', 'Flat', 'Downsloping'].index(slope)
    thal = ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thal)
    
    features = pd.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.write('The patient is likely to have heart disease.')
    else:
        st.write('The patient is unlikely to have heart disease.')

