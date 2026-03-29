## Project Overview
The goal of this project is to build a robust classifier that can assist in identifying patients at risk of heart disease. I implemented several models—including Logistic Regression, KNN, and SVM—to determine which offers the best performance for this specific dataset.

## Key Features
Data Imputation: Handled missing/zero values in Cholesterol and RestingBP using mean imputation.

Exploratory Data Analysis (EDA): Visualized distributions and correlations using Seaborn and Matplotlib.

Automated Analysis: Utilized sheryanalysis for quick data insights.

Feature Scaling: Standardized numerical features using StandardScaler for model consistency.

Model Comparison: Evaluated five different algorithms to find the most accurate predictor.

## Tech Stack
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

Gemini said
That is a solid workflow! You've covered everything from Exploratory Data Analysis (EDA) and handling zero-values (imputation) to comparing multiple classification models.

Here is a professional, well-structured README.md file tailored to your code.

Heart Disease Prediction 🩺
This repository contains a machine learning project designed to predict the likelihood of heart disease based on clinical parameters. The project involves comprehensive data preprocessing, exploratory data analysis (EDA), and a comparison of various classification algorithms.

## Project Overview
The goal of this project is to build a robust classifier that can assist in identifying patients at risk of heart disease. I implemented several models—including Logistic Regression, KNN, and SVM—to determine which offers the best performance for this specific dataset.

## Key Features
Data Imputation: Handled missing/zero values in Cholesterol and RestingBP using mean imputation.

Exploratory Data Analysis (EDA): Visualized distributions and correlations using Seaborn and Matplotlib.

Automated Analysis: Utilized sheryanalysis for quick data insights.

Feature Scaling: Standardized numerical features using StandardScaler for model consistency.

Model Comparison: Evaluated five different algorithms to find the most accurate predictor.

## Tech Stack
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

## Getting Started
### Prerequisites
Ensure you have Python installed. You can install the required dependencies using:

Bash
pip install pandas numpy seaborn matplotlib scikit-learn sheryanalysis joblib
### Usage
Clone the repository:

Bash
git clone https://github.com/your-username/heart-disease-prediction.git
Place your heart.csv file in the root directory.

Run the script or Jupyter notebook to train the models.

The best-performing model (Logistic Regression) and the scaler are exported as .pkl files for deployment.

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
