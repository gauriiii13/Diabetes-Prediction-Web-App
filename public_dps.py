# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:21:52 2023

@author: DELL
"""

import pickle
import streamlit as st

#loading the saved models
diabetes_model=pickle.load(open("diabetes_model.sav",'rb'))
    
#page title
st.title('Diabetes Prediction Using ML')
col1,col2,col3=st.columns(3)
with col1:
  Pregnancies=st.text_input('Number of Pregnancies',required=True)
with col2: 
  Glucose=st.text_input('Glucose Level', required=True)
with col3:
  BloodPressure=st.text_input('Blood Pressure Value', required=True)
with col1:
  SkinThickness=st.text_input('Skin Thickness Value',required=True)
with col2:
  Insulin=st.text_input('Insulin Value',required=True)
with col3:
  BMI=st.text_input('BMI Value',required=True)
with col1:
  DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value',required=True)
with col2:
  Age=st.text_input('Age of the person',required=True)
#code for prediction
diab_diagnosis=''
if st.button('Diabetes Test Result'):
  diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
  if diab_prediction[0]==1:
     diab_diagnosis='The person is diabetic'
  else:
     diab_diagnosis='The person is not diabetic'
st.success(diab_diagnosis)     
