from rich import print
from utils import input_gols, atualiza_pontos, mostra_pontos, mostra_placares
from pontos_grupos import (
    pontos_grupoA, pontos_grupoB, pontos_grupoC, pontos_grupoD,
    pontos_grupoE, pontos_grupoF, pontos_grupoG, pontos_grupoH
)


def rodada2():
    print("\n--- PLACARES DA 2ª RODADA ---")
    placares = []

    # Grupo A
    gols_dinamarca = input_gols("Dinamarca")
    gols_senegal = input_gols("Senegal")
    atualiza_pontos(pontos_grupoA, 'Dinamarca', gols_dinamarca, 'Senegal', gols_senegal)
    placares.append(("Dinamarca", gols_dinamarca, gols_senegal, "Senegal"))

    gols_franca = input_gols("França")
    gols_uruguai = input_gols("Uruguai")
    atualiza_pontos(pontos_grupoA, 'França', gols_franca, 'Uruguai', gols_uruguai)
    placares.append(("França", gols_franca, gols_uruguai, "Uruguai"))

    # Grupo B
    gols_espanha = input_gols("Espanha")
    gols_paraguai = input_gols("Paraguai")
    atualiza_pontos(pontos_grupoB, 'Espanha', gols_espanha, 'Paraguai', gols_paraguai)
    placares.append(("Espanha", gols_espanha, gols_paraguai, "Paraguai"))

    gols_africadosul = input_gols("África do Sul")
    gols_eslovenia = input_gols("Eslovênia")
    atualiza_pontos(pontos_grupoB, 'África do Sul', gols_africadosul, 'Eslovênia', gols_eslovenia)
    placares.append(("África do Sul", gols_africadosul, gols_eslovenia, "Eslovênia"))

    # Grupo C
    gols_brasil = input_gols("Brasil")
    gols_china = input_gols("China")
    atualiza_pontos(pontos_grupoC, 'Brasil', gols_brasil, 'China', gols_china)
    placares.append(("Brasil", gols_brasil, gols_china, "China"))

    gols_costarica = input_gols("Costa Rica")
    gols_turquia = input_gols("Turquia")
    atualiza_pontos(pontos_grupoC, 'Costa Rica', gols_costarica, 'Turquia', gols_turquia)
    placares.append(("Costa Rica", gols_costarica, gols_turquia, "Turquia"))

    # Grupo D
    gols_coreiadosul = input_gols("Coreia do Sul")
    gols_estadosunidos = input_gols("Estados Unidos")
    atualiza_pontos(pontos_grupoD, 'Coreia do Sul', gols_coreiadosul, 'Estados Unidos', gols_estadosunidos)
    placares.append(("Coreia do Sul", gols_coreiadosul, gols_estadosunidos, "Estados Unidos"))

    gols_portugal = input_gols("Portugal")
    gols_polonia = input_gols("Polônia")
    atualiza_pontos(pontos_grupoD, 'Portugal', gols_portugal, 'Polônia', gols_polonia)
    placares.append(("Portugal", gols_portugal, gols_polonia, "Polônia"))

    # Grupo E
    gols_alemanha = input_gols("Alemanha")
    gols_irlanda = input_gols("Irlanda")
    atualiza_pontos(pontos_grupoE, 'Alemanha', gols_alemanha, 'Irlanda', gols_irlanda)
    placares.append(("Alemanha", gols_alemanha, gols_irlanda, "Irlanda"))

    gols_camaroes = input_gols("Camarões")
    gols_arabiasaudita = input_gols("Arábia Saudita")
    atualiza_pontos(pontos_grupoE, 'Camarões', gols_camaroes, 'Arábia Saudita', gols_arabiasaudita)
    placares.append(("Camarões", gols_camaroes, gols_arabiasaudita, "Arábia Saudita"))

    # Grupo F
    gols_suecia = input_gols("Suécia")
    gols_nigeria = input_gols("Nigéria")
    atualiza_pontos(pontos_grupoF, 'Suécia', gols_suecia, 'Nigéria', gols_nigeria)
    placares.append(("Suécia", gols_suecia, gols_nigeria, "Nigéria"))

    gols_argentina = input_gols("Argentina")
    gols_inglaterra = input_gols("Inglaterra")
    atualiza_pontos(pontos_grupoF, 'Argentina', gols_argentina, 'Inglaterra', gols_inglaterra)
    placares.append(("Argentina", gols_argentina, gols_inglaterra, "Inglaterra"))

    # Grupo G
    gols_italia = input_gols("Itália")
    gols_croacia = input_gols("Croácia")
    atualiza_pontos(pontos_grupoG, 'Itália', gols_italia, 'Croácia', gols_croacia)
    placares.append(("Itália", gols_italia, gols_croacia, "Croácia"))

    gols_mexico = input_gols("México")
    gols_equador = input_gols("Equador")
    atualiza_pontos(pontos_grupoG, 'México', gols_mexico, 'Equador', gols_equador)
    placares.append(("México", gols_mexico, gols_equador, "Equador"))

    # Grupo H
    gols_japao = input_gols("Japão")
    gols_russia = input_gols("Rússia")
    atualiza_pontos(pontos_grupoH, 'Japão', gols_japao, 'Rússia', gols_russia)
    placares.append(("Japão", gols_japao, gols_russia, "Rússia"))

    gols_belgica = input_gols("Bélgica")
    gols_tunisia = input_gols("Tunísia")
    atualiza_pontos(pontos_grupoH, 'Bélgica', gols_belgica, 'Tunísia', gols_tunisia)
    placares.append(("Bélgica", gols_belgica, gols_tunisia, "Tunísia"))


    mostra_placares(placares)
    mostra_pontos(pontos_grupoA, "Grupo A")
    mostra_pontos(pontos_grupoB, "Grupo B")
    mostra_pontos(pontos_grupoC, "Grupo C")
    mostra_pontos(pontos_grupoD, "Grupo D")
    mostra_pontos(pontos_grupoE, "Grupo E")
    mostra_pontos(pontos_grupoF, "Grupo F")
    mostra_pontos(pontos_grupoG, "Grupo G")
    mostra_pontos(pontos_grupoH, "Grupo H")

    return "Final da Segunda Rodada"