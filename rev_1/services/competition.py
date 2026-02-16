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
