import streamlit as st
import pickle
import numpy as np

# Load the KNN model from the file
with open('best_knn_model (1).pkl', 'rb') as model_file:
    loaded_knn_model = pickle.load(model_file)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background image from URL */
    .stApp {
        background-image: url("https://github.com/Akhila-p-v/Credit_Insight/blob/main/bg6.jpg?raw=true");
        background-size: cover; /* Change to cover */
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center; /* Center the image */
    }

    /* Input fields styling */
    .stNumberInput input, .stTextInput input {
        background-color: white; /* Changed to white */
        color: black;
        border-radius: 5px;
        border: 1px solid #8B4513; /* dark brown border */
        padding: 5px;
        font-size: 16px;
    }

    /* Increment buttons styling */
    .stNumberInput button {
        background-color: #FFD700; /* Yellow color */
        color: black;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        padding: 5px;
    }

    /* Labels styling */
    .stNumberInput label, .stTextInput label {
        color: black;
        font-size: 16px;
    }

    /* Title styling */
    .stMarkdown h1 {
        color: black;
        text-shadow: 1px 1px 2px white;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }

    /* Align text to the left */
    .stMarkdown p, .stNumberInput, .stTextInput, .stButton {
        text-align: left;
    }

    /* Align all tabs to the left and set their color */
    .stTabs [role="tablist"] {
        background-color: white; /* Tab background color */
        color: black; /* Tab text color */
    }
    
    /* Tab portion color */
    .stTabs [role="tablist"] div {
        background-color: #FFD700; /* Yellow tab portion color */
    }

    /* Button styling */
    .stButton button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px 20px;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Alert box styling */
    .alert-poor {
        background-color: rgba(255, 0, 0, 0.8);
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    .alert-standard {
        background-color: rgba(255, 215, 0, 0.8);
        color: black;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    .alert-good {
        background-color: rgba(0, 128, 0, 0.8);
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Credit Score Classification")  # Title 
st.write("Enter the details:")

# Create two columns for input fields
col1, col2 = st.columns(2)

# Input fields for the specified features in two columns
with col1:
    outstanding_debt = st.number_input("Outstanding Debt", min_value=0.0, max_value=4998.070000, value=0.0, step=1.0)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=34.00000, value=15.0, step=0.1)
    credit_history_age = st.number_input("Credit History Age (Days)", min_value=0.0, max_value=404.0, value=200.0, step=1.0)  # Updated default value to be within range
    changed_credit_limit = st.number_input("Changed Credit Limit", min_value=0.0, max_value=29.980000, value=0.0, step=0.1)
    delay_from_due_date = st.number_input("Delay from Due Date (Days)", min_value=0.0, max_value=62.0, value=0.0, step=1.0)

with col2:
    monthly_balance = st.number_input("Monthly Balance", min_value=-100000.0, max_value=1183.930696, value=1000.0, step=1.0)  # Updated default value to be within range
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", min_value=0.0, max_value=50.0, value=30.0, step=0.1)
    num_of_delayed_payments = st.number_input("Number of Delayed Payments", min_value=0.0, max_value=25.0, value=0.0, step=1.0)
    annual_income = st.number_input("Annual Income", min_value=0.0, max_value=179987.280000, value=50000.0, step=100.0)
    total_emi_per_month = st.number_input("Total EMI per Month", min_value=0.0, max_value=1779.103254, value=0.0, step=1.0)

# Creating empty columns around the button for centering
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    submitted = st.button('Predict')

if submitted:
    user_features = np.array([
        outstanding_debt, 
        interest_rate, 
        credit_history_age,  # Now in days
        changed_credit_limit, 
        delay_from_due_date, 
        monthly_balance, 
        credit_utilization_ratio, 
        num_of_delayed_payments, 
        annual_income, 
        total_emi_per_month
    ]).reshape(1, -1)
    
    predicted_category = loaded_knn_model.predict(user_features)[0]
    
    # Define colors for output based on category
    if predicted_category == 'Poor':
        color_class = "alert-poor"
        message = "The credit score is predicted to be **Poor**!"
    elif predicted_category == 'Standard':
        color_class = "alert-standard"
        message = "The credit score is predicted to be **Standard**!"
    else:  # Assuming the only other option is 'Good'
        color_class = "alert-good"
        message = "The credit score is predicted to be **Good**!"

    st.markdown(
        f'<div class="{color_class}">{message}</div>',
        unsafe_allow_html=True
    )
