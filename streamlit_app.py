import streamlit as st 
from streamlit_option _menu import option_menu
import requests
import joblib
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import smtplib
import json
def front_iris():
         st.markdown("<h1 style='text-align:center;'> PREDICTION DU TYPE DE FLEUR D'iris"/h1", unsafe_allow_html=True)
         col1,col2=st.columns([1,3]) #colonne 1 pour la navbar(1/4),colonne 2 pour le contenu(3/4)
         #navbar verticale dans la colonne de gauche
         col1,col2 = st.columns(2)
         with col1;
         sepal_length=st.slider("Longueur du sépal", 0.0, 10.0,value=0.0, step=0.1)
         with col2;
         sepal_length=st.slider("Largeur du sépal", 0.0, 10.0,value=0.0, step=0.1)
         #Deuxième ligne avec deux autres curseurs
         col3,col4 = st.columns(2)
         with col3;
         petal_length=st.slider("Longueur du petale", 0.0, 10.0,value=0.0, step=0.1)
         with col4;*
          petal_width=st.slider("Longueur du petale", 0.0, 10.0,value=0.0, step=0.1)
         petal_width=st.slider("Largeur du petale", 0.0, 10.0,value=0.0, step=0.1)
         #Bouton pour envoyer les données à l'API

                    
