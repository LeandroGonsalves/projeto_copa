from rich import print
from utils import atualiza_pontos, mostrar_pontos, mostra_placares
from pontos_grupos import (
    pontos_grupoA, pontos_grupoB, pontos_grupoC, pontos_grupoD,
    pontos_grupoE, pontos_grupoF, pontos_grupoG, pontos_grupoH
)


def rodada3():
    print("\n--- PLACARES DA 3ª RODADA ---")
    placares = []

    # Grupo A
    gols_dinamarca = int(input("\nDinamarca: "))
    gols_franca = int(input("França: "))
    atualiza_pontos(pontos_grupoA, 'Dinamarca', gols_dinamarca, 'França', gols_franca)
    placares.append(("Dinamarca", gols_dinamarca, gols_franca, "França"))

    gols_senegal = int(input("\nSenegal: "))
    gols_uruguai = int(input("Uruguai: "))
    atualiza_pontos(pontos_grupoA, 'Senegal', gols_senegal, 'Uruguai', gols_uruguai)
    placares.append(("Senegal", gols_senegal, gols_uruguai, "Uruguai"))

    # Grupo B
    gols_africadosul = int(input("\nÁfrica do Sul: "))
    gols_espanha = int(input("Espanha: "))
    atualiza_pontos(pontos_grupoB, 'África do Sul', gols_africadosul, 'Espanha', gols_espanha)
    placares.append(("África do Sul", gols_africadosul, gols_espanha, "Espanha"))

    gols_eslovenia = int(input("\nEslovênia: "))
    gols_paraguai = int(input("Paraguai: "))
    atualiza_pontos(pontos_grupoB, 'Eslovênia', gols_eslovenia, 'Paraguai', gols_paraguai)
    placares.append(("Eslovênia", gols_eslovenia, gols_paraguai, "Paraguai"))

    # Grupo C
    gols_costarica = int(input("\nCosta Rica: "))
    gols_brasil = int(input("Brasil: "))
    atualiza_pontos(pontos_grupoC, 'Costa Rica', gols_costarica, 'Brasil', gols_brasil)
    placares.append(("Costa Rica", gols_costarica, gols_brasil, "Brasil"))

    gols_turquia = int(input("\nTurquia: "))
    gols_china = int(input("China: "))
    atualiza_pontos(pontos_grupoC, 'Turquia', gols_turquia, 'China', gols_china)
    placares.append(("Turquia", gols_turquia, gols_china, "China"))

    # Grupo D
    gols_portugal = int(input("\nPortugal: "))
    gols_coreiadosul = int(input("Coreia do Sul: "))
    atualiza_pontos(pontos_grupoD, 'Portugal', gols_portugal, 'Coreia do Sul', gols_coreiadosul)
    placares.append(("Portugal", gols_portugal, gols_coreiadosul, "Coreia do Sul"))

    gols_polonia = int(input("\nPolônia: "))
    gols_estadosunidos = int(input("Estados Unidos: "))
    atualiza_pontos(pontos_grupoD, 'Polônia', gols_polonia, 'Estados Unidos', gols_estadosunidos)
    placares.append(("Polônia", gols_polonia, gols_estadosunidos, "Estados Unidos"))

    # Grupo E
    gols_camaroes = int(input("\nCamarões: "))
    gols_alemanha = int(input("Alemanha: "))
    atualiza_pontos(pontos_grupoE, 'Camarões', gols_camaroes, 'Alemanha', gols_alemanha)
    placares.append(("Camarões", gols_camaroes, gols_alemanha, "Alemanha"))

    gols_arabiasaudita = int(input("\nArábia Saudita: "))
    gols_irlanda = int(input("Irlanda: "))
    atualiza_pontos(pontos_grupoE, 'Arábia Saudita', gols_arabiasaudita, 'Irlanda', gols_irlanda)
    placares.append(("Arábia Saudita", gols_arabiasaudita, gols_irlanda, "Irlanda"))

    # Grupo F
    gols_nigeria = int(input("\nNigéria: "))
    gols_inglaterra = int(input("Inglaterra: "))
    atualiza_pontos(pontos_grupoF, 'Nigéria', gols_nigeria, 'Inglaterra', gols_inglaterra)
    placares.append(("Nigéria", gols_nigeria, gols_inglaterra, "Inglaterra"))

    gols_suecia = int(input("\nSuécia: "))
    gols_argentina = int(input("Argentina: "))
    atualiza_pontos(pontos_grupoF, 'Suécia', gols_suecia, 'Argentina', gols_argentina)
    placares.append(("Suécia", gols_suecia, gols_argentina, "Argentina"))

    # Grupo G
    gols_equador = int(input("\nEquador: "))
    gols_croacia = int(input("Croácia: "))
    atualiza_pontos(pontos_grupoG, 'Equador', gols_equador, 'Croácia', gols_croacia)
    placares.append(("Equador", gols_equador, gols_croacia, "Croácia"))

    gols_mexico = int(input("\nMéxico: "))
    gols_italia = int(input("Itália: "))
    atualiza_pontos(pontos_grupoG, 'México', gols_mexico, 'Itália', gols_italia)
    placares.append(("México", gols_mexico, gols_italia, "Itália"))

    # Grupo H
    gols_tunisia = int(input("\nTunísia: "))
    gols_japao = int(input("Japão: "))
    atualiza_pontos(pontos_grupoH, 'Tunísia', gols_tunisia, 'Japão', gols_japao)
    placares.append(("Tunísia", gols_tunisia, gols_japao, "Japão"))

    gols_belgica = int(input("\nBélgica: "))
    gols_russia = int(input("Rússia: "))
    atualiza_pontos(pontos_grupoH, 'Bélgica', gols_belgica, 'Rússia', gols_russia)
    placares.append(("Bélgica", gols_belgica, gols_russia, "Rússia"))


    mostra_placares(placares)

    print("\n\n--- PONTUAÇÃO FINAL ---")
    mostrar_pontos(pontos_grupoA, "Grupo A")
    mostrar_pontos(pontos_grupoB, "Grupo B")
    mostrar_pontos(pontos_grupoC, "Grupo C")
    mostrar_pontos(pontos_grupoD, "Grupo D")
    mostrar_pontos(pontos_grupoE, "Grupo E")
    mostrar_pontos(pontos_grupoF, "Grupo F")
    mostrar_pontos(pontos_grupoG, "Grupo G")
    mostrar_pontos(pontos_grupoH, "Grupo H")

    return "Final da Terceira Rodada"