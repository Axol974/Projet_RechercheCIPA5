import time

import requests
import streamlit as st


def get_villes():
    return requests.get(url + '/villes').json()


def get_quartiers(ville):
    return requests.get(url + '/ville/' + ville).json()


def get_prix_moyen(ville, quartier):
    return requests.get(url + '/ville/' + ville + '/' + quartier).json()


def post_prix(ville, quartier, prix):
    return requests.post(url + '/ville', json={'ville': ville, 'quartier': quartier, 'prix': prix}).json()['message']


# url api
url = 'http://127.0.0.1:5000'

st.title("Prix immobilier")

tab_titles = ['Calculer', 'Ajouter']
tab1, tab2 = st.tabs(tab_titles)


# Add content to each tab
with tab1:
    # Liste déroulante des villes à récupérer depuis l'API (/villes)
    ville_selected = st.selectbox('Ville', get_villes())

    # Liste déroulante des quartiers à récupérer depuis l'API (/ville/<ville>)
    quartier_selected = st.selectbox('Quartier', get_quartiers(ville_selected))

    # Récupérer le prix moyen depuis l'API (/ville/<ville>/<quartier>)
    st.write('Prix moyen au m² :', get_prix_moyen(ville_selected, quartier_selected), '€')

with tab2:
    # Saisie de la ville
    ville = st.text_input('Ville')

    # Saisie du quartier
    quartier = st.text_input('Quartier')

    # Saisie du prix
    prix = st.number_input('Prix', min_value=0)

    # Bouton pour ajouter le prix
    if st.button('Ajouter'):
        # Appel de l'API pour ajouter le prix
        # Afficher le message de retour de l'API pendant 3 secondes
        test = st.success(post_prix(ville, quartier, prix))
        time.sleep(3)
        test.empty()
        st.rerun()
