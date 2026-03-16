import streamlit as st
import pandas as pd
import pickle


with open("notebooks/models/mental_health_model.pkl","rb") as f:
    model = pickle.load(f)
    

st.title("Mental Health Risk Predictor")

st.write("Enter your digital lifestyle details")

age = st.number_input("Age", 10, 80)

gender = st.selectbox("Gender", ["Male", "Female"])

region = st.selectbox("Region", ["Asia", "Europe", "America"])

income = st.selectbox("Income Level", ["Low", "Medium", "High"])

education = st.selectbox("Education Level", ["School", "Graduate", "Postgraduate"])

role = st.selectbox("Daily Role", ["Student", "Worker"])

device_hours = st.number_input("Device Hours Per Day")

unlock = st.number_input("Phone Unlocks Per Day")

notifications = st.number_input("Notifications Per Day")

social = st.number_input("Social Media Minutes")

study = st.number_input("Study Minutes")

activity = st.number_input("Physical Activity Days")

sleep = st.number_input("Sleep Hours")

sleep_quality = st.number_input("Sleep Quality (1-10)")

device_type = st.selectbox("Device Type", ["Smartphone", "Laptop", "Tablet"])

productivity = st.number_input("Productivity Score")

dependence = st.number_input("Digital Dependence Score")


if st.button("Predict Risk"):

    input_data = pd.DataFrame({
        "age":[age],
        "gender":[gender],
        "region":[region],
        "income_level":[income],
        "education_level":[education],
        "daily_role":[role],
        "device_hours_per_day":[device_hours],
        "phone_unlocks":[unlock],
        "notifications_per_day":[notifications],
        "social_media_mins":[social],
        "study_mins":[study],
        "physical_activity_days":[activity],
        "sleep_hours":[sleep],
        "sleep_quality":[sleep_quality],
        "device_type":[device_type],
        "productivity_score":[productivity],
        "digital_dependence_score":[dependence]
    })

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error("High Mental Health Risk")
    else:
        st.success("Low Mental Health Risk")
        

    st.write("High Risk Probability:", round(probability[0][1]*100,2), "%")