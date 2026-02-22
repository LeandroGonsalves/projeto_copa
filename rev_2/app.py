from flask import Flask, jsonify, request
from marshmallow import ValidationError
from schemas import PartidaSchema
from rich import print

app = Flask(__name__)

schema_partida = PartidaSchema()


@app.route("/jogos", methods=["PUT"])
def rodada1():

    json_data = request.get_json()

    if not json_data:
        return jsonify({
            "success": False,
            "error": "JSON não enviado"
        }), 400

    try:
        dados_validados = schema_partida.load(json_data)
    except ValidationError as err:
        return jsonify({
            "success": False,
            "erros": err.messages
        }), 400

    print(dados_validados)

    return jsonify({
        "success": True,
        "data": dados_validados
    }), 200


@app.route("/health-check")
def health_check():
    return jsonify({
        "status": "ok",
        "message": "API da Copa funcionando"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)