import streamlit as st
import pandas as pd
import joblib

st.title("AI-Based Machine Failure Prediction")
st.write("Enter machine measurements to predict possible failure.")

saved_data = joblib.load("final_machine_failure_model.pkl")
model = saved_data["model"]
threshold = saved_data["threshold"]

st.subheader("Machine Measurements")

air_temp = st.number_input("Air Temperature (K)", value=300.0)
process_temp = st.number_input("Process Temperature (K)", value=310.0)
speed = st.number_input("Rotational Speed (rpm)", value=1500)
torque = st.number_input("Torque (Nm)", value=40.0)
tool_wear = st.number_input("Tool Wear (min)", value=100)

if st.button("Predict Machine Failure"):
    inputs = pd.DataFrame([{
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear
    }])

    failure_probability = model.predict_proba(inputs)[0, 1]

    st.write(
        "Estimated failure probability:",
        f"{failure_probability * 100:.2f}%"
    )

    if failure_probability >= threshold:
        st.error("Potential machine failure detected!")
    else:
        st.success("Machine predicted to be operating normally.")
