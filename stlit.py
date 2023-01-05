# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:30:24 2023

@author: Shagun
"""

import streamlit as st
import sklearn 
from sklearn.linear_model import LinearRegression
model = LinearRegression()
st.title('Product Demand Prediction App')
BP = st.number_input('Base price')
TP = st.number_input('Total price')
def predicts(BP,TP):
    prediction = model.predict([[BP,TP]])
    return prediction
if st.button('Predict Units'):
    Units = predicts(BP,TP)
    st.success(st.success(f'The predicted price of the diamond is ${Units[0]:.2f} Unit'))

