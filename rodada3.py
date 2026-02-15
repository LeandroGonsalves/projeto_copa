from rich import print
from utils import input_gols, atualiza_pontos, mostra_pontos, mostra_placares
from pontos_grupos import (
    pontos_grupoA, pontos_grupoB, pontos_grupoC, pontos_grupoD,
    pontos_grupoE, pontos_grupoF, pontos_grupoG, pontos_grupoH
)


def rodada3():
    print("\n--- PLACARES DA 3ª RODADA ---")
    placares = []

    # Grupo A
    gols_dinamarca = input_gols("Dinamarca")
    gols_franca = input_gols("França")
    atualiza_pontos(pontos_grupoA, 'Dinamarca', gols_dinamarca, 'França', gols_franca)
    placares.append(("Dinamarca", gols_dinamarca, gols_franca, "França"))

    gols_senegal = input_gols("Senegal")
    gols_uruguai = input_gols("Uruguai")
    atualiza_pontos(pontos_grupoA, 'Senegal', gols_senegal, 'Uruguai', gols_uruguai)
    placares.append(("Senegal", gols_senegal, gols_uruguai, "Uruguai"))

    # Grupo B
    gols_africadosul = input_gols("África do Sul")
    gols_espanha = input_gols("Espanha")
    atualiza_pontos(pontos_grupoB, 'África do Sul', gols_africadosul, 'Espanha', gols_espanha)
    placares.append(("África do Sul", gols_africadosul, gols_espanha, "Espanha"))

    gols_eslovenia = input_gols("Eslovênia")
    gols_paraguai = input_gols("Paraguai")
    atualiza_pontos(pontos_grupoB, 'Eslovênia', gols_eslovenia, 'Paraguai', gols_paraguai)
    placares.append(("Eslovênia", gols_eslovenia, gols_paraguai, "Paraguai"))

    # Grupo C
    gols_costarica = input_gols("Costa Rica")
    gols_brasil = input_gols("Brasil")
    atualiza_pontos(pontos_grupoC, 'Costa Rica', gols_costarica, 'Brasil', gols_brasil)
    placares.append(("Costa Rica", gols_costarica, gols_brasil, "Brasil"))

    gols_turquia = input_gols("Turquia")
    gols_china = input_gols("China")
    atualiza_pontos(pontos_grupoC, 'Turquia', gols_turquia, 'China', gols_china)
    placares.append(("Turquia", gols_turquia, gols_china, "China"))

    # Grupo D
    gols_portugal = input_gols("Portugal")
    gols_coreiadosul = input_gols("Coreia do Sul")
    atualiza_pontos(pontos_grupoD, 'Portugal', gols_portugal, 'Coreia do Sul', gols_coreiadosul)
    placares.append(("Portugal", gols_portugal, gols_coreiadosul, "Coreia do Sul"))

    gols_polonia = input_gols("Polônia")
    gols_estadosunidos = input_gols("Estados Unidos")
    atualiza_pontos(pontos_grupoD, 'Polônia', gols_polonia, 'Estados Unidos', gols_estadosunidos)
    placares.append(("Polônia", gols_polonia, gols_estadosunidos, "Estados Unidos"))

    # Grupo E
    gols_camaroes = input_gols("Camarões")
    gols_alemanha = input_gols("Alemanha")
    atualiza_pontos(pontos_grupoE, 'Camarões', gols_camaroes, 'Alemanha', gols_alemanha)
    placares.append(("Camarões", gols_camaroes, gols_alemanha, "Alemanha"))

    gols_arabiasaudita = input_gols("Arábia Saudita")
    gols_irlanda = input_gols("Irlanda")
    atualiza_pontos(pontos_grupoE, 'Arábia Saudita', gols_arabiasaudita, 'Irlanda', gols_irlanda)
    placares.append(("Arábia Saudita", gols_arabiasaudita, gols_irlanda, "Irlanda"))

    # Grupo F
    gols_nigeria = input_gols("Nigéria")
    gols_inglaterra = input_gols("Inglaterra")
    atualiza_pontos(pontos_grupoF, 'Nigéria', gols_nigeria, 'Inglaterra', gols_inglaterra)
    placares.append(("Nigéria", gols_nigeria, gols_inglaterra, "Inglaterra"))

    gols_suecia = input_gols("Suécia")
    gols_argentina = input_gols("Argentina")
    atualiza_pontos(pontos_grupoF, 'Suécia', gols_suecia, 'Argentina', gols_argentina)
    placares.append(("Suécia", gols_suecia, gols_argentina, "Argentina"))

    # Grupo G
    gols_equador = input_gols("Equador")
    gols_croacia = input_gols("Croácia")
    atualiza_pontos(pontos_grupoG, 'Equador', gols_equador, 'Croácia', gols_croacia)
    placares.append(("Equador", gols_equador, gols_croacia, "Croácia"))

    gols_mexico = input_gols("México")
    gols_italia = input_gols("Itália")
    atualiza_pontos(pontos_grupoG, 'México', gols_mexico, 'Itália', gols_italia)
    placares.append(("México", gols_mexico, gols_italia, "Itália"))

    # Grupo H
    gols_tunisia = input_gols("Tunísia")
    gols_japao = input_gols("Japão")
    atualiza_pontos(pontos_grupoH, 'Tunísia', gols_tunisia, 'Japão', gols_japao)
    placares.append(("Tunísia", gols_tunisia, gols_japao, "Japão"))

    gols_belgica = input_gols("Bélgica")
    gols_russia = input_gols("Rússia")
    atualiza_pontos(pontos_grupoH, 'Bélgica', gols_belgica, 'Rússia', gols_russia)
    placares.append(("Bélgica", gols_belgica, gols_russia, "Rússia"))


    mostra_placares(placares)

    print("\n\n--- PONTUAÇÃO FINAL ---")
    mostra_pontos(pontos_grupoA, "Grupo A")
    mostra_pontos(pontos_grupoB, "Grupo B")
    mostra_pontos(pontos_grupoC, "Grupo C")
    mostra_pontos(pontos_grupoD, "Grupo D")
    mostra_pontos(pontos_grupoE, "Grupo E")
    mostra_pontos(pontos_grupoF, "Grupo F")
    mostra_pontos(pontos_grupoG, "Grupo G")
    mostra_pontos(pontos_grupoH, "Grupo H")

    return "Final da Terceira Rodada"