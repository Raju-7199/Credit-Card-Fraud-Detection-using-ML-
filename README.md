# 💳 Credit Card Fraud Detection using SMOTE, Scaling, and Model Comparison

A machine learning project for detecting fraudulent credit card transactions using **SMOTE** for class balancing, **MinMax Scaling** for preprocessing, and a comparative evaluation of **Logistic Regression**, **Random Forest**, and **XGBoost**.

🚀 Final deployed model: **XGBoost**

---

## 📌 Project Overview

This project uses the highly imbalanced **Credit Card Fraud Detection Dataset** and builds an end-to-end fraud detection pipeline:

- Train-test split with stratification  
- SMOTE oversampling on training data  
- Feature scaling using MinMaxScaler  
- Training and comparison of three classifiers  
- Model selection and persistence  
- Streamlit web app for real-time fraud prediction

The final selected model is **XGBoost**, chosen for deployment due to strong fraud detection performance and production readiness.

---

## ✨ Features

- Fraud detection on tabular transaction data  
- Handles class imbalance using **SMOTE**
- Feature scaling with **MinMaxScaler**
- Compares:
  - Logistic Regression
  - Random Forest Classifier
  - XGBoost Classifier

### Evaluation Metrics
- Accuracy Score  
- Confusion Matrix  
- Classification Report  
- ROC AUC Score  

### Deployment
- Streamlit interactive dashboard  
- Saved model using Pickle  
- Real-time fraud prediction

---

## 📂 Project Structure

```text
.
├── app1.py
├── final1ML.ipynb
├── ML_project1.ipynb
├── Presentation-ML.pptx
├── trainedmodel.sav
├── scaler.sav
├── requirements.txt
└── README.md
```

---

# ⚙️ Workflow

1. Load `creditcard.csv`
2. Split features and target (`Class`)
3. Perform train-test split
4. Apply SMOTE only to training data
5. Scale features using MinMaxScaler
6. Train and compare models:
   - Logistic Regression
   - Random Forest
   - XGBoost
7. Select best model
8. Save trained model and scaler
9. Use saved artifacts in Streamlit for predictions

---

# 🤖 Model Experiments

## 1. Logistic Regression

**Metrics**

- Accuracy: **97.90%**
- ROC AUC: **0.9187**

### Confusion Matrix

```text
[[83524, 1771],
 [   21,  127]]
```

---

## 2. Random Forest Classifier

**Metrics**

- Accuracy: **99.36%**
- ROC AUC: **0.9158**

### Confusion Matrix

```text
[[84771, 524],
 [   24, 124]]
```

---

## 3. XGBoost (Final Model)

**Metrics**

- Accuracy: **~100%**
- ROC AUC: **0.8971**

### Confusion Matrix

```text
[[76489, 15],
 [   29,112]]
```

### Fraud Class Performance

- Precision: **0.88**
- Recall: **0.79**
- F1 Score: **0.84**

---

# 📊 Model Comparison

| Model | Accuracy | ROC AUC | Notes |
|------|---------:|--------:|------|
| Logistic Regression | 0.9790 | 0.9187 | Strong baseline |
| Random Forest | 0.9936 | 0.9158 | Excellent performance |
| XGBoost | ~1.00 | 0.8971 | Final deployed model |

---

# ✅ Why XGBoost?

XGBoost was selected as the deployment model because it offers:

- Strong fraud precision/recall
- Robust performance on imbalanced data
- Better deployment-ready pipeline
- High scalability and optimization

---

# 🌐 Streamlit Application

The project includes a fraud prediction dashboard using Streamlit.

## Features

- Loads saved model (`trainedmodel.sav`)
- Loads saved scaler (`scaler.sav`)
- Accepts:
  - `Time`
  - `V1` to `V28`
  - `Amount`

### App Functions

✔ Predicts fraud probability  
✔ Displays risk level  
✔ Demo buttons for sample transactions  
✔ Interactive UI for testing

---

# 🛠 Installation

## Clone Repository

```bash
git clone https://github.com/Raju-7199/credit-card-fraud-detection-ml.git
cd credit-card-fraud-detection-ml
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
streamlit
numpy
pandas
scikit-learn
imbalanced-learn
xgboost
pickle-mixin
```

---

## Required Files

Place these in the project directory:

- creditcard.csv
- trainedmodel.sav
- scaler.sav
- app1.py

---

## Run Streamlit App

```bash
streamlit run app1.py
```

---

# 🔍 Code Review Notes

## What Works Well

- Proper handling of imbalanced data with SMOTE
- Correct resampling only on training set
- Scaler saved with model
- Multiple models compared
- Real deployment via Streamlit app

---

## Improvements

- Add unified comparison notebook
- Add ROC curve visualizations
- Add confusion matrix plots
- Include feature importance plots
- Add `requirements.txt` version pinning

Example:

```txt
numpy==1.26.4
pandas==2.2.2
scikit-learn==1.4.2
imbalanced-learn==0.12.2
xgboost==2.0.3
streamlit==1.35.0
```

---

# 🚀 Optional Enhancements

- ROC Curves for all models
- Unified ML Pipeline
- Feature Importance Visualization
- Hyperparameter Tuning
- Cross Validation
- Streamlit deployment on Streamlit Cloud
- Docker support
- Model API with Flask/FastAPI

---

# 📷 Suggested Repository Additions

You can improve the repository by adding:

- Streamlit screenshots
- Demo GIF
- Architecture diagram
- Presentation slides
- Dataset description

---

# 📤 GitHub Upload Steps

```bash
git init
git add .
git commit -m "Initial commit - credit card fraud detection project"
git branch -M main
git remote add origin https://github.com/yourusername/credit-card-fraud-detection-ml.git
git push -u origin main
```

## 🧠 Tech Stack

- Python
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Streamlit
- Pandas
- NumPy

---

## 👨‍💻 Author
  
GitHub: https://github.com/Raju-7199

---

## 📜 License

This project is open-source under the MIT License.
