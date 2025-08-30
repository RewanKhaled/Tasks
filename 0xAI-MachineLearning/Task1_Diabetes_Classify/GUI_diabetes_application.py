import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
import pandas as pd
import os

# Load Decision Tree model
base_dir = os.path.dirname(os.path.abspath(__file__))
dt_folder = os.path.join(base_dir, "Decision tree")
model = joblib.load(os.path.join(dt_folder, "DecisionTree_model.pkl"))
feature_columns = model.feature_names_in_  # Feature names from the model

# GUI App
root = tk.Tk()
root.title("Diabetes Classifier - Decision Tree")
root.geometry("480x650")
root.resizable(False, False)

# Input fields
fields = [
    "Age",
    "Gender (Female=1, Male=0)",
    "BMI",
    "HbA1c Level",
    "Blood Glucose Level",
    "Hypertension (0/1)",
    "Heart Disease (0/1)",
    "Smoking History (0-4)"
]

entries = {}
for i, field in enumerate(fields):
    label = tk.Label(root, text=field, font=("Arial", 10))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[field] = entry

# Prediction function
def predict():
    try:
        input_data = np.array([float(entries[f].get()) for f in fields]).reshape(1, -1) # Collect user input
        x_df = pd.DataFrame(input_data, columns=feature_columns)
        pred_class = model.predict(x_df)[0]  # 0 or 1
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(x_df)[0]  # [prob_no, prob_yes]

            # Determine risk level
            if proba[1] < 0.4:
                risk = "Low risk"
            elif proba[1] < 0.7:
                risk = "Medium risk"
            else:
                risk = "High risk"

            # Class imbalance warning
            if proba[0] == 0.0 or proba[1] == 0.0:
                warning_msg = (
                    "⚠️ Warning: The model may be biased due to class imbalance.\n"
                    "Predictions may always return the same result regardless of input."
                )
                messagebox.showwarning("Class Imbalance Warning", warning_msg)
                print(warning_msg)

            # Show prediction result
            messagebox.showinfo(
                "Prediction Result",
                f"Diabetes Prediction: {'Yes' if pred_class == 1 else 'No'}\n\n"
                f"Probability No Diabetes: {proba[0]:.4f}\n"
                f"Probability Diabetes: {proba[1]:.4f}\n"
                f"Risk Level: {risk}"
            )
            print("Input:", input_data)
            print("Prediction:", pred_class)
            print("Probabilities:", proba)
            print("Risk Level:", risk)
        else:
            # If predict_proba is not available
            messagebox.showinfo(
                "Prediction Result",
                f"Diabetes Prediction: {'Yes' if pred_class == 1 else 'No'}"
            )
            print("Input:", input_data)
            print("Prediction:", pred_class)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or error:\n{e}")

# Predict Button
predict_btn = tk.Button(root, text="Predict", command=predict, bg="pink", fg="black", font=("Arial", 12))
predict_btn.grid(row=len(fields), column=0, columnspan=2, pady=20)
root.mainloop()
