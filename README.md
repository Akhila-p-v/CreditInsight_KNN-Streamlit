# CreditScoreInsight:A Credit Score Classification Model

# Introduction

 In the global finance industry, accurately assessing an individual's creditworthiness is a critical process that influences loan approvals, interest rates, and overall risk management. Traditionally, credit score evaluation has been a manual and time-consuming task, prone to human error and inefficiencies. With the vast accumulation of banking details and credit-related data, there is an opportunity to enhance this process through automation.
<div align="center">
  <img src="https://github.com/Akhila-p-v/Credit_Insight/blob/main/creditgif.gif" alt="Animated GIF" width="800" height="500">
</div>

# Problem Statement

The objective of this project is to develop an intelligent, machine learning-based system that automates the categorization of individuals into three distinct creditworthiness levels: Good, Standard, and Poor. This system aims to streamline the credit assessment process, improve accuracy, and provide financial institutions with a reliable tool for making informed decisions about loan approvals and risk assessment.


# Dataset Profiling

This dataset contains information on 100,000 customers' financial and credit activities. It includes 28 attributes .

a.Columns

ID: Unique record identifier.

Customer_ID: Unique identifier for each customer.

Month: Reporting month.

Name: Customer's name.

Age: Customer's age.

SSN: Customer's Social Security Number.

Occupation: Customer's occupation.

Annual_Income: Yearly income.

Monthly_Inhand_Salary: Monthly take-home salary.

Num_Bank_Accounts: Number of bank accounts.

Num_Credit_Card: Number of credit cards.

Interest_Rate: Applicable interest rate.

Num_of_Loan: Number of loans.

Type_of_Loan: Types of loans held.

Delay_from_due_date: Average days payments are delayed.

Num_of_Delayed_Payment: Count of delayed payments.

Changed_Credit_Limit: Change in credit limit.

Num_Credit_Inquiries: Number of credit inquiries.

Credit_Mix: Variety of credit accounts.

Outstanding_Debt: Total debt owed.

Credit_Utilization_Ratio: Ratio of credit used to credit available.

Credit_History_Age: Age of credit history (months).

Payment_of_Min_Amount: Indicates if only minimum payments are made.

Total_EMI_per_month: Total monthly EMI payments.

Amount_invested_monthly: Monthly investments.

Payment_Behaviour: Spending and payment patterns.

Monthly_Balance: End-of-month balance.

Credit_Score: Credit score category (Good, Standard, Poor).

b.Types of column

ID,Customer_ID, 'SSN','Name' -These are unique identifiers.

Discrete Columns: These columns represent distinct, countable values. 'ID', 'Customer_ID', 'Month'

Continuous Columns: These columns represent measurable quantities and can take on any value within a range. 'Age', 'SSN', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Credit_History_Age', 'Total_EMI_per_month', 'Amount_invested_monthly', 'Monthly_Balance'

Categorical Columns: These columns represent categories or groups and are typically non-numeric. Name, Occupation, Type_of_Loan, Credit_Mix, Payment_of_Min_Amount, Payment_Behaviour, Credit_Score

# Streamlit Application

Deploying a machine learning model in Streamlit is a straightforward process. Streamlit is a Python library that allows you to create interactive web applications for data science and machine learning projects. A Streamlit web application was developed to host the trained machine learning model. The application provides users with a user-friendly interface to input  features and receive predictions for credit score categories. The design emphasizes simplicity and interactivity.

•	Begin by installing Streamlit using pip.

•	Imported the necessary libraries such as pandas, NumPy, scikit-learn and pickle along with Streamlit.

•	Defined the layout of the application.

•	Added widgets for user input. Users can input 10features related to Credit score like
   'Outstanding_Debt', 
    'Interest_Rate', 
    'Credit_History_Age', 
    'Changed_Credit_Limit', 
    'Delay_from_due_date', 
    'Monthly_Balance', 
    'Credit_Utilization_Ratio', 
    'Num_of_Delayed_Payment', 
    'Annual_Income', 
    'Total_EMI_per_month'.

•	Loaded the pre-trained KNN t model into memory.

•	Performed predictions based on user input.

•	Presented the prediction to the user.

•	Once the app runned locally, deployed it to Streamlit Sharing.



Hosted Website:https://creditinsightknn-app-ayrg4k5spnr6byaytqwems.streamlit.app/ 


# Screenshots

![Good Prediction](https://github.com/Akhila-p-v/Credit_Insight/blob/main/good.png)
*Good:"The credit score is predicted to be **Good**!"* 

![Standard Prediction](https://github.com/Akhila-p-v/Credit_Insight/blob/main/standard.png)
*Standard:"The credit score is predicted to be **Standard**!"*

![Poor Prediction](https://github.com/Akhila-p-v/Credit_Insight/blob/main/poor.png)
*Poor: "The credit score is predicted to be **Poor**!"* .
