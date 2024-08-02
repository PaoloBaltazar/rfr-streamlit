import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

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


# Input Features
with st.sidebar:
  st.header('Input features')
  attendance = st.number_input('Attendance', value=None, placeholder="Insert Attendance")
  financial_situation = st.slider('Financial Situation', 1, 5, 3)
  learning_environment = st.slider('Learning Environmnet', 1, 5, 3)
  prev_grade = st.number_input('Previous Grade', value=None, placeholder="Insert Previous Grade")
  
  data = {'attendance': attendance,
          'financial_situation': financial_situation,
          'learning_environment': learning_environment,
          'prev_grade': prev_grade}
  
  input_df = pd.DataFrame(data, index=[0])
  input_penguins pd.concat([input_df, X], axis=0)

# Model Training
rfr = RandomForestRegression()
rfr.fit(


  
