# POST http://127.0.0.1:5000/api/init
# GET  http://127.0.0.1:5000/api/classificacao
# PUT  http://127.0.0.1:5000/api/placar
from flask import Flask, jsonify, request, render_template
from services.storage import (
    inicializar_database,
    carregar_competicao,
    salvar_competicao
)
from services.competition import (
    atualizar_placar,
    gerar_classificacao,
    gerar_oitavas,
    garantir_fase_final,
    atualizar_placar_oitavas
)
from services.bootstrap import criar_estrutura_inicial

app = Flask(__name__)


# ==============================
# PÁGINAS
# ==============================

@app.route("/")
def publico():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


# ==============================
# INICIALIZAÇÃO
# ==============================

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


# ==============================
# FASE DE GRUPOS
# ==============================

@app.route("/api/placar", methods=["PUT"])
def atualizar():
    dados = request.json

    grupo = dados["grupo"]
    id_partida = dados["id_partida"]
    placar = dados["placar"]

    for gols in placar.values():
        if gols < 0:
            return jsonify({"erro": "Gols não podem ser negativos"}), 400

    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    competicao_atualizada = atualizar_placar(
        competicao["data"],
        grupo,
        id_partida,
        placar
    )

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


# ==============================
# OITAVAS
# ==============================

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


@app.route("/api/oitavas/placar", methods=["PUT"])
def atualizar_oitavas():
    dados = request.json

    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    try:
        competicao_atualizada = atualizar_placar_oitavas(
            competicao["data"],
            int(dados["id_jogo"]),
            int(dados["gols_mandante"]),
            int(dados["gols_visitante"]),
            dados.get("penaltis_mandante"),
            dados.get("penaltis_visitante")
        )
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        competicao_atualizada
    )

    return jsonify({"mensagem": "Placar das oitavas atualizado!"})


# ==============================
# QUARTAS
# ==============================

@app.route("/admin/gerar-quartas")
def gerar_quartas():
    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    data = competicao["data"]

    oitavas = (
        data
        .get("fase_final", {})
        .get("oitavas", [])
    )

    if not oitavas:
        return jsonify({"erro": "Oitavas ainda não foram geradas."}), 400

    vencedores = []

    for jogo in oitavas:
        if not jogo.get("vencedor"):
            return jsonify({"erro": "Ainda existem oitavas sem vencedor."}), 400
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

    return jsonify({"mensagem": "Quartas de final geradas com sucesso!"})


@app.route("/api/quartas", methods=["GET"])
def listar_quartas():
    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    return jsonify(
        competicao["data"]
        .get("fase_final", {})
        .get("quartas", [])
    )


@app.route("/api/quartas/placar", methods=["PUT"])
def atualizar_quartas():
    competicao = carregar_competicao()

    if not competicao:
        return jsonify({"erro": "Nenhuma competição iniciada."}), 400

    data = competicao["data"]

    quartas = (
        data
        .get("fase_final", {})
        .get("quartas", [])
    )

    if not quartas:
        return jsonify({"erro": "Quartas ainda não geradas."}), 400

    req = request.json
    id_jogo = int(req.get("id_jogo"))

    jogo = next((j for j in quartas if j["id_jogo"] == id_jogo), None)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado."}), 404

    gols_mandante = int(req.get("gols_mandante", 0))
    gols_visitante = int(req.get("gols_visitante", 0))

    penaltis_mandante = req.get("penaltis_mandante")
    penaltis_visitante = req.get("penaltis_visitante")

    if penaltis_mandante is not None:
        penaltis_mandante = int(penaltis_mandante)

    if penaltis_visitante is not None:
        penaltis_visitante = int(penaltis_visitante)

    jogo["gols_mandante"] = gols_mandante
    jogo["gols_visitante"] = gols_visitante
    jogo["penaltis_mandante"] = penaltis_mandante
    jogo["penaltis_visitante"] = penaltis_visitante

    if gols_mandante > gols_visitante:
        jogo["vencedor"] = jogo["mandante"]
    elif gols_visitante > gols_mandante:
        jogo["vencedor"] = jogo["visitante"]
    else:
        if penaltis_mandante is None or penaltis_visitante is None:
            return jsonify({"erro": "Empate exige pênaltis."}), 400

        if penaltis_mandante > penaltis_visitante:
            jogo["vencedor"] = jogo["mandante"]
        else:
            jogo["vencedor"] = jogo["visitante"]

    jogo["finalizado"] = True

    salvar_competicao(
        competicao["id_copa"],
        competicao["competition_name"],
        data
    )

    return jsonify({"mensagem": "Quartas atualizadas com sucesso!"})




# ==============================
# HEALTH CHECK
# ==============================

@app.route("/health-check")
def health_check():
    return jsonify({"status": "ok", "message": "API da Copa funcionando"}), 200


if __name__ == "__main__":
    app.run(debug=True)
