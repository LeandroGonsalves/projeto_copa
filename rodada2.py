from rich import print
from utils import atualiza_pontos, mostrar_pontos, mostra_placares
from pontos_grupos import (
    pontos_grupoA, pontos_grupoB, pontos_grupoC, pontos_grupoD,
    pontos_grupoE, pontos_grupoF, pontos_grupoG, pontos_grupoH
)


def rodada2():
    print("\n--- PLACARES DA 2ª RODADA ---")
    placares = []

    # Grupo A
    gols_dinamarca = int(input("\nDinamarca: "))
    gols_senegal = int(input("Senegal: "))
    atualiza_pontos(pontos_grupoA, 'Dinamarca', gols_dinamarca, 'Senegal', gols_senegal)
    placares.append(("Dinamarca", gols_dinamarca, gols_senegal, "Senegal"))

    gols_franca = int(input("\nFrança: "))
    gols_uruguai = int(input("Uruguai: "))
    atualiza_pontos(pontos_grupoA, 'França', gols_franca, 'Uruguai', gols_uruguai)
    placares.append(("França", gols_franca, gols_uruguai, "Uruguai"))

    # Grupo B
    gols_espanha = int(input("\nEspanha: "))
    gols_paraguai = int(input("Paraguai: "))
    atualiza_pontos(pontos_grupoB, 'Espanha', gols_espanha, 'Paraguai', gols_paraguai)
    placares.append(("Espanha", gols_espanha, gols_paraguai, "Paraguai"))

    gols_africadosul = int(input("\nÁfrica do Sul: "))
    gols_eslovenia = int(input("Eslovênia: "))
    atualiza_pontos(pontos_grupoB, 'África do Sul', gols_africadosul, 'Eslovênia', gols_eslovenia)
    placares.append(("África do Sul", gols_africadosul, gols_eslovenia, "Eslovênia"))

    # Grupo C
    gols_brasil = int(input("\nBrasil: "))
    gols_china = int(input("China: "))
    atualiza_pontos(pontos_grupoC, 'Brasil', gols_brasil, 'China', gols_china)
    placares.append(("Brasil", gols_brasil, gols_china, "China"))

    gols_costarica = int(input("\nCosta Rica: "))
    gols_turquia = int(input("Turquia: "))
    atualiza_pontos(pontos_grupoC, 'Costa Rica', gols_costarica, 'Turquia', gols_turquia)
    placares.append(("Costa Rica", gols_costarica, gols_turquia, "Turquia"))

    # Grupo D
    gols_coreiadosul = int(input("\nCoreia do Sul: "))
    gols_estadosunidos = int(input("Estados Unidos: "))
    atualiza_pontos(pontos_grupoD, 'Coreia do Sul', gols_coreiadosul, 'Estados Unidos', gols_estadosunidos)
    placares.append(("Coreia do Sul", gols_coreiadosul, gols_estadosunidos, "Estados Unidos"))

    gols_portugal = int(input("\nPortugal: "))
    gols_polonia = int(input("Polônia: "))
    atualiza_pontos(pontos_grupoD, 'Portugal', gols_portugal, 'Polônia', gols_polonia)
    placares.append(("Portugal", gols_portugal, gols_polonia, "Polônia"))

    # Grupo E
    gols_alemanha = int(input("\nAlemanha: "))
    gols_irlanda = int(input("Irlanda: "))
    atualiza_pontos(pontos_grupoE, 'Alemanha', gols_alemanha, 'Irlanda', gols_irlanda)
    placares.append(("Alemanha", gols_alemanha, gols_irlanda, "Irlanda"))

    gols_camaroes = int(input("\nCamarões: "))
    gols_arabiasaudita = int(input("Arábia Saudita: "))
    atualiza_pontos(pontos_grupoE, 'Camarões', gols_camaroes, 'Arábia Saudita', gols_arabiasaudita)
    placares.append(("Camarões", gols_camaroes, gols_arabiasaudita, "Arábia Saudita"))

    # Grupo F
    gols_suecia = int(input("\nSuécia: "))
    gols_nigeria = int(input("Nigéria: "))
    atualiza_pontos(pontos_grupoF, 'Suécia', gols_suecia, 'Nigéria', gols_nigeria)
    placares.append(("Suécia", gols_suecia, gols_nigeria, "Nigéria"))

    gols_argentina = int(input("\nArgentina: "))
    gols_inglaterra = int(input("Inglaterra: "))
    atualiza_pontos(pontos_grupoF, 'Argentina', gols_argentina, 'Inglaterra', gols_inglaterra)
    placares.append(("Argentina", gols_argentina, gols_inglaterra, "Inglaterra"))

    # Grupo G
    gols_italia = int(input("\nItália: "))
    gols_croacia = int(input("Croácia: "))
    atualiza_pontos(pontos_grupoG, 'Itália', gols_italia, 'Croácia', gols_croacia)
    placares.append(("Itália", gols_italia, gols_croacia, "Croácia"))

    gols_mexico = int(input("\nMéxico: "))
    gols_equador = int(input("Equador: "))
    atualiza_pontos(pontos_grupoG, 'México', gols_mexico, 'Equador', gols_equador)
    placares.append(("México", gols_mexico, gols_equador, "Equador"))

    # Grupo H
    gols_japao = int(input("\nJapão: "))
    gols_russia = int(input("Rússia: "))
    atualiza_pontos(pontos_grupoH, 'Japão', gols_japao, 'Rússia', gols_russia)
    placares.append(("Japão", gols_japao, gols_russia, "Rússia"))

    gols_belgica = int(input("\nBélgica: "))
    gols_tunisia = int(input("Tunísia: "))
    atualiza_pontos(pontos_grupoH, 'Bélgica', gols_belgica, 'Tunísia', gols_tunisia)
    placares.append(("Bélgica", gols_belgica, gols_tunisia, "Tunísia"))


    mostra_placares(placares)
    mostrar_pontos(pontos_grupoA, "Grupo A")
    mostrar_pontos(pontos_grupoB, "Grupo B")
    mostrar_pontos(pontos_grupoC, "Grupo C")
    mostrar_pontos(pontos_grupoD, "Grupo D")
    mostrar_pontos(pontos_grupoE, "Grupo E")
    mostrar_pontos(pontos_grupoF, "Grupo F")
    mostrar_pontos(pontos_grupoG, "Grupo G")
    mostrar_pontos(pontos_grupoH, "Grupo H")

    return "Final da Segunda Rodada"