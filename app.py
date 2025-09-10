import streamlit as st
import pandas as pd
import pickle
import sklearn

# --- Page Configuration ---
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="👋",
    layout="wide"
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    /* General App Styling */
    .stApp {
        background-color: #0f172a; /* Dark Slate background */
        color: #e2e8f0; /* Default light text color */
    }

    /* Main Content Area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    /* Card-like containers */
    .stDataFrame, .stButton > button, .stInfo, .stSuccess, .stError {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: #1e293b; /* Darker slate for cards */
        border: 1px solid #334155;
    }

    /* Title Styling */
    h1 {
        color: #f8fafc; /* White */
        text-align: center;
        padding-bottom: 1rem;
    }
    
    /* Subheader Styling */
    h2, h3 {
        color: #cbd5e1; /* Lighter Gray */
    }

    /* Sidebar Styling */
    .st-emotion-cache-16txtl3 {
        background-color: #1e293b;
        padding: 1.5rem;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        border: none;
        padding: 0.75rem 0;
        margin-top: 1rem;
        background-color: #2563eb; /* Bright Blue */
        color: white;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1d4ed8; /* Darker Blue on hover */
    }

    /* Prediction Result Styling */
    .stSuccess {
        padding: 1rem;
        background-color: #064e3b; /* Darker Green */
        border: 1px solid #10b981;
    }
    .stError {
        padding: 1rem;
        background-color: #7f1d1d; /* Darker Red */
        border: 1px solid #ef4444;
    }
    
    /* Info Box */
    .stInfo {
        border-left: 5px solid #3b82f6; /* Blue accent */
        padding: 1rem;
    }
    
    /* Make sure text in dataframes is light */
    .stDataFrame * {
        color: #e2e8f0;
    }

</style>
""", unsafe_allow_html=True)


# --- Load Model ---
try:
    with open('customer_churn_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Error: 'customer_churn_model.pkl' not found. Please ensure the model file is in the same directory as the app.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()


# --- App Title and Description ---
st.title("Customer Churn Analyzer 📊")
st.markdown("<p style='text-align: center; color: #94a3b8;'>This application uses a machine learning model to predict customer churn based on their data.</p>", unsafe_allow_html=True)


# --- Sidebar for User Input ---
st.sidebar.header("Customer Input Features")

def get_user_input():
    """
    Collects user input from the sidebar and returns it as a DataFrame.
    """
    call_failure = st.sidebar.slider('Call Failures', 0, 20, 5)
    complains = st.sidebar.selectbox('Complains', [0, 1], help="0 = No, 1 = Yes")
    subscription_length = st.sidebar.slider('Subscription Length (months)', 1, 60, 24)
    charge_amount = st.sidebar.selectbox('Charge Amount Tier', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    seconds_of_use = st.sidebar.slider('Seconds of Use', 0, 20000, 5000)
    frequency_of_use = st.sidebar.slider('Frequency of Use', 0, 200, 50)
    frequency_of_sms = st.sidebar.slider('Frequency of SMS', 0, 500, 50)
    distinct_called_numbers = st.sidebar.slider('Distinct Called Numbers', 0, 100, 20)
    age_group = st.sidebar.selectbox('Age Group', [1, 2, 3, 4, 5], 3)
    tariff_plan = st.sidebar.selectbox('Tariff Plan', [1, 2], 1)
    status = st.sidebar.selectbox('Status', [1, 2], 1, help="Customer status tier")
    age = st.sidebar.slider('Age', 15, 80, 30)
    customer_value = st.sidebar.number_input('Customer Value', min_value=0.0, max_value=5000.0, value=500.0, step=50.0)

    # Create a dictionary of the input data
    input_data = {
        'Call_Failure': [call_failure],
        'Complains': [complains],
        'Subscription_Length': [subscription_length],
        'Charge_Amount': [charge_amount],
        'Seconds_of_Use': [seconds_of_use],
        'Frequency_of_use': [frequency_of_use],
        'Frequency_of_SMS': [frequency_of_sms],
        'Distinct_Called_Numbers': [distinct_called_numbers],
        'Age_Group': [age_group],
        'Tariff_Plan': [tariff_plan],
        'Status': [status],
        'Age': [age],
        'Customer_Value': [customer_value]
    }
    
    # Convert dictionary to a DataFrame
    features = pd.DataFrame(input_data)
    
    return features

# Get input from the user
user_input_df = get_user_input()

# --- Display User Input and Prediction ---
st.subheader("📝 Your Input")
st.write("Here are the customer details you've provided:")
st.dataframe(user_input_df)

# Prediction button
if st.button('Predict Churn', key='predict_button'):
    try:
        # Generate predictions
        prediction = model.predict(user_input_df)
        prediction_proba = model.predict_proba(user_input_df)

        st.subheader("🤖 Prediction Result")
        
        # Display the result
        churn_probability = prediction_proba[0][1]
        
        if prediction[0] == 1:
            st.error(f"Prediction: **Customer is likely to Churn**", icon="🚨")
        else:
            st.success(f"Prediction: **Customer is unlikely to Churn**", icon="✅")
        
        st.write(f"**Confidence Score (Churn Probability):** `{churn_probability:.2%}`")
        
        # Display probability in a progress bar for better visualization
        st.progress(churn_probability)
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# --- Instructions ---
st.info(
    """
    **How to use this app:**
    1.  Adjust the sliders and select options in the left sidebar to reflect the customer's data.
    2.  Click the "Predict Churn" button.
    3.  The app will display the churn prediction and the associated confidence score.
    """
)

