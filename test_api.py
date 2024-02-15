import pytest
import requests

# URL de base de l'API
BASE_URL = "http://127.0.0.1:5000"


def test_get_villes():
    response = requests.get(f"{BASE_URL}/villes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_quartiers():
    ville = "Paris"  # Utilisez une ville existante dans votre base de données
    response = requests.get(f"{BASE_URL}/ville/{ville}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_prix_quartiers():
    ville = "Paris"  # Utilisez une ville existante dans votre base de données
    quartier = "Sud"  # Utilisez un quartier existant dans votre base de données
    response = requests.get(f"{BASE_URL}/ville/{ville}/{quartier}")
    assert response.status_code == 200
    # Verifier que le prix est un nombre
    # verify if can convert to float
    try:
        float(response.json())
    except ValueError:
        assert False


def test_post_ville():
    ville = "NouvelleVille"
    quartier = "NouveauQuartier"
    prix = 5000
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier, 'prix': prix})
    assert response.status_code == 200
    assert response.json() == {'message': 'Prix ajouté avec succès'}

    response2 = requests.get(f"{BASE_URL}/ville/{ville}/{quartier}")
    assert response2.status_code == 200
    # Verifier que le prix est un nombre
    # verify if can convert to float
    try:
        float(response2.json())
    except ValueError:
        assert False
    # Verifier que le prix est bien celui qu'on a ajouté
    assert float(response2.json()) == prix


def test_get_quartiers_non_existant():
    ville = "NonExistantCity"  # Utilisez une ville qui n'existe pas dans votre base de données
    response = requests.get(f"{BASE_URL}/ville/{ville}")
    assert response.status_code == 404  # Le code de statut HTTP pour "Not Found" est 404


def test_get_prix_quartiers_non_existant():
    ville = "Paris"  # Utilisez une ville existante dans votre base de données
    quartier = "NonExistantQuartier"  # Utilisez un quartier qui n'existe pas dans votre base de données
    response = requests.get(f"{BASE_URL}/ville/{ville}/{quartier}")
    assert response.status_code == 404  # Le code de statut HTTP pour "Not Found" est 404


def test_post_ville_prix_negatif():
    ville = "NouvelleVille"
    quartier = "NouveauQuartier"
    prix = -5000  # Utilisez une valeur négative pour le prix
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_sans_ville():
    quartier = "NouveauQuartier"
    prix = 5000
    response = requests.post(f"{BASE_URL}/ville", json={'quartier': quartier, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_sans_quartier():
    ville = "NouvelleVille"
    prix = 5000
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_sans_prix():
    ville = "NouvelleVille"
    quartier = "NouveauQuartier"
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_prix_non_numerique():
    ville = "NouvelleVille"
    quartier = "NouveauQuartier"
    prix = "non_numerique"
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_prix_chaine_vide():
    ville = "NouvelleVille"
    quartier = "NouveauQuartier"
    prix = ""  # Utilisez une chaîne vide pour le prix
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_ville_chaine_vide():
    ville = ""  # Utilisez une chaîne vide pour la ville
    quartier = "NouveauQuartier"
    prix = 5000
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400


def test_post_ville_quartier_chaine_vide():
    ville = "NouvelleVille"
    quartier = ""  # Utilisez une chaîne vide pour le quartier
    prix = 5000
    response = requests.post(f"{BASE_URL}/ville", json={'ville': ville, 'quartier': quartier, 'prix': prix})
    assert response.status_code == 400  # Le code de statut HTTP pour "Bad Request" est 400
