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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

#fonction pour envoi email 
# def envoyer_email(nom, email, objet, message):
# destinataire = "thierrycosendai@gmail.com"
# mot de passe = "Graciamaria1986"

#msg = MIMEText(message)
#msg=['Subject'] = object
#msg=['From'] = email
#msg=['To'] = destinataire
# with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
#   smtp_server.login(email,mot_de_passe)
#   smtp_server.sendmail(email, destinataire, msg.as_string())

col1,col2=st.Columns([1,3]) #colonne1 pour la navbar(1/4),colonne 2 pour le contenu (3/4)
with st.sidebar:
    selected = option_menu(
        menu_title = "Main menu",
        options= [Accueil","EDA","Predictions Iris", "contact"],
        icons = ["house", "graph-up-arrow","database", "enveloppe"],
        menu_icon = "cast",
        default_index = 0,
    ) 
    #Fonction pour l'envoi des donnees à l'API
    def send_data_to_api(data):
        response=predict(data)
        return response.json()

    def load_model()
       mode1 = joblib.load('model_classifier_iris.pkl')
       scale = joblib.load("scaler.pkl")

       return model,scale
#Extraction des caracteristiques
    def predict(data):
    model,scale = load_model()
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']
    # creation tableau Numpy de caracteristiques
    features = np.array([[sepal_length,sepal_width,petal_length,petal_width]])
    #Conversion en dataframe
    X_train = pd.DataFrame(features, columns=['SepalLength','SepalWidth','PetalLength',PetalWidth'])
    #Normalisation
    X_train_normalized = scale.transform(X_train)
    #predire à partir du modele
    prediction= model.predict(X_train_normalized)
    #retourne la prediction
        return prediction[0]
   except Exception as e:
       return
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
         if st.button ("Predire la fleur...,help="Cliquer pour envoyer les données",type="primary"): data={
                                                                                             "sepal_length":sepal_length,
                                                                                    "sepal_width": sepal_width,
                                                                                         "petal_length":petal_length,
                                                                                                    "petal_width": petal_width
                                                                                   }
                   #Envoyer les données de l'API
                   reponse= predict(data);
                   #Envoyer la reponse de l'API
                   # st.write(<p style=style='font-size:20px;font-weight:bold;'> Votre fleur semble être:<span style='color:#ff4b4c;'>",response,"</span> </p> unsafe_allow_html=true)
                   my_data = "iris.csv"
                   def explore_data(dataset)
                   df=pd.read_csv(os.path.join(dataset),sep=";")
                   return df
                   if selected == "Accueil":
                   st.title("Accueil")
                   texte_a_afficher"""< div style= "text-align: justify;">
                   <i> 'informatique</i>

                    st.markdown(texte_a_afficher, unsafe_allow_html=True)

if selected == "EDA":
    st.title("Iris EDA")
    data = explore_data(my_data)
    if st.checkbox("Preview Data"):
        
        if st.button("Head"):
            st.write(data.head())

        if st.button("Sample"):
            st.write(data.sample(5))

        if st.button("Show All Dataset"):
            st.write(data)

    if st.checkbox("Show Columns Names"):
        st.write(data.columns)

    text_dim = st.radio("What Dimensions Do You Want To See?", ("Rows", "Columns", "All"))
    if text_dim == "Rows":
        st.text("Nombre de ligne:")
        st.write(data.shape[0]) 
    elif text_dim == "Columns":
        st.text("Nombre de colonne:")
        st.write(data.shape[1])   
    else:
        st.text("Dimensions:")
        st.write(data.shape) 

    if st.checkbox("Show Summary of Dataset"):
        st.write(data.describe())

    if st.checkbox("percentage of distributions"):
        effectif = data["Species"].value_counts()
        fig, ax = plt.subplots()
        st.write(plt.pie(effectif, labels=effectif.index, autopct='%1.2f%%'))
        plt.title("Répartition des modalités")
        plt.axis('equal')
        st.pyplot(fig)
    
    if st.checkbox("Visualization"):
        fig, ax = plt.subplots()
        st.write(sns.scatterplot(data=data, x="PetalLength", y="PetalWidth", hue="Species", s=100))
        st.pyplot(fig)

    if st.checkbox("Correlation"):
        fig, ax = plt.subplots()
        data_x = data.drop(columns="Species", axis=1)
        corr_matrix = data_x.corr()
        st.write(sns.heatmap(corr_matrix, annot=True, linewidths=.5,))
        st.pyplot(fig)

if selected == "Predictions Iris":
    front_iris()
    
if selected == "Contact":
    st.title("Formulaire de Contact")

    # Créer un formulaire
    with st.form("contact_form"):
        nom = st.text_input("Nom")
        email = st.text_input("Email")
        objet = st.text_input("Objet")
        message = st.text_area("Message")

        # Bouton pour soumettre le formulaire
        submitted = st.form_submit_button("Envoyer", type="primary")

        if submitted:
            # Vérifier si tous les champs sont remplis
            if not nom or not email or not objet or not message:
                st.error("Tous les champs sont obligatoires!")
            else:
                 st.error("Cette fonctionnailté n'est pas encore achévée...")
                # try:
                #     envoyer_email(nom, email, objet, message)
                #     st.success(f"Merci, {nom}, votre message a été envoyé !")
                # except Exception as e:
                #     st.error(f"Une erreur est survenue lors de l'envoi de l'email : {e}")

                    teccnopedagogue
                    .......
                    </div>"""
