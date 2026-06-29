#libraries
import streamlit as st
import pandas as pd
import sklearn
import numpy as np
import pickle

#load the model using pickle
mod = pickle.load(open('linear_regression_model.pkl','rb')) #rb--> read+binary 
#rb -- open the file in binary mode and read the binary data inside it 

#creating a web app using stream lit (to run it --> streamlit run file_name.py)
st.title("Linear Regression model using Scikit learn") #title of the web app
tv =st.text_input("Enter TV sales...") #blanks to fill the value
radio =st.text_input("Enter radio sales...")
newspaper =st.text_input("Enter newspaper sales....")

if st.button("Predict"):
    features = np.array([[tv,radio,newspaper]], dtype =np.float64) #dtype-->coverts input values into decimal
    results =mod.predict(features).reshape(1,-1) #predicting the output 1- all rows, -1 - last columns
    st.write("Predicted sales::::", results[0]) #to print anything in streamlit we use write
    #result[0] --- returns the result at 0th index