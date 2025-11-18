import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib # Used for saving/loading scikit-learn models

print("\n--- STEP 1: Loading Dataset ---")
file_name = 'heart_statlog_cleveland_hungary_final.csv'
try:
    df = pd.read_csv(file_name)
    print(f"Successfully loaded '{file_name}'.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    print("Please make sure the file is in the correct directory and try again.")
    raise

print("\n--- STEP 2: Handling Missing Values ---")
print("Checking for missing values...")
total_missing = df.isnull().sum().sum()
if total_missing > 0:
    initial_rows = df.shape[0]
    df.dropna(inplace=True) 
    final_rows = df.shape[0]
    print(f"Dropped {initial_rows - final_rows} rows that contained missing values.")
else:
    print("No missing values found.")

print("\n--- STEP 3: Separating features (X) and target (y) ---")
if 'target' not in df.columns:
    print("Error: 'target' column not found! Aborting.")
else:
    X = df.drop('target', axis=1)
    y = df['target']
    print("Features (X) and target (y) separated successfully.")
    print(f"X (features) shape: {X.shape}")
    print(f"y (target) shape: {y.shape}")

    # Save feature names for the web app
    feature_names = list(X.columns)
    joblib.dump(feature_names, 'feature_names.joblib')
    print("Saved feature names.")

print("\n--- STEP 4: Standardizing features (X) ---")
# We initialize the scaler that we will save
scaler = StandardScaler()

# We fit and transform the *entire* dataset X
# The web app will use this fitted scaler to transform new user input
X_scaled = scaler.fit_transform(X)
print("Features standardized.")

print("\n--- STEP 5: Training Random Forest model ---")
print("Initializing the RandomForestClassifier model...")
# We train the final model on ALL available data for best performance
model = RandomForestClassifier(random_state=42)

print("Training the model on the *full* dataset...")
model.fit(X_scaled, y)
print("Model training complete.")

print("\n--- STEP 6: Saving Model and Scaler ---")
# Save the trained model
joblib.dump(model, 'model.joblib')
# Save the fitted scaler
joblib.dump(scaler, 'scaler.joblib')

print("Model and Scaler have been saved successfully as 'model.joblib' and 'scaler.joblib'")