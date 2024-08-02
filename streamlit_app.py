import streamlit as st
import pandas as pd

st.title('Prediction of Academic Performance Level')

st.info('This app use a random forest regression')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/PaoloBaltazar/rfr-thesis/master/data_100.csv')
  df

st.write('**X**')
X = df.drop('grades', axis=1)
X

st.write('**y**')
y = df.grades
y

# Data preparation
with st.sidebar:
  st.header('Input features')
  attendance = st.number_input('Attendance', value=None, placeholder="Insert Attendance")
  prev_grade = st.number_input('Previous Grade', value=None, placeholder="Insert Previous Grade")
  financial_situation = st.slider('Financial Situation', 1, 5, 3)
  learning_environment = st.slider('Learning Environmnet', 1, 5, 3)
  
