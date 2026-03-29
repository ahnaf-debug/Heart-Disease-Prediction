## Project Overview
The goal of this project is to build a robust classifier that can assist in identifying patients at risk of heart disease. I implemented several models—including Logistic Regression, KNN, and SVM—to determine which offers the best performance for this specific dataset.

## Key Features
Data Cleaning: Handled missing/zero values in Cholesterol and RestingBP using mean imputation.

Exploratory Data Analysis (EDA): Visualized distributions and correlations using Seaborn and Matplotlib.

Automated Analysis: Utilized sheryanalysis for quick data insights.

Feature Scaling: Standardized numerical features using StandardScaler for model consistency.

Model Comparison: Evaluated five different algorithms to find the most accurate predictor.

Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Joblib

Models Used:

Logistic Regression

K-Nearest Neighbors (KNN)

Gaussian Naive Bayes

Decision Tree Classifier

Support Vector Machine (SVM)

## Dataset Information
The dataset includes features such as:

Age, Sex, ChestPainType

RestingBP, Cholesterol, FastingBS

MaxHR, Oldpeak, HeartDisease (Target)

## Results
The models were evaluated based on Accuracy and F1-Score.

Model	Accuracy	F1-Score
Logistic Regression	0.85	0.87
KNN	0.83	0.85
SVM	0.86	0.88
Decision Tree	0.79	0.81
Naive Bayes	0.84	0.86
> Note: Results may vary slightly based on the random state and dataset version.		
## Model Deployment
The trained models are saved using joblib:

logistic_heart.pkl: The trained Logistic Regression model.

scaler.pkl: The StandardScaler object for preprocessing new input data.

columns.pkl: The list of feature columns used during training.

Streamlit Link: https://heart-disease-prediction-slmc4j7osmzfw6jqdfjs5h.streamlit.app/
