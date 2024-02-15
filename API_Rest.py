from flask import Flask, jsonify, request
from ImmoDataSql import villes, quartiers, prix_quartiers, init, insert_prix

app = Flask(__name__)


@app.route('/villes', methods=['GET'])
def get_villes():
    villes_result = villes()
    return jsonify(villes_result)


# /ville/Paris
@app.route('/ville/<string:ville>', methods=['GET'])
def get_quartiers(ville):
    quarties_result = quartiers(ville)
    # if quarties_result is [] return 404
    if not quarties_result:
        return jsonify({'message': 'Ville non trouvée'}), 404
    return jsonify(quarties_result)


@app.route('/ville/<string:ville>/<string:quartier>', methods=['GET'])
def get_prix_quartiers(ville, quartier):
    prix_quartier_result = prix_quartiers(ville, quartier)
    # if tuple and [1] == 404 return 404 and message at [0]
    if isinstance(prix_quartier_result, tuple):
        return jsonify({'message': prix_quartier_result[0]}), prix_quartier_result[1]

    return jsonify(prix_quartier_result)


@app.route('/ville', methods=['POST'])
def post_ville():
    ville = request.json['ville']
    quartier = request.json['quartier']
    prix = request.json['prix']
    #Verifie si le prix est un nombre
    try:
        float(prix)
    except ValueError:
        return jsonify({'message': 'Le prix doit être un nombre'}), 400
    #Verifie si le prix est positif
    if prix < 0:
        return jsonify({'message': 'Le prix doit être positif'}), 400

    insert_prix(ville, quartier, prix)
    return jsonify({'message': 'Prix ajouté avec succès'})


if __name__ == "__main__":
    init()
    app.run(debug=True)