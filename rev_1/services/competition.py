"""
Este arquivo contém exclusivamente as regras da competição. Ele é responsável por:
- Atualizar gols de uma partida
- Recalcular estatísticas dos times
- Garantir que o estado fique sempre consistente

Importante:
Aqui NÃO existe nada de Flask, HTTP nem CSV. Apenas regra de negócio.
"""


def registrar_gol(competicao, grupo, id_partida, selecao):
    """
    Esta função recebe:
    - competicao (dicionário completo carregado do CSV)
    - grupo (ex: "A")
    - id_partida (ex: 1)
    - selecao (ex: "França")

    Ela:
    - Atualiza o placar da partida
    - Recalcula todos os pontos do grupo
    """

    # Acessa o grupo dentro da competição
    grupo_data = competicao["grupos"][grupo]

    # Percorre as partidas do grupo
    for partida in grupo_data["partidas"]:

        # Encontra a partida correta pelo ID
        if partida["id_partida"] == id_partida:

            # Incrementa 1 gol para a seleção informada
            partida["gols"][selecao] += 1

            break

    # Após atualizar o gol, recalculamos toda a tabela
    recalcular_tabela(grupo_data)

    return competicao


def recalcular_tabela(grupo_data):
    """
    Recalcula do zero:

    - Pontos
    - Gols marcados (gm)
    - Gols sofridos (gs)

    Isso garante consistência total.
    """

    # Primeiro zeramos todos os times
    for time in grupo_data["times"].values():
        time["pontos"] = 0
        time["gm"] = 0
        time["gs"] = 0

    # Depois percorremos todas as partidas
    for partida in grupo_data["partidas"]:

        time1 = partida["time1"]
        time2 = partida["time2"]

        gols1 = partida["gols"][time1]
        gols2 = partida["gols"][time2]

        # Atualiza gols marcados e sofridos
        grupo_data["times"][time1]["gm"] += gols1
        grupo_data["times"][time1]["gs"] += gols2

        grupo_data["times"][time2]["gm"] += gols2
        grupo_data["times"][time2]["gs"] += gols1

        # Atualiza pontos
        if gols1 > gols2:
            grupo_data["times"][time1]["pontos"] += 3
        elif gols2 > gols1:
            grupo_data["times"][time2]["pontos"] += 3
        else:
            grupo_data["times"][time1]["pontos"] += 1
            grupo_data["times"][time2]["pontos"] += 1


def atualizar_placar(competicao, grupo, id_partida, novo_placar):
    grupo_data = competicao["grupos"][grupo]

    for partida in grupo_data["partidas"]:
        if partida["id_partida"] == id_partida:

            partida["gols"] = novo_placar

            break

    recalcular_tabela(grupo_data)

    return competicao


def gerar_classificacao(competicao):
    """
    Recebe o dicionário da competição.
    
    Percorre todos os grupos e:
    - Calcula saldo
    - Ordena os times
    - Retorna classificação organizada
    """

    resultado = {}

    # Percorre cada grupo da competição
    for nome_grupo, dados_grupo in competicao["grupos"].items():

        tabela = []

        # Percorre cada time do grupo
        for nome_time, stats in dados_grupo["times"].items():

            saldo = stats["gm"] - stats["gs"]

            tabela.append({
                "selecao": nome_time,
                "pontos": stats["pontos"],
                "gm": stats["gm"],
                "gs": stats["gs"],
                "saldo": saldo
            })

        # Ordena segundo critérios oficiais
        tabela_ordenada = sorted(
            tabela,
            key=lambda x: (
                x["pontos"],
                x["saldo"],
                x["gm"]
            ),
            reverse=True
        )

        resultado[nome_grupo] = tabela_ordenada

    return resultado
