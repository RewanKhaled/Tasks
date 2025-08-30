# This code just for testing

import joblib
import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
dt_folder = os.path.join(base_dir, "Decision tree")
model = joblib.load(os.path.join(dt_folder, "DecisionTree_model.pkl"))
feature_columns = model.feature_names_in_

test_cases = {
    "Low risk (healthy young)": [25, 0, 22.0, 5.0, 85.0, 0, 0, 0],
    "Low risk (middle age normal)": [40, 1, 24.0, 5.4, 95.0, 0, 0, 1],
    "High risk (older, high BMI)": [65, 0, 34.0, 8.5, 180.0, 1, 1, 2],
    "High risk (diabetic profile)": [55, 1, 30.0, 9.0, 200.0, 1, 0, 3]
}

for desc, features in test_cases.items():
    x_df = pd.DataFrame([features], columns=feature_columns)
    pred = model.predict(x_df)[0]
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(x_df)[0]
        if prob[1] < 0.4:
            risk = "Low risk"
        elif prob[1] < 0.7:
            risk = "Medium risk"
        else:
            risk = "High risk"
        print(f"\n{desc}:")
        print(f"  Features: {features}")
        print(f"  Prediction: {'Diabetes YES' if pred==1 else 'No Diabetes'}")
        print(f"  Probability -> No: {prob[0]:.4f}, Yes: {prob[1]:.4f}")
        print(f"  Risk Level: {risk}")
    else:
        print(f"\n{desc}:")
        print(f"  Features: {features}")
        print(f"  Prediction: {'Diabetes YES' if pred==1 else 'No Diabetes'}")
