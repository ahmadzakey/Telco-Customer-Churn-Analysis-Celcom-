# Streamcode.py
import streamlit as st
import pandas as pd
import numpy as np

st.title('Telco Customer Churn Analysis')
st.header('Welcome to the customer churn prediction app!')


a = st.slider('Field 1:', min_value=1, max_value=100, step=1)
b = st.slider('Field 2:', min_value=1, max_value=100, step=1)
c = st.slider('Field 3:', min_value=1, max_value=100, step=1)
d = st.slider('Field 4:', min_value=1, max_value=100, step=1)
e = st.slider('Field 5:', min_value=1, max_value=100, step=1)

st.write("Field 1:", a)
st.write("Field 2:", b)
st.write("Field 3:", c)
st.write("Field 4:", d)
st.write("Field 5:", e)

btn = st.button('Predict')
if btn:
    st.text('Button clicked!')




import pandas as pd


# Correct file path with the actual file name
data = r"C:\Users\User\Desktop\DATA SCIENCE CLASS\Class\Technical class\Self learn\Project\Supervised\Telco Customer Churn Analysis (Celcom)\Data\WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Read the CSV file
df = pd.read_csv(data)

# Display the first few rows of the DataFrame
st.dataframe(df.head())



df_final = df.copy()
selected_features1 = ['Contract', 'tenure', 'MonthlyCharges', 'OnlineSecurity', 'TotalCharges', 'TechSupport', 'Churn']
df_filtered1 = df_final[selected_features1]
st.dataframe(df_filtered1.head())

