import pandas as pd


def villes():
    # Lire le fichier CSV
    df = lire_csv()

    # renvoyer la liste des villes
    villes_result = df['Ville'].unique().tolist()
    return villes_result


def quartiers(ville):
    # Lire le fichier CSV
    df = lire_csv()

    # renvoyer la list des quartiers
    quartiers_result = df[df['Ville'] == ville]['Quartier'].unique().tolist()
    return quartiers_result


def prix_quartiers(ville, quartier):
    # Lire le fichier CSV
    df = lire_csv()

    # renvoyer  sous forme de dictionnaire la moyenne des prix au m² pour un quartier
    prix_moyen = df[(df['Ville'] == ville) & (df['Quartier'] == quartier)]['Prix au m²'].mean()

    # Aprocher le prix moyen à 2 chiffres après la virgule
    prix_moyen = round(prix_moyen, 2)

    return prix_moyen


# Fonction pour Lire le fichier CSV avec Pandas
# entête: Ville,Quartier,Prix au m²
def lire_csv():
    df = pd.read_csv('prix_immobilier_fictif.csv', sep=',')
    return df
