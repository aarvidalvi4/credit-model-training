import streamlit as st
import numpy as np
import pandas as pd
import joblib


# LOAD MODEL FILES
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")


# UI
st.title("💳 Credit Risk Predictor")
st.write("Enter customer details below:")


# NUMERICAL INPUTS
age = st.number_input("Age", 18, 100, 30)
credit_amount = st.number_input("Credit Amount", 0, 100000, 20000)
duration = st.number_input("Loan Duration (months)", 1, 72, 12)
payment_ratio = st.number_input("Payment to Income Ratio", 1, 100, 30)
n_credits = st.number_input("Number of Credits", 0, 10, 1)
residence_since = st.number_input("Residence Since (years)", 1, 10, 2)


# CREATE INPUT TEMPLATE
input_df = pd.DataFrame(columns=columns)
input_df.loc[0] = 0


# FILL NUMERICAL VALUES
if "age" in columns:
    input_df.loc[0, "age"] = age

if "credit_amount" in columns:
    input_df.loc[0, "credit_amount"] = credit_amount

if "month_duration" in columns:
    input_df.loc[0, "month_duration"] = duration

if "payment_to_income_ratio" in columns:
    input_df.loc[0, "payment_to_income_ratio"] = payment_ratio

if "n_credits" in columns:
    input_df.loc[0, "n_credits"] = n_credits

if "residence_since" in columns:
    input_df.loc[0, "residence_since"] = residence_since

# Housing
housing_map = {
    "Own": "housing_own",
    "Rent": "housing_rent"
}
selected_housing = st.selectbox("Housing", list(housing_map.keys()))
input_df.loc[0, housing_map[selected_housing]] = 1

# Job
job_map = {
    "Skilled": "job_skilled employee/ official",
    "Unskilled": "job_unskilled - resident",
    "Unemployed": "job_unemployed/ unskilled - non-resident"
}
selected_job = st.selectbox("Job", list(job_map.keys()))
input_df.loc[0, job_map[selected_job]] = 1

# Purpose
purpose_map = {
    "Car New": "purpose_car (new)",
    "Car Used": "purpose_car (used)",
    "Education": "purpose_education",
    "Furniture": "purpose_furniture/equipment",
    "Others": "purpose_others"
}
selected_purpose = st.selectbox("Purpose", list(purpose_map.keys()))
input_df.loc[0, purpose_map[selected_purpose]] = 1

# Account Status
account_map = {
    "Negative Balance": "status_account_< 0 DM",
    "High Balance": "status_account_>= 200 DM",
    "No Account": "status_account_no checking account"
}
selected_account = st.selectbox("Account Status", list(account_map.keys()))
input_df.loc[0, account_map[selected_account]] = 1


# PREDICTION
if st.button("Predict Credit Risk"):

    input_scaled = scaler.transform(input_df)

    prob = model.predict_proba(input_scaled)

    st.write(input_scaled)

    if prob[0][1] > 0.4:
        st.success("✅ Likely Good Credit")
    else:
        st.error("❌ Likely Bad Credit")


    st.write(f"Probability of Good Credit: {prob[0][1]*100:.2f}%")


    st.write("FULL INPUT DATA:")
    st.write(input_df.T)


    st.write("Columns with value = 1:")
    for col in input_df.columns:
        if input_df.loc[0, col] == 1:
            st.write(col)
