import streamlit as st
import pandas as pd
import joblib

# Load the saved model, scaler, and feature names
try:
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib')
    feature_names = joblib.load('feature_names.joblib')
except FileNotFoundError:
    st.error("Model or scaler files not found. Please run 'train_and_save.py' first.")
    st.stop()
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# Set up the Streamlit page
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")
st.title('❤️ Heart Disease Prediction')
st.write("Enter the patient's details below to predict the likelihood of heart disease.")

# Create a sidebar for inputs
st.sidebar.header('Patient Input Features')

# Function to collect user inputs
def get_user_input():
    # Use a dictionary to store inputs
    inputs = {}

    # Based on the features in your dataset
    # NOTICE THE KEYS (e.g., 'chest pain type') NOW MATCH YOUR CSV
    
    inputs['age'] = st.sidebar.slider('Age', 20, 100, 50)
    
    inputs['sex'] = st.sidebar.selectbox('Sex', (0, 1), format_func=lambda x: 'Female' if x == 0 else 'Male')
    
    # CHANGED: 'cp' is now 'chest pain type'
    inputs['chest pain type'] = st.sidebar.selectbox('Chest Pain Type (cp)', (0, 1, 2, 3), 
                                        help="0=typical angina, 1=atypical angina, 2=non-anginal pain, 3=asymptomatic")
    
    # CHANGED: 'trestbps' is now 'resting bp s'
    inputs['resting bp s'] = st.sidebar.slider('Resting Blood Pressure (trestbps)', 90, 200, 120)
    
    # CHANGED: 'chol' is now 'cholesterol'
    inputs['cholesterol'] = st.sidebar.slider('Serum Cholesterol (chol)', 100, 600, 200)
    
    # CHANGED: 'fbs' is now 'fasting blood sugar'
    inputs['fasting blood sugar'] = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', (0, 1), 
                                         format_func=lambda x: 'False' if x == 0 else 'True')
    
    # CHANGED: 'restecg' is now 'resting ecg'
    inputs['resting ecg'] = st.sidebar.selectbox('Resting ECG (restecg)', (0, 1, 2),
                                             help="0=normal, 1=ST-T wave abnormality, 2=left ventricular hypertrophy")
    
    # CHANGED: 'thalach' is now 'max heart rate'
    inputs['max heart rate'] = st.sidebar.slider('Max Heart Rate Achieved (thalach)', 70, 220, 150)
    
    # CHANGED: 'exang' is now 'exercise angina'
    inputs['exercise angina'] = st.sidebar.selectbox('Exercise Induced Angina (exang)', (0, 1),
                                          format_func=lambda x: 'No' if x == 0 else 'Yes')
    
    # 'oldpeak' was correct, so we leave it
    inputs['oldpeak'] = st.sidebar.slider('ST Depression (oldpeak)', 0.0, 6.2, 1.0, step=0.1)
    
    # CHANGED: 'slope' is now 'ST slope'
    inputs['ST slope'] = st.sidebar.selectbox('Slope of Peak Exercise ST (slope)', (0, 1, 2),
                                           help="0=upsloping, 1=flat, 2=downsloping")

    # Convert inputs to a DataFrame
    input_df = pd.DataFrame([inputs])
    
    # This line will now work, because the columns in 'input_df' 
    # (created from the keys above) will match the 'feature_names' list.
    input_df = input_df[feature_names] 
    
    return input_df

# Get input from the user
user_input_df = get_user_input()

# Display the user's input
st.subheader('Patient Input:')
st.dataframe(user_input_df)

# Create a button to make predictions
if st.button('Predict Heart Disease'):
    # 1. Scale the user input
    try:
        user_input_scaled = scaler.transform(user_input_df)
        
        # 2. Make a prediction
        prediction = model.predict(user_input_scaled)
        
        # 3. Get prediction probabilities
        prediction_proba = model.predict_proba(user_input_scaled)
        
        st.subheader('Prediction:')
        
        if prediction[0] == 1:
            st.error('**Result: Positive for Heart Disease**')
            st.write(f"The model predicts a **{prediction_proba[0][1]*100:.2f}%** probability of heart disease.")
        else:
            st.success('**Result: Negative for Heart Disease**')
            st.write(f"The model predicts a **{prediction_proba[0][0]*100:.2f}%** probability of *not* having heart disease.")
            
        st.subheader('Prediction Confidence:')
        prob_df = pd.DataFrame(
            {'Probability': prediction_proba[0]},
            index=['Negative (0)', 'Positive (1)']
        )
        st.bar_chart(prob_df)

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

st.write("---")
st.write("**Disclaimer:** This is a machine learning model and not a substitute for professional medical advice. Please consult a doctor for any health concerns.")