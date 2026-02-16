def criar_estrutura_inicial():
    """
    Monta toda a estrutura base da competição.

    Retorna:
        dict: estrutura completa da copa
    """

    grupos = {
        "A": ["França", "Senegal", "Uruguai", "Dinamarca"],
        "B": ["Espanha", "Paraguai", "África do Sul", "Eslovênia"],
        "C": ["Brasil", "Turquia", "Costa Rica", "China"],
        "D": ["Coreia do Sul", "Estados Unidos", "Portugal", "Polônia"],
        "E": ["Alemanha", "Irlanda", "Camarões", "Arábia Saudita"],
        "F": ["Suécia", "Inglaterra", "Argentina", "Nigéria"],
        "G": ["México", "Itália", "Croácia", "Equador"],
        "H": ["Japão", "Bélgica", "Rússia", "Tunísia"]
    }

    estrutura = {"grupos": {}}

    # Percorre cada grupo dinamicamente
    for nome_grupo, selecoes in grupos.items():

        # Cria estrutura de times zerados
        times = {
            selecao: {"pontos": 0, "gm": 0, "gs": 0}
            for selecao in selecoes
        }

        partidas = [
            # Rodada 1
            {
                "id_partida": 1,
                "rodada": 1,
                "time1": selecoes[0],
                "time2": selecoes[1],
                "gols": None,
                "status": "nao_iniciado"
            },
            {
                "id_partida": 2,
                "rodada": 1,
                "time1": selecoes[2],
                "time2": selecoes[3],
                "gols": None,
                "status": "nao_iniciado"
            },

            # Rodada 2
            {
                "id_partida": 3,
                "rodada": 2,
                "time1": selecoes[0],
                "time2": selecoes[2],
                "gols": None,
                "status": "nao_iniciado"
            },
            {
                "id_partida": 4,
                "rodada": 2,
                "time1": selecoes[1],
                "time2": selecoes[3],
                "gols": None,
                "status": "nao_iniciado"
            },

            # Rodada 3
            {
                "id_partida": 5,
                "rodada": 3,
                "time1": selecoes[0],
                "time2": selecoes[3],
                "gols": None,
                "status": "nao_iniciado"
            },
            {
                "id_partida": 6,
                "rodada": 3,
                "time1": selecoes[1],
                "time2": selecoes[2],
                "gols": None,
                "status": "nao_iniciado"
            }
        ]

        estrutura["grupos"][nome_grupo] = {
            "times": times,
            "partidas": partidas
        }

    return estrutura
