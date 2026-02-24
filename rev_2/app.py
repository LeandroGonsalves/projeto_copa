from flask import Flask, jsonify, request
from marshmallow import ValidationError
from schemas import PartidaSchema
from rich import print
from funcoes import atualizar_dados_jogo, buscar_partidas, buscar_classificacao, gerar_oitavas

app = Flask(__name__)

schema_partida = PartidaSchema()


@app.route("/jogos", methods=["PUT"])
def rodadas():

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

    #print(dados_validados)

    atualizar_dados_jogo(dados_validados)

    return jsonify({
        "success": True,
        "data": dados_validados
    }), 200


@app.route("/jogos", methods=["GET"])
def listar_jogos():

    dados = buscar_partidas()
    print(dados)

    return jsonify({
        "success": True,
        "data": dados
    }), 200



@app.route("/classificacao", methods=["GET"])
def classificacao():

    dados = buscar_classificacao()
    print(dados)

    gerar_oitavas(dados)

    return jsonify({
        "success": True,
        "data": dados
    }), 200



@app.route("/health-check")
def health_check():
    return jsonify({
        "status": "ok",
        "message": "API da Copa funcionando"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)