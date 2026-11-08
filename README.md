# BITS Pilani M.Tech AIML
# AIMLZG565-ML-Assignment-2
# Bits ID - 2026ak05544
# Name - Pravin Marathe

### a. Problem Statement
The objective of this assignment is to implement and compare five machine learning classification algorithms using a publicly available dataset.
The performance of the models will be evaluated using Accuracy, AUC, Precision, Recall, F1 Score and Matthews Correlation Coefficient (MCC).
An interactive Streamlit web application will be developed to evaluate the trained models on uploaded test data.

### b. Dataset Description 
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
### Logistic Regression
- Achieved the highest accuracy (90.12%) and F1-score (0.4518) among all five models.
- Its high AUC (0.9056) indicates good class discrimination, making it a strong overall performer.

### Decision Tree
- Achieved 87.46% accuracy and an AUC of 0.7015.
- Its recall (0.4754) was higher than Logistic Regression and SVM, but its lower AUC indicates comparatively weaker class discrimination.

### K-Nearest Neighbors (KNN)
- Achieved 89.62% accuracy and an AUC of 0.8277.
- Although its accuracy was competitive, its lower recall (0.3403) indicates that many actual subscribers were not identified.

### Naive Bayes
- Achieved the highest recall (0.5198), identifying the largest proportion of actual subscribers.
- However, its lower precision (0.4059) and accuracy (85.48%) indicate a higher proportion of false-positive predictions.

### Support Vector Machine (SVM)
- Achieved the highest AUC (0.9072) and precision (0.6605), with accuracy of 90.01%.
- Its high precision indicates fewer false positives among predicted subscribers, although its recall (0.3015) was the lowest.

### Overall Conclusion
Logistic Regression is the preferred overall model based on its highest accuracy and F1-score. SVM is a strong alternative when precision and AUC are prioritized, while Naive Bayes is suitable when higher recall is important. These results demonstrate that model selection should consider multiple evaluation metrics rather than accuracy alone.

The complete performance comparison, including Accuracy, AUC, Precision, Recall, F1-score, and MCC, is provided in "model_comparison.csv".

### e. Streamlit Application

The Machine Learning classification application is deployed on Streamlit Community Cloud.

Live Application:
https://2026ak05544-ml-assignment2.streamlit.app/

The application supports:
- Selection of five trained ML models
- Uploading test data in CSV format
- Display of model evaluation metrics
- Prediction using saved models
- Downloading prediction results
