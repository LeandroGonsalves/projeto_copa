# POST http://127.0.0.1:5000/api/init
# GET  http://127.0.0.1:5000/api/classificacao
# PUT  http://127.0.0.1:5000/api/placar

from flask import Flask, jsonify, request
from services.storage import (inicializar_database, carregar_competicao, salvar_competicao)
from services.competition import atualizar_placar, gerar_classificacao
from services.bootstrap import criar_estrutura_inicial
from flask import render_template


# Cria a instância principal da aplicação
app = Flask(__name__)

@app.route("/")
def publico():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/api/init", methods=["POST"])
def iniciar_competicao():
    inicializar_database()

    competicao = criar_estrutura_inicial()

    salvar_competicao(
        id_copa=1,
        competition_name="copa_2002",
        data=competicao
    )

    return jsonify({"mensagem": "Competição iniciada com sucesso!"})


@app.route("/api/placar", methods=["PUT"])
def atualizar():
    dados = request.json

    grupo = dados["grupo"]
    id_partida = dados["id_partida"]
    placar = dados["placar"]

    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    competicao_atualizada = atualizar_placar(
        competicao["data"],
        grupo,
        id_partida,
        placar
    )

    for gols in placar.values():
        if gols < 0:
            return jsonify({"erro": "Gols não podem ser negativos"}), 400

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        competicao_atualizada
    )

    return jsonify({"mensagem": "Placar atualizado com sucesso!"})


@app.route("/api/classificacao", methods=["GET"])
def classificacao():
    """
        - Carrega a competição do CSV
        - Gera a classificação ordenada
        - Retorna em formato JSON
    """

    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    classificacao = gerar_classificacao(competicao["data"])

    return jsonify(classificacao)



@app.route("/api/grupo/<grupo>", methods=["GET"])
def obter_grupo(grupo):
    competicao = carregar_competicao()
    
    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    dados = competicao["data"]

    if grupo not in dados["grupos"]:
        return jsonify({"erro": "Grupo não encontrado"}), 404

    grupo_dados = dados["grupos"][grupo]

    times = list(grupo_dados["times"].keys())

    partidas = []
    for p in grupo_dados["partidas"]:
        partidas.append({
            "id_partida": p["id_partida"],
            "rodada": p["rodada"],
            "time1": p["time1"],
            "time2": p["time2"]
        })

    return jsonify({
        "times": times,
        "partidas": partidas
    })


@app.route("/health-check")
def health_check():
    return jsonify({"status": "ok", "message": "API da Copa funcionando"}), 200


if __name__ == "__main__":
    app.run(debug=True)
