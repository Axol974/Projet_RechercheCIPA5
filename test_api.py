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
