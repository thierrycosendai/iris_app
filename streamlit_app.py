import streamlit as st 
import requests
import joblibimport numpy as np
import pandas as pd
import os

# Titre de l'application
st.title("Prédiction des espèces d'Iris")

# Formulaire de saisie des caractéristiques
st.sidebar.header("Entrée des caractéristiques")
sepal_length88 if= st.sidebar.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.sidebar.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.sidebar.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.sidebar.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)

