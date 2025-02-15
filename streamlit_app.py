import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylot as plt

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
@st.cache
def load_data():
    return pd.read_csv("iris.csv")

data = load_data()

# Titre de l'application
st.title("Formulaire d'Utilisation des Données Iris")

# Formulaire utilisateur
st.sidebar.header("Formulaire")
name = st.sidebar.text_input("Votre nom")
age = st.sidebar.number_input("Votre âge", min_value=1, max_value=100, step=1)
feedback = st.sidebar.text_area("Votre avis sur l'application")
submit = st.sidebar.button("Soumettre")

if submit:
    st.sidebar.success(f"Merci {name}, votre avis a été enregistré !")

# Menu latéral
st.sidebar.header("Options d'affichage des données")
if st.sidebar.checkbox("Afficher les données brutes"):
    st.subheader("Aperçu des Données")
    st.write(data.head())

# Sélection de la variable pour l'analyse
selected_column = st.sidebar.selectbox("Sélectionnez une colonne pour l'analyse", data.columns[:-1])

# Affichage de statistiques descriptives
st.subheader(f"Statistiques de {selected_column}")
st.write(data[selected_column].describe())

# Affichage de l'histogramme
st.subheader("Distribution de la variable sélectionnée")
fig, ax = plt.subplots()
sns.histplot(data[selected_column], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Affichage des données filtrées par espèce
st.sidebar.subheader("Filtrer par espèce")
species = st.sidebar.selectbox("Sélectionnez une espèce", data["species"].unique())
st.subheader(f"Données filtrées pour : {species}")
st.write(data[data["species"] == species])
