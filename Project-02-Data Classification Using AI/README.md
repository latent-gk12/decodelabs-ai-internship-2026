# 📊 Project 02: Data Classification Using AI

> A Machine Learning classification project developed as part of the **DecodeLabs Artificial Intelligence Internship 2026**.

---

# 📌 Project Overview

This project focuses on building a complete Machine Learning classification pipeline using a structured e-commerce dataset.

The workflow covers every major stage of a supervised learning project, including:

- Data Understanding
- Data Preprocessing
- Feature Engineering
- Train-Test Split
- Model Training
- Model Evaluation
- Model Comparison
- Model Saving

---

# 🎯 Problem Statement

The objective of this project is to build a Machine Learning classification model capable of predicting the **Order Status** of an e-commerce order using historical order information.

The project demonstrates the complete workflow of a supervised classification task.

---

# 📂 Dataset Information

- Dataset Type: CSV
- Domain: E-Commerce
- Total Records: **1200**
- Total Features: **14**
- Target Variable: **OrderStatus**

Target Classes:

- Cancelled
- Delivered
- Pending
- Returned
- Shipped

---

# 🛠 Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib

---

# 📁 Project Structure

```
Project-02-Data-Classification/
│
├── data/
│   └── Dataset for Data Analytics - Sheet1.csv
│
├── notebooks/
│   └── Data_Understanding.ipynb
│
├── models/
│   └── logistic_regression_model.pkl
│
├── outputs/
│
├── PROJECT_BLUEPRINT.md
├── README.md
└── requirements.txt
```

---

# 🔄 Machine Learning Workflow

```
Dataset
    │
    ▼
Data Understanding
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Train-Test Split
    │
    ▼
Model Training
    │
    ▼
Prediction
    │
    ▼
Model Evaluation
    │
    ▼
Model Comparison
    │
    ▼
Save Model
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed identifier columns:
  - OrderID
  - CustomerID
  - TrackingNumber

- Handled missing values in the CouponCode column.

- Converted the Date column into datetime format.

- Extracted:
  - Year
  - Month
  - Day
  - DayOfWeek

- Removed the original Date column.

---

# ⚙ Feature Engineering

- Removed high-cardinality features that were not suitable for this project.
- Encoded categorical variables.
- Separated Features (X) and Target (y).
- Prepared the dataset for Machine Learning.

---

# 🤖 Machine Learning Models

The following classification models were implemented:

- Random Forest Classifier
- Decision Tree Classifier
- Logistic Regression

---

# 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Random Forest | 17.50% |
| Decision Tree | 17.08% |
| Logistic Regression | 19.17% |

---

# 📋 Observations

- The complete Machine Learning pipeline was successfully implemented.
- Multiple classification algorithms were evaluated.
- All models achieved similar accuracy.
- The dataset appears to contain limited predictive information for accurately classifying the target variable.

---

# 💾 Model Export

The best-performing model was saved using Joblib.

```
models/logistic_regression_model.pkl
```

---

# 🚀 How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Move into the project

```bash
cd Project-02-Data-Classification
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Open the notebook

Run:

```
notebooks/Data_Understanding.ipynb
```

---

# 📚 Learning Outcomes

Through this project, the following concepts were practiced:

- Data Exploration
- Data Cleaning
- Feature Engineering
- Label Encoding
- Train-Test Split
- Classification Models
- Model Evaluation
- Model Serialization

---

# 🔮 Future Improvements

- Apply One-Hot Encoding for categorical features.
- Perform Hyperparameter Tuning.
- Experiment with additional classification algorithms.
- Deploy the trained model using Streamlit or FastAPI.
- Train on a real-world dataset with stronger predictive relationships.

---

# 👨‍💻 Author

**Garvit Sharma**

Artificial Intelligence Intern

DecodeLabs AI Internship 2026

---