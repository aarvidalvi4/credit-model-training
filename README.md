# 💳 Credit Risk Prediction using Machine Learning

## Project Overview

This project is a **Credit Risk Prediction System** built using Machine Learning techniques. The goal is to predict whether a loan applicant is likely to default based on their financial and personal information.

The project includes a trained ML model and a deployed **Streamlit web application** that allows users to input details and get real-time predictions.

---

## Live Demo

Try the deployed application here:
👉 https://credit-model-training-rce3vxxhyg8d7k3g7dq3sm.streamlit.app/

---

## Problem Statement

Financial institutions face risk when approving loans. This project helps in automating credit risk assessment using historical data and machine learning models.

---

## Machine Learning Approach

### Steps followed:

* Data preprocessing and cleaning
* Handling missing values
* Feature selection and engineering
* Model training
* Model evaluation

### Algorithms used:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier (final model)

---

## Model Evaluation

The model was evaluated using:

* Accuracy Score
* Precision & Recall
* Confusion Matrix

Final model was selected based on best performance on validation data.

---

## Tech Stack

* Python 
* Pandas & NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit (for deployment)
* Jupyter Notebook

---

## Project Structure

```
credit-model-training/
│── app.py                  # Streamlit web app
│── credit_model.ipynb      # Model training notebook
│── model.pkl               # Trained ML model
│── scaler.pkl             # Feature scaler
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```

---

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/aarvidalvi4/credit-model-training.git
```

2. Navigate to the project folder:

```bash
cd credit-model-training
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Streamlit app:

```bash
streamlit run app.py
```

---

## Key Features
* Real-time credit risk prediction
* Simple and interactive UI using Streamlit
* End-to-end ML pipeline
* Ready-to-deploy project

---

## Future Improvements
* Improve model accuracy using advanced algorithms (XGBoost / LightGBM)
* Add explainable AI (SHAP values)
* Improve UI design
* Add database integration for storing predictions

---

## Author:
Aarvi Amol Dalvi--
Machine Learning Enthusiast--
BSc First year (Computing)


## If you like this project
Give the repository a ⭐ on GitHub!
