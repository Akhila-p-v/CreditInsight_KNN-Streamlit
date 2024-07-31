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

1.ID: Unique record identifier.

2.Customer_ID: Unique identifier for each customer.

3.Month: Reporting month.

4.Name: Customer's name.

5.Age: Customer's age.

6.SSN: Customer's Social Security Number.

7.Occupation: Customer's occupation.

8.Annual_Income: Yearly income.

9.Monthly_Inhand_Salary: Monthly take-home salary.

10.Num_Bank_Accounts: Number of bank accounts.

11.Num_Credit_Card: Number of credit cards.

12.Interest_Rate: Applicable interest rate.

13.Num_of_Loan: Number of loans.

14.Type_of_Loan: Types of loans held.

15.Delay_from_due_date: Average days payments are delayed.

16.Num_of_Delayed_Payment: Count of delayed payments.

17.Changed_Credit_Limit: Change in credit limit.

18.Num_Credit_Inquiries: Number of credit inquiries.

19.Credit_Mix: Variety of credit accounts.

20.Outstanding_Debt: Total debt owed.

21.Credit_Utilization_Ratio: Ratio of credit used to credit available.

22.Credit_History_Age: Age of credit history (months).

23.Payment_of_Min_Amount: Indicates if only minimum payments are made.

24.Total_EMI_per_month: Total monthly EMI payments.

25.Amount_invested_monthly: Monthly investments.

26.Payment_Behaviour: Spending and payment patterns.

27.Monthly_Balance: End-of-month balance.

28.Credit_Score: Credit score category (Good, Standard, Poor).


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
