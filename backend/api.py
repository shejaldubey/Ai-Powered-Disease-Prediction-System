import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS)
# This allows your React app (running on localhost:3000)
# to make requests to this server (running on localhost:5000)
CORS(app)

# --- Load Model, Scaler, and Feature Names ---
# We load these once when the server starts for efficiency
try:
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib')
    feature_names = joblib.load('feature_names.joblib')
    print("Model, scaler, and feature names loaded successfully.")
except FileNotFoundError:
    print("Error: Model or scaler files not found.")
    print("Make sure 'model.joblib', 'scaler.joblib', and 'feature_names.joblib' are in the same directory.")
    # In a real app, you'd handle this more gracefully
    model = None
    scaler = None
    feature_names = None
except Exception as e:
    print(f"Error loading files: {e}")
    model = None
    scaler = None
    feature_names = None

# --- Define the Prediction Endpoint ---
@app.route('/predict', methods=['POST'])
def predict():
    if not model or not scaler or not feature_names:
        return jsonify({'error': 'Model is not loaded properly. Check server logs.'}), 500

    try:
        # Get the JSON data from the React app's request
        data = request.json
        
        # Convert the incoming data (a dictionary) into a DataFrame
        # The [data] syntax creates a DataFrame with a single row
        input_df = pd.DataFrame([data])

        # Ensure the columns are in the *exact* order the model was trained on
        # This is a critical step
        input_df = input_df[feature_names]

        # Scale the new data using the *loaded* scaler
        input_scaled = scaler.transform(input_df)

        # Make the prediction and get probabilities
        prediction = model.predict(input_scaled)
        probabilities = model.predict_proba(input_scaled)

        # Get the probability for the predicted class
        predicted_class = int(prediction[0])
        probability = float(probabilities[0][predicted_class])
        
        # Get probabilities for both classes to send to the frontend
        prob_class_0 = float(probabilities[0][0])
        prob_class_1 = float(probabilities[0][1])

        # Create the response JSON
        response = {
            'prediction': predicted_class,
            'probability': probability,
            'probability_negative': prob_class_0,
            'probability_positive': prob_class_1
        }
        
        return jsonify(response)

    except Exception as e:
        # Log the error for debugging
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

# --- Run the Server ---
if __name__ == '__main__':
    # Runs the Flask server on http://localhost:5000
    # You can access it from any computer on your network by using host='0.0.0.0'
    app.run(port=5000, debug=True)