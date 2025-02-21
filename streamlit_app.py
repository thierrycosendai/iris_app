import streamlit as st
import numpy as np
import pandas as pd ;
import joblib
st.title("PREDICTION DE L'ESPECE D'IRIS")
PetalLength =st.slider("PetalLength", 0.0, 10.0, value=2.0, step=0.1)
SepalLength = st.slider("SepalLength", 0.0, 10.0, value=0.2, step=0.1)
PetalWidth =st.slider("PetalWidth ", 0.0, 10.0, value=2.0, step=0.1)
SepalWidth = st.slider("SepalWidth", 0.0, 10.0, value=0.3, step=0.1)
      
if st.button("Prediction sur la fleur", help="Cliquez pour envoyer les donnees", type="primary"): 
   
   
    f = np.array([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
    X = pd.DataFrame(f,columns=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"])
    scaler= joblib.load("mon_scaler.pkl")
    model=joblib.load("mon_model2.pkl")
    X_transform = scaler.transform(X)
    prediction = model.predict(X_transform)
    response = prediction[0]
    st.write("fleur est: ", response)
