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
  Pregnancies=st.text_input('Number of Pregnancies')  
with col2: 
  Glucose=st.text_input('Glucose Level')
with col3:
  BloodPressure=st.text_input('Blood Pressure Value')  
with col1:
  SkinThickness=st.text_input('Skin Thickness Value')
with col2:
  Insulin=st.text_input('Insulin Value')  
with col3:
  BMI=st.text_input('BMI Value')   
with col1:
  DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
with col2:
  Age=st.text_input('Age of the person')  
#code for prediction
diab_diagnosis=''
if st.button('Diabetes Test Result'):
  if not Pregnancies:
     st.error("Please enter number of pregnancies")  
  if not Glucose:
     st.error("Please enter Glucose Level") 
  if not BloodPressure:
     st.error("Please Blood Pressure Value")    
  if not SkinThickness:
     st.error("Please enter Skin Thickness Value")  
  if not Insulin:
     st.error("Please enter Insulin Value") 
  if not BMI:
     st.error("Please enter BMI Value")    
  if not DiabetesPedigreeFunction:
     st.error("Please Diabetes Pedigree Function Value")      
  if not Age:
     st.error("Please enter age")         
  diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
  if diab_prediction[0]==1:
     diab_diagnosis='The person is diabetic'
  else:
     diab_diagnosis='The person is not diabetic'
st.success(diab_diagnosis)     
