app_code = '''
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import model_utils  # Required for Naive Bayes model

st.set_page_config(
    page_title="Bank Marketing ML Classifier",
    layout="wide"
)

st.title("BITS Pilani AIMLZG565 - Machine Learning Assignment 2")

st.write("**Name:** Pravin Subhash Marathe")

st.write("**BITS ID:** 2026AK05544")

st.header("Bank Marketing - ML Classification")

BASE = Path(__file__).resolve().parent

models = {
    "Logistic Regression": "logistic_regression.joblib",
    "Decision Tree": "decision_tree.joblib",
    "KNN": "knn.joblib",
    "Naive Bayes": "naive_bayes.joblib",
    "SVM": "svm.joblib"
}

@st.cache_resource
def load_model(filename):
    return joblib.load(BASE / "model" / filename)

model_name = st.selectbox("Select ML Model", list(models))
model = load_model(models[model_name])

st.subheader("Model Performance Comparison")
comparison = pd.read_csv(BASE / "model_comparison.csv")
st.dataframe(comparison, use_container_width=True)

st.subheader("Upload Test Data")
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv(BASE / "test_data.csv")

st.write("Preview of Test Data")
st.dataframe(data.head(), use_container_width=True)

X = data.drop(columns=["y"], errors="ignore")

if st.button("Predict"):
    predictions = model.predict(X)
    result = data.copy()
    result["Prediction"] = predictions
    result["Prediction Label"] = result["Prediction"].map(
        {0: "No", 1: "Yes"}
    )

    st.success("Prediction completed successfully!")
    st.dataframe(result.head(100), use_container_width=True)

 # Evaluate predictions against actual target values
    if "y" in data.columns:
            from sklearn.metrics import confusion_matrix, classification_report

            y_true = data["y"].replace({
                "no": 0, "yes": 1,
                "No": 0, "Yes": 1
            }).astype(int)

            st.subheader("Confusion Matrix")
            cm = confusion_matrix(y_true, predictions, labels=[0, 1])
            cm_df = pd.DataFrame(
                cm,
                index=["Actual No", "Actual Yes"],
                columns=["Predicted No", "Predicted Yes"]
            )
            st.dataframe(cm_df)

            st.subheader("Classification Report")
            report = classification_report(
                y_true, predictions,
                labels=[0, 1],
                target_names=["No", "Yes"],
                output_dict=True,
                zero_division=0
            )
            st.dataframe(pd.DataFrame(report).transpose())
        else:
            st.info("Evaluation requires a 'y' column in the uploaded CSV.")


    st.download_button(
        "Download Predictions",
        result.to_csv(index=False),
        file_name="predictions.csv",
        mime="text/csv"
    )
'''

with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

print("app.py created successfully!")
