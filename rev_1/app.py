# POST http://127.0.0.1:5000/api/init
# GET  http://127.0.0.1:5000/api/classificacao
# PUT  http://127.0.0.1:5000/api/placar

from flask import Flask, jsonify, request
from services.storage import (inicializar_database, carregar_competicao, salvar_competicao)
from services.competition import (atualizar_placar, gerar_classificacao, gerar_oitavas, garantir_fase_final, atualizar_placar_oitavas)
from services.bootstrap import criar_estrutura_inicial
from flask import render_template


# Cria a instância principal da aplicação
app = Flask(__name__)

quartas = []

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


@app.route("/admin/gerar-oitavas")
def gerar_oitavas_admin():

    competicao = carregar_competicao()

    if not competicao:
        return "Nenhuma competição iniciada.", 400

    data = competicao["data"]

    garantir_fase_final(data)

    classificacao = gerar_classificacao(data)

    data["fase_final"]["oitavas"] = gerar_oitavas(classificacao)

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        data
    )

    return "Oitavas geradas com sucesso!"


@app.route("/api/oitavas/placar", methods=["PUT"])
def atualizar_oitavas():

    dados = request.json

    id_jogo = dados["id_jogo"]
    gols_mandante = int(dados["gols_mandante"])
    gols_visitante = int(dados["gols_visitante"])

    penaltis_mandante = dados.get("penaltis_mandante")
    penaltis_visitante = dados.get("penaltis_visitante")

    if penaltis_mandante is not None:
        penaltis_mandante = int(penaltis_mandante)

    if penaltis_visitante is not None:
        penaltis_visitante = int(penaltis_visitante)

    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    try:
        competicao_atualizada = atualizar_placar_oitavas(
            competicao["data"],
            id_jogo,
            gols_mandante,
            gols_visitante,
            penaltis_mandante,
            penaltis_visitante
        )
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        competicao_atualizada
    )

    return jsonify({"mensagem": "Placar das oitavas atualizado!"})


@app.route("/api/oitavas", methods=["GET"])
def listar_oitavas():

    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    return jsonify(
        competicao["data"]
        .get("fase_final", {})
        .get("oitavas", [])
    )


@app.route("/admin/gerar-quartas")
def gerar_quartas():

    competicao = carregar_competicao()

    if not competicao:
        return {"erro": "Nenhuma competição iniciada."}, 400

    data = competicao["data"]

    oitavas = (
        data
        .get("fase_final", {})
        .get("oitavas", [])
    )

    if not oitavas:
        return {"erro": "Oitavas ainda não foram geradas."}, 400

    vencedores = []

    for jogo in oitavas:
        if not jogo.get("vencedor"):
            return {"erro": "Ainda existem oitavas sem vencedor."}, 400
        vencedores.append(jogo["vencedor"])

    quartas = []

    for i in range(0, len(vencedores), 2):
        quartas.append({
            "id_jogo": (i // 2) + 1,
            "mandante": vencedores[i],
            "visitante": vencedores[i+1],
            "gols_mandante": 0,
            "gols_visitante": 0,
            "penaltis_mandante": None,
            "penaltis_visitante": None,
            "vencedor": None,
            "finalizado": False
        })

    data["fase_final"]["quartas"] = quartas

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        data
    )

    return {"mensagem": "Quartas de final geradas com sucesso!"}



@app.route("/api/quartas")
def listar_quartas():

    competicao = carregar_competicao()

    if not competicao:
        return {"erro": "Nenhuma competição iniciada."}, 400

    return (
        competicao["data"]
        .get("fase_final", {})
        .get("quartas", [])
    )


@app.route("/api/quartas/placar", methods=["PUT"])
def atualizar_quartas():

    competicao = carregar_competicao()

    if not competicao:
        return {"erro": "Nenhuma competição iniciada."}, 400

    data = competicao["data"]

    quartas = (
        data
        .get("fase_final", {})
        .get("quartas", [])
    )

    req = request.json
    id_jogo = req.get("id_jogo")

    jogo = next((j for j in quartas if j["id_jogo"] == id_jogo), None)

    if not jogo:
        return {"erro": "Jogo não encontrado."}, 404

    jogo["gols_mandante"] = req.get("gols_mandante")
    jogo["gols_visitante"] = req.get("gols_visitante")
    jogo["penaltis_mandante"] = req.get("penaltis_mandante")
    jogo["penaltis_visitante"] = req.get("penaltis_visitante")

    if jogo["gols_mandante"] > jogo["gols_visitante"]:
        jogo["vencedor"] = jogo["mandante"]
    elif jogo["gols_visitante"] > jogo["gols_mandante"]:
        jogo["vencedor"] = jogo["visitante"]
    else:
        if jogo["penaltis_mandante"] is not None and jogo["penaltis_visitante"] is not None:
            if int(jogo["penaltis_mandante"]) > int(jogo["penaltis_visitante"]):
                jogo["vencedor"] = jogo["mandante"]
            else:
                jogo["vencedor"] = jogo["visitante"]
        else:
            return {"erro": "Empate exige pênaltis."}, 400

    jogo["finalizado"] = True

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        data
    )

    return {"mensagem": "Quartas atualizadas com sucesso!"}



@app.route("/health-check")
def health_check():
    return jsonify({"status": "ok", "message": "API da Copa funcionando"}), 200


if __name__ == "__main__":
    app.run(debug=True)
