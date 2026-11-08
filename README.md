# BITS Pilani M.Tech AIML
# AIMLZG565-ML-Assignment-2
# Bits ID - 2026ak05544
# Name - Pravin Marathe

# a. Problem Statement
The objective of this assignment is to implement and compare five machine learning classification algorithms using a publicly available dataset.
The performance of the models will be evaluated using Accuracy, AUC, Precision, Recall, F1 Score and Matthews Correlation Coefficient (MCC).
An interactive Streamlit web application will be developed to evaluate the trained models on uploaded test data.

# b. Dataset Description 
Dataset Name: Bank Marketing Dataset

Source: UCI Machine Learning Repository

Dataset Link:
https://archive.ics.uci.edu/dataset/222/bank+marketing

Total Instances: 45,211
Input Features: 16
Target Variable: y
Classification Type: Binary (yes/no)

The dataset contains information about bank
marketing campaigns. The objective is to predict
whether a customer will subscribe to a term deposit.

### C. GitHub Repository Link
https://github.com/pravin-marathe/AIMLZG565-ML-Assignment-2

### d. Model Performance Comparison
The following table compares five machine learning classification models using Accuracy, AUC, Precision, Recall, F1 Score and MCC.
| Model | Accuracy | AUC | Precision | Recall | F1-score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9012 | 0.9056 | 0.6445 | 0.3478 | 0.4518 | 0.4261 |
| Decision Tree | 0.8746 | 0.7015 | 0.4649 | 0.4754 | 0.4701 | 0.3990 |
| KNN | 0.8962 | 0.8277 | 0.5990 | 0.3403 | 0.4339 | 0.4261 |
| Naive Bayes | 0.8548 | 0.8101 | 0.4059 | 0.5198 | 0.4559 | 0.3774 |
| SVM | 0.9001 | 0.9072 | 0.6605 | 0.3015 | 0.4140 | 0.4016 |

### Observations
- Logistic Regression achieved the highest accuracy (90.12%).
- SVM achieved the highest AUC (0.9072) and precision (0.6605).
- Naive Bayes achieved the highest recall (0.5198).
- Logistic Regression achieved the highest F1-score.
- The complete performance results are available in model_comparison.csv.

