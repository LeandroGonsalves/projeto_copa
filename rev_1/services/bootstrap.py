"""
Arquivo responsável por montar a estrutura inicial da competição.

Aqui definimos:
- Grupos
- Seleções
- Estrutura base
- Partidas iniciais

Este arquivo pertence à camada de domínio (não HTTP).
"""


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

        # Criamos partidas automaticamente:
        # 1º vs 2º
        # 3º vs 4º
        partidas = [
            {
                "id_partida": 1,
                "time1": selecoes[0],
                "time2": selecoes[1],
                "gols": {selecoes[0]: 0, selecoes[1]: 0},
                "status": "em_andamento"
            },
            {
                "id_partida": 2,
                "time1": selecoes[2],
                "time2": selecoes[3],
                "gols": {selecoes[2]: 0, selecoes[3]: 0},
                "status": "em_andamento"
            }
        ]

        estrutura["grupos"][nome_grupo] = {
            "times": times,
            "partidas": partidas
        }

    return estrutura
