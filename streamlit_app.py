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
