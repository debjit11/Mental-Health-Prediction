# 🧠 Mental Health Risk Prediction using Digital Behavioral Data

## 📌 Project Overview

Mental health issues are increasingly linked with modern digital lifestyles. Excessive screen time, poor sleep patterns, high notification frequency, and social media overuse can significantly impact psychological well-being.

This project develops a **machine learning system that predicts mental health risk based on digital behavioral patterns**. Using behavioral features such as device usage, sleep quality, physical activity, and digital dependence, the model predicts whether a user is at **high mental health risk or low risk**.

The system also includes a **Streamlit web application** where users can input their lifestyle data and instantly receive a risk prediction.

---

## 🚀 Key Features

- 📊 Behavioral data analysis of digital lifestyle patterns
- 🤖 Machine learning prediction using **XGBoost**
- ⚖️ Handling class imbalance in the dataset
- 🧹 Data preprocessing with **OneHotEncoding and Standard Scaling**
- 🌐 Interactive **Streamlit web application** for real-time prediction
- 📈 Model evaluation using Precision, Recall, F1 Score, and ROC-AUC

---

## 🗂️ Dataset Description

The project uses a **Digital Lifestyle Benchmark Dataset** containing behavioral and demographic attributes.

### Important Features

- Age
- Gender
- Region
- Device Hours Per Day
- Phone Unlocks
- Notifications Per Day
- Social Media Usage
- Study Time
- Physical Activity
- Sleep Hours
- Sleep Quality
- Productivity Score
- Digital Dependence Score

### Target Variable

| Value | Meaning |
|-------|---------|
| 0 | Low Mental Health Risk |
| 1 | High Mental Health Risk |

**Dataset size:** 3,500 records

---

## ⚙️ Machine Learning Pipeline

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. Handling Class Imbalance
5. Model Training
6. Model Evaluation
7. Deployment with Streamlit

---

## 🧠 Model Selection

Multiple models were evaluated:

- Logistic Regression
- Random Forest
- XGBoost

**XGBoost achieved the best performance** due to its ability to capture nonlinear relationships and interactions between behavioral variables.

---

## 📊 Model Evaluation Metrics

To properly evaluate the model, multiple metrics were used:

- **Accuracy** - Overall correctness of predictions
- **Precision** - True positive rate among positive predictions
- **Recall** - True positive rate among actual positives
- **F1 Score** - Harmonic mean of precision and recall
- **ROC-AUC** - Area under the receiver operating characteristic curve

These metrics help measure the model's ability to correctly identify individuals at **high mental health risk**.

---

## 🌐 Streamlit Web Application

A simple and interactive **Streamlit interface** allows users to enter digital lifestyle information such as:

- Screen time
- Sleep duration
- Social media usage
- Phone unlock frequency
- Physical activity
- Digital dependence

The trained model then predicts:

- **Low Risk** ✅
- **High Risk** ⚠️

This demonstrates how machine learning models can be integrated into user-friendly applications for practical use.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| Scikit-learn | Machine learning utilities |
| XGBoost | Gradient boosting model |
| Streamlit | Web application framework |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |

---

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

---

## ▶️ How to Run the Project

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/debjit11/Mental-Health-Prediction.git
cd mental-health-prediction
```

#### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

---

## 📈 Future Improvements

- Add explainable AI using SHAP
- Deploy the model on cloud platforms (AWS, Google Cloud, Heroku)
- Integrate wearable health data
- Improve prediction accuracy with deep learning models
- Add real-time data collection from mobile devices
- Implement user feedback loop for continuous model improvement

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact & Support

For questions, issues, or suggestions, please open an issue on the [GitHub repository](https://github.com/debjit11/Mental-Health-Prediction) or contact the project maintainers.

---

## 🙏 Acknowledgments

- Digital Lifestyle Benchmark Dataset for providing the data
- Open-source community for the amazing tools and libraries
- Contributors and collaborators who helped improve this project

---

**Last Updated:** March 2026
