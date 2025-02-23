#!/usr/bin/env python3
import pandas as pd
import numpy as np
import argparse
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler      
from sklearn.linear_model import LogisticRegression  

def main():
    # Load the dataset (update the file path if necessary)
    data = pd.read_csv("framingham.csv.xls")
    
    # Drop rows with missing values
    data = data.dropna()
    
    # Separate features and target
    # Features: all columns except 'TenYearCHD'
    X = data.drop(columns=["TenYearCHD"])
    y = data["TenYearCHD"]
    
    # Split data (using only the training set for model fitting)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    
    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)
    
    # List of features to be provided via command-line arguments
    features = [
        "male", "age", "education", "currentSmoker", "cigsPerDay",
        "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes",
        "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"
    ]
    
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Predict 10-Year CHD risk: prints 'yes' if risk is detected (prediction=1), otherwise 'no'."
    )
    for feature in features:
        parser.add_argument(f"--{feature}", type=float, required=True, help=f"Input value for {feature}")
    args = parser.parse_args()
    
    # Build the input vector in the correct order
    input_vector = np.array([getattr(args, feature) for feature in features]).reshape(1, -1)
    
    # Scale the input vector using the same scaler fitted on the training data
    input_scaled = scaler.transform(input_vector)
    
    # Make the prediction
    prediction = model.predict(input_scaled)[0]
    
    # Print "yes" if prediction is 1, otherwise print "no"
    print("yes" if prediction == 1 else "no")

if __name__ == "__main__":
    main()
