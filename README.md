# 🫀 Cardiovascular Disease Prediction System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Model-Random%20Forest-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **A Minor Project implementation for real-time heart disease risk assessment using Ensemble Learning.**

---

## 📖 Abstract
Cardiovascular diseases (CVDs) are a leading cause of mortality globally. This system leverages **Machine Learning** to predict the likelihood of heart disease in patients based on physiological data. By analyzing critical health metrics, the model provides a binary classification (Risk / No Risk), aiding in early diagnosis and informed decision-making.

## ⚙️ The Model: Random Forest Classifier
The core of this project is built upon the **Random Forest Algorithm**. We selected this ensemble method over single Decision Trees or Logistic Regression for several key reasons:

* **Ensemble Logic:** It constructs a multitude of decision trees at training time. The final output is determined by the **mode** (majority vote) of the classes of individual trees.
* **Overfitting Prevention:** By averaging multiple trees, the model reduces variance and generalizes better to unseen patient data than individual decision trees.
* **Feature Sensitivity:** It effectively handles high-dimensional data and identifies which features (e.g., Cholesterol, Chest Pain) are most indicative of disease.

## 📊 Datasets Used
To ensure the model is robust and scientifically valid, it was trained and cross-validated on two distinct, major health datasets:

1.  **UCI Machine Learning Repository:**
    * *Source:* The Cleveland Heart Disease Dataset.
    * *Key Features:* Age, Sex, Chest Pain (cp), Resting BP (trestbps), Cholesterol (chol), Fasting Blood Sugar (fbs), RestECG, etc.
2.  **IEEE DataPort Dataset:**
    * Used to supplement training data and validate performance across different demographic distributions.

## 🚀 Key Features
* **High Accuracy:** Validated via cross-validation to ensure reliability.
* **Real-Time Prediction:** Optimized for quick inference times.
* **Data Robustness:** Capable of handling missing values and outliers effectively due to the Random Forest architecture.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Scikit-Learn, Pandas, NumPy, Matplotlib/Seaborn.
* **Algorithm:** Random Forest Classifier.

---

## 👥 Contributors
This project was developed as a **Minor Project** by:

* **Shreyansh Mishra**
* **Shejal Dubey**
* **Shivansh**

### 🎓 Supervision
Under the expert guidance of:
**Prof. Vipin Tyagi**

---

## 📥 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/cardio-prediction.git](https://github.com/yourusername/cardio-prediction.git)
