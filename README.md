# Cardiovascular Disease Risk Prediction
---
## Background
Cardiovascular disease refers to any condition affecting the heart and blood vessels. The cardiovascular system, consisting of the heart and blood vessels, is responsible for pumping blood throughout the body. Cardiovascular diseases include coronary heart disease, hypertension, stroke, heart failure, and more.

Over the course of 3 months, I aim to build a predictive model with a minimum recall of 70% to classify the risk of cardiovascular disease. The model will use features such as age, gender, height, weight, blood pressure, cholesterol levels, glucose levels, smoking habits, alcohol consumption, and physical activity to assist in early detection and prevention of cardiovascular diseases.

---

## Plan to Solve the Problem
I have been recruited by a heart clinic to conduct classification analysis to detect cardiovascular disease risk among patients. The goal is to help the clinic identify high-risk patients for timely interventions. The program classifies whether a patient is at risk of cardiovascular disease or not using classification methods and patient health data.

Since recall is crucial in this context, the goal is to minimize False Negatives (FN), where a high-risk patient might be classified as low-risk. This is important as FN cases may result in patients not receiving early and appropriate treatment. Hence, maximizing recall ensures that as many high-risk patients as possible are correctly identified.

--- 

## Models to be Used
The models that will be considered for this project include:

- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Tree
- XGBoost

---

## Evaluation Metric
The primary evaluation metric for this project is Recall, as we aim to minimize the number of False Negatives. In a healthcare context, misclassifying a high-risk cardiovascular patient as low-risk could lead to serious health complications. Therefore, maximizing recall is crucial for this project.
