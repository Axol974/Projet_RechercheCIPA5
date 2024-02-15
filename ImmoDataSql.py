import sqlite3
import csv


def init():
    connection = sqlite3.connect("prix_immobilier_fictif.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='immobilier'")
    # Vérifier si la table immobilier existe
    table = result.fetchone()
    if not table:
        # Créer la table immobilier
        cursor.execute("CREATE TABLE immobilier (ville TEXT, quartier TEXT, prix INTEGER)")
        print("Table immobilier créée avec succès.")
        # Importer les données du fichier CSV

        with open('prix_immobilier_fictif.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                cursor.execute("INSERT INTO immobilier VALUES (?, ?, ?)",
                               (row['Ville'], row['Quartier'], row['Prix au m2']))
            print("Données importées avec succès.")
        connection.commit()
    connection.close()


def villes():
    connection = sqlite3.connect("prix_immobilier_fictif.db")
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT ville FROM immobilier")
    villes_result = cursor.fetchall()

    villes_result2 = []
    for ville in villes_result:
        villes_result2.append(ville[0])
    print(villes_result2)
    connection.close()
    return villes_result2


def quartiers(ville):
    connection = sqlite3.connect("prix_immobilier_fictif.db")
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT quartier FROM immobilier WHERE ville=?", (ville,))
    quartiers_result = cursor.fetchall()
    quartiers_result2 = []
    for quartier in quartiers_result:
        quartiers_result2.append(quartier[0])
    connection.close()

    return quartiers_result2


def prix_quartiers(ville, quartier):
    connection = sqlite3.connect("prix_immobilier_fictif.db")
    cursor = connection.cursor()

    cursor.execute("SELECT AVG(prix) FROM immobilier WHERE ville=? AND quartier=?", (ville, quartier))
    prix_moyen = cursor.fetchone()
    connection.close()

    prix_moyen = round(prix_moyen[0], 2)
    return prix_moyen


def insert_prix(ville, quartier, prix):
    connection = sqlite3.connect("prix_immobilier_fictif.db")
    try:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO immobilier VALUES (?, ?, ?)", (ville, quartier, prix))
        connection.commit()
    finally:
        connection.close()
