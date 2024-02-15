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
    return jsonify(quarties_result)


@app.route('/ville/<string:ville>/<string:quartier>', methods=['GET'])
def get_prix_quartiers(ville, quartier):
    prix_quartier_result = prix_quartiers(ville, quartier)
    return jsonify(prix_quartier_result)


@app.route('/ville', methods=['POST'])
def post_ville():
    ville = request.json['ville']
    quartier = request.json['quartier']
    prix = request.json['prix']
    insert_prix(ville, quartier, prix)
    return jsonify({'message': 'Prix ajouté avec succès'})


if __name__ == "__main__":
    init()
    app.run(debug=True)
