def recalcular_tabela(grupo_data):

    # Zera todos os times
    for time in grupo_data["times"].values():
        time["pontos"] = 0
        time["gm"] = 0
        time["gs"] = 0

    # Percorre partidas
    for partida in grupo_data["partidas"]:

        # 🔒 Se ainda não tem placar, ignora
        if partida["gols"] is None:
            continue

        time1 = partida["time1"]
        time2 = partida["time2"]

        gols1 = partida["gols"][time1]
        gols2 = partida["gols"][time2]

        # Gols marcados/sofridos
        grupo_data["times"][time1]["gm"] += gols1
        grupo_data["times"][time1]["gs"] += gols2

        grupo_data["times"][time2]["gm"] += gols2
        grupo_data["times"][time2]["gs"] += gols1

        # Pontos
        if gols1 > gols2:
            grupo_data["times"][time1]["pontos"] += 3
        elif gols2 > gols1:
            grupo_data["times"][time2]["pontos"] += 3
        else:
            grupo_data["times"][time1]["pontos"] += 1
            grupo_data["times"][time2]["pontos"] += 1


def atualizar_placar(competicao, grupo, id_partida, novo_placar):

    grupo_data = competicao["grupos"][grupo]

    partida = next(
        (p for p in grupo_data["partidas"] if p["id_partida"] == id_partida),
        None
    )

    if not partida:
        raise ValueError("Partida não encontrada")

    time1 = partida["time1"]
    time2 = partida["time2"]

    gols1 = int(novo_placar.get(time1, 0))
    gols2 = int(novo_placar.get(time2, 0))

    # 🔥 Aqui criamos o dicionário de gols
    partida["gols"] = {
        time1: gols1,
        time2: gols2
    }

    recalcular_tabela(grupo_data)

    return competicao


def gerar_classificacao(competicao):

    resultado = {}

    for nome_grupo, dados_grupo in competicao["grupos"].items():

        tabela = []

        for nome_time, stats in dados_grupo["times"].items():

            saldo = stats["gm"] - stats["gs"]

            tabela.append({
                "selecao": nome_time,
                "pontos": stats["pontos"],
                "gm": stats["gm"],
                "gs": stats["gs"],
                "saldo": saldo
            })

        tabela_ordenada = sorted(
            tabela,
            key=lambda x: (x["pontos"], x["saldo"], x["gm"]),
            reverse=True
        )

        resultado[nome_grupo] = tabela_ordenada

    return resultado


def gerar_oitavas(classificacao):

    CHAVEAMENTO_OITAVAS = [
        ("A", 1, "H", 2),
        ("A", 2, "H", 1),
        ("B", 1, "G", 2),
        ("B", 2, "G", 1),
        ("C", 1, "F", 2),
        ("C", 2, "F", 1),
        ("D", 1, "E", 2),
        ("D", 2, "E", 1),
    ]

    oitavas = []

    for grupo1, pos1, grupo2, pos2 in CHAVEAMENTO_OITAVAS:

        # 🔥 CORREÇÃO AQUI — usar apenas a letra do grupo
        if grupo1 not in classificacao or grupo2 not in classificacao:
            continue

        if len(classificacao[grupo1]) < pos1 or len(classificacao[grupo2]) < pos2:
            continue

        time1 = classificacao[grupo1][pos1 - 1]["selecao"]
        time2 = classificacao[grupo2][pos2 - 1]["selecao"]

        jogo = {
            "id_jogo": len(oitavas) + 1,
            "mandante": time1,
            "visitante": time2,
            "gols_mandante": 0,
            "gols_visitante": 0,
            "penaltis_mandante": None,
            "penaltis_visitante": None,
            "finalizado": False,
            "vencedor": None
        }

        oitavas.append(jogo)

    return oitavas



def garantir_fase_final(competicao):
    if "fase_final" not in competicao:
        competicao["fase_final"] = {
            "oitavas": []
        }


def atualizar_placar_oitavas(
    competicao,
    id_jogo,
    gols_mandante,
    gols_visitante,
    penaltis_mandante=None,
    penaltis_visitante=None
):

    if "fase_final" not in competicao:
        raise ValueError("Fase final ainda não criada")

    jogos = competicao["fase_final"].get("oitavas", [])

    jogo = next((j for j in jogos if j.get("id_jogo") == id_jogo), None)

    if not jogo:
        raise ValueError("Jogo não encontrado")

    if gols_mandante < 0 or gols_visitante < 0:
        raise ValueError("Gols não podem ser negativos")

    jogo["gols_mandante"] = gols_mandante
    jogo["gols_visitante"] = gols_visitante

    # Se houver empate no tempo normal
    if gols_mandante == gols_visitante:

        if penaltis_mandante is None or penaltis_visitante is None:
            jogo["finalizado"] = False
            jogo["vencedor"] = None
            return competicao

        if penaltis_mandante == penaltis_visitante:
            raise ValueError("Pênaltis não podem terminar empatados")

        jogo["penaltis_mandante"] = penaltis_mandante
        jogo["penaltis_visitante"] = penaltis_visitante

        jogo["vencedor"] = (
            jogo["mandante"]
            if penaltis_mandante > penaltis_visitante
            else jogo["visitante"]
        )

        jogo["finalizado"] = True

    else:
        # Vitória no tempo normal
        jogo["penaltis_mandante"] = None
        jogo["penaltis_visitante"] = None

        jogo["vencedor"] = (
            jogo["mandante"]
            if gols_mandante > gols_visitante
            else jogo["visitante"]
        )

        jogo["finalizado"] = True

    return competicao
