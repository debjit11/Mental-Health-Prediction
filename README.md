# 🧠 Mental Health Risk Prediction using Digital Behavioral Data

## 📌 Project Overview

Mental health issues are increasingly linked with modern digital
lifestyles. Excessive screen time, poor sleep patterns, high
notification frequency, and social media overuse can significantly
impact psychological well-being.

This project develops a **machine learning system that predicts mental
health risk based on digital behavioral patterns**. Using behavioral
features such as device usage, sleep quality, physical activity, and
digital dependence, the model predicts whether a user is at **high
mental health risk or low risk**.

The system also includes a **Streamlit web application** where users can
input their lifestyle data and instantly receive a risk prediction.

------------------------------------------------------------------------

## 🚀 Key Features

-   📊 Behavioral data analysis of digital lifestyle patterns
-   🤖 Machine learning prediction using **XGBoost**
-   ⚖ Handling class imbalance in the dataset
-   🧹 Data preprocessing with **OneHotEncoding and Standard Scaling**
-   🌐 Interactive **Streamlit web application** for real-time
    prediction
-   📈 Model evaluation using Precision, Recall, F1 Score, and ROC-AUC

------------------------------------------------------------------------

## 🗂 Dataset Description

The project uses a **Digital Lifestyle Benchmark Dataset** containing
behavioral and demographic attributes.

### Important Features

-   Age
-   Gender
-   Region
-   Device Hours Per Day
-   Phone Unlocks
-   Notifications Per Day
-   Social Media Usage
-   Study Time
-   Physical Activity
-   Sleep Hours
-   Sleep Quality
-   Productivity Score
-   Digital Dependence Score

### Target Variable

`high_risk_flag`

  Value   Meaning
  ------- -------------------------
  0       Low Mental Health Risk
  1       High Mental Health Risk

Dataset size: **3500 records**

------------------------------------------------------------------------

## ⚙ Machine Learning Pipeline

1.  Data Collection
2.  Data Cleaning and Preprocessing
3.  Feature Engineering
4.  Handling Class Imbalance
5.  Model Training
6.  Model Evaluation
7.  Deployment with Streamlit

------------------------------------------------------------------------

## 🧠 Model Selection

Multiple models were evaluated:

-   Logistic Regression
-   Random Forest
-   XGBoost

Among these, **XGBoost achieved the best performance** due to its
ability to capture nonlinear relationships and interactions between
behavioral variables.

------------------------------------------------------------------------

## 📊 Model Evaluation Metrics

To properly evaluate the model, multiple metrics were used:

-   Accuracy
-   Precision
-   Recall
-   F1 Score
-   ROC-AUC

These metrics help measure the model's ability to correctly identify
individuals at **high mental health risk**.

------------------------------------------------------------------------

## 🌐 Streamlit Web Application

A simple and interactive **Streamlit interface** allows users to enter
digital lifestyle information such as:

-   Screen time
-   Sleep duration
-   Social media usage
-   Phone unlock frequency
-   Physical activity
-   Digital dependence

The trained model then predicts:

-   **Low Risk**
-   **High Risk**
----
There are multiple ways the app might be executed depending on how `app.py` is implemented. Try these in order:

```bash


streamlit run app.py

```
<div align="center">
  <img src="https://github.com/debjit11/Mental-Health-Prediction/blob/main/img1.png" alt="Radar System UI" width="45%" />
  <img src="https://github.com/debjit11/Mental-Health-Prediction/blob/main/img2.png" alt="Missile Defense UI" width="45%" />
</div>  

---

Open the printed URL in your browser ([http://localhost:8501](http://localhost:8501) for Streamlit).

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   XGBoost
-   Streamlit
-   Matplotlib
-   Seaborn

------------------------------------------------------------------------

## 📂 Project Structure

```
mental-health-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── dataset.csv
│
├── models/
│   └── mental_health_model.pkl
│
├── notebooks/
│   └── main.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

------------------------------------------------------------------------

## ▶ How to Run the Project

### 1️⃣ Clone the repository

git clone : https://github.com/debjit11/Mental-Health-Prediction.git

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Run the Streamlit application

streamlit run app.py

The application will open in your browser.

------------------------------------------------------------------------

## 📈 Future Improvements

-   Add explainable AI using SHAP
-   Deploy the model on cloud platforms
-   Integrate wearable health data
-   Improve prediction accuracy with deep learning models

------------------------------------------------------------------------


