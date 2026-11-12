# Import des librairies nécessaires
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu

st.title("Organisation en Colonnes")
# Création de 3 colonnes de largeur égale
col1, col2, col3 = st.columns(3)
with col1:
 st.header("Métrique A")
 st.metric(label="Utilisateurs", value="1,200", delta="+5%")
with col2:
 st.header("Métrique B")
 st.metric(label="Revenu", value="45 000 €", delta="+12%")
with col3:
 st.header("Métrique C")
 st.metric(label="Conversion", value="3.2%", delta="-0.4%")

st.subheader("Galerie Mascottes (3 images par ligne)")
# Liste des images d'exemple
image_urls = [
 "https://static.streamlit.io/examples/cat.jpg",
 "https://static.streamlit.io/examples/dog.jpg",
 "https://static.streamlit.io/examples/owl.jpg"
]
# Affichage côte à côte sur 3 colonnes
cols = st.columns(3)
for index, url in enumerate(image_urls):
    with cols[index % 3]:
        st.image(url, width="stretch", caption=f"Photo {index + 1}")


# Ajout d'éléments dans la barre latérale

st.sidebar.title("Configuration")
user_role = st.sidebar.selectbox("Rôle :", ["Analyste", "Manager","Admin"])

# Placement du menu de navigation dans la barre latérale
with st.sidebar:
 selected_page = option_menu(
 menu_title="Navigation principale", # Titre du menu (ou None)
 options=["Accueil", "Dashboard Data", "Galerie Photos"], 
 # Liste des pages
 icons=["house", "bar-chart-fill", "images"], 
 # Icônes Bootstrap (optionnel)
 default_index=0 # Page sélectionnée par défaut
 )
4
# Affichage dynamique du contenu selon le choix de navigation
if selected_page == "Accueil":
    st.title(" Bienvenue sur l'Application Data")
    st.write("Sélectionnez un onglet dans le menu latéral pour démarrer l'exploration.")
elif selected_page == "Dashboard Data":
    st.title(" Dashboard d'Analyse")
    st.write("Contenu réservé à l'analyse des données...")
elif selected_page == "Galerie Photos":
    st.title(" Album Photos")
    st.write("Galerie d'images et contenus multimédias...")



# --- 1. INITIALISATION DE LA SESSION ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# --- 2. FONCTION DE VÉRIFICATION DES IDENTIFIANTS ---
@st.cache_data
def load_accounts():
    return pd.read_csv("accounts.csv")

def authenticate(username_input, password_input):
    accounts_df = load_accounts()

    # Vérification de la correspondance nom d'utilisateur et mot de passe
    user_match = accounts_df[
        (accounts_df["name"] == username_input) & 
        (accounts_df["password"] == password_input)
    ]
    return not user_match.empty

# --- 3. GESTION DE L'AFFICHAGE CONDITIONNEL ---
if not st.session_state["logged_in"]:
    
    # --- PAGE DE CONNEXION ---
    st.title("Connexion à l'Application Data")
    st.subheader("Veuillez vous identifier pour accéder au contenu")
    username_input = st.text_input("Nom d'utilisateur")
    password_input = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username_input, password_input):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username_input
            st.success(f"Bienvenue {username_input} !")
            st.rerun()  # Relance le script pour afficher l'application sécurisée
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

else:
    # --- APPLICATION SÉCURISÉE (UTILISATEUR CONNECTÉ) ---

    # 1. Barre latérale : Message de bienvenue et bouton de déconnexion
    with st.sidebar:
        st.write(f"Bienvenue, **{st.session_state['username']}** !")
        if st.button("Se déconnecter"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.rerun()
        st.divider()

    # 2. Barre latérale : Menu de navigation
    with st.sidebar:
        selected_page = option_menu(
            menu_title="Menu principal",
            options=["Accueil", "Galerie Photos"],
            icons=["house", "images"],
            default_index=0
        )

    # 3. Contenu principal des pages
    if selected_page == "Accueil":
        st.title("Page d'Accueil Réservée")
        st.write("Ce contenu est uniquement accessible aux utilisateurs authentifiés.")
        
    elif selected_page == "Galerie Photos":
        st.title("Album Photos")
        st.write("Voici la galerie multimédia organisée sur 3 colonnes :")

        # Exemple d'affichage d'images alignées sur 3 colonnes
        cols = st.columns(3)
        sample_images = [
            "https://static.streamlit.io/examples/cat.jpg",
            "https://static.streamlit.io/examples/dog.jpg",
            "https://static.streamlit.io/examples/owl.jpg"
        ]
        for idx, img_url in enumerate(sample_images):
            with cols[idx % 3]:
                st.image(img_url, caption=f"Image {idx+1}", width="stretch")