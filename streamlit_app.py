import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylot as plt

# Charger les données
@st.cache
def load_data():
    return pd.read_csv("iris.csv")

data = load_data()
@st.cache
def load_model():
    with open("iris_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model
model = load_model()
# Titre de l'application
st.title("Formulaire d'Utilisation des Données Iris")
st.sidebar.header("Entrée des caractéristiques")
sepal_length = st.sidebar.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.sidebar.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.sidebar.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.sidebar.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)

if st.sidebar.button("Prédire"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)[0]
    st.sidebar.success(f"L'espèce prédite est : {prediction}")




