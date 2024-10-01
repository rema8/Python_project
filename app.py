import streamlit as st 
import sqlite3 
from datetime import datetime 

st.title("Application de recommandations de films")

# Inscription 
st.header("Inscription")
nom = st.text_input("Nom")
prenom = st.text_input("Prenom")
email = st.text_input("Email")
mot_de_passe = st.text_input('Mot de passe', type="password")
# connexion a  la db
def ajouter_utilisateur (prenom,nom,email,mot_de_passe):
    conn = sqlite3.connect('movies.db')
    cursor=conn.cursor()

# inserer l'utilisateur dans la table 

    cursor.execute("INSERT INTO utilisateurs_reels (prenom,nom,email,mot_de_passe) VAlUES (?,?,?,?)",(prenom,nom,email,mot_de_passe) )
    conn.commit()
    conn.close()

if st.button("Sinscrire"):
    ajouter_utilisateur(prenom,nom,email,mot_de_passe)
    st.success(f"Inscription réussie pour {prenom} {nom}")