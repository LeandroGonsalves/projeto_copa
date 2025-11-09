from rich import print
from utils import atualiza_pontos, mostrar_pontos, mostra_placares
from pontos_grupos import (
    pontos_grupoA, pontos_grupoB, pontos_grupoC, pontos_grupoD,
    pontos_grupoE, pontos_grupoF, pontos_grupoG, pontos_grupoH
)


def rodada1():
    print(f"\n--- PLACARES DA 1ª RODADA ---")
    placares = []

    # Grupo A
    gols_franca = int(input("França: "))
    gols_senegal = int(input("Senegal: "))
    atualiza_pontos(pontos_grupoA, 'França', gols_franca, 'Senegal', gols_senegal)
    placares.append(("França", gols_franca, gols_senegal, "Senegal"))

    gols_uruguai = int(input("\nUruguai: "))
    gols_dinamarca = int(input("Dinamarca: "))
    atualiza_pontos(pontos_grupoA, 'Uruguai', gols_uruguai, 'Dinamarca', gols_dinamarca)
    placares.append(("Uruguai", gols_uruguai, gols_dinamarca, "Dinamarca"))
    

    # Grupo B
    gols_paraguai = int(input("\nParaguai: "))
    gols_africadosul = int(input("África do Sul: "))
    atualiza_pontos(pontos_grupoB, 'Paraguai', gols_paraguai, 'África do Sul', gols_africadosul)
    placares.append(("Paraguai", gols_paraguai, gols_africadosul, "África do Sul"))
    
    gols_espanha = int(input("\nEspanha: "))
    gols_eslovenia = int(input("Eslovênia: "))
    atualiza_pontos(pontos_grupoB, 'Espanha', gols_espanha, 'Eslovênia', gols_eslovenia)
    placares.append(("Espanha", gols_espanha, gols_eslovenia, "Eslovênia"))
    

    # Grupo C
    gols_brasil = int(input("\nBrasil: "))
    gols_turquia = int(input("Turquia: "))
    atualiza_pontos(pontos_grupoC, 'Brasil', gols_brasil, 'Turquia', gols_turquia)
    placares.append(("Brasil", gols_brasil, gols_turquia, "Turquia"))
        
    gols_china = int(input("\nChina: "))
    gols_costarica = int(input("Costa Rica: "))
    atualiza_pontos(pontos_grupoC, 'China', gols_china, 'Costa Rica', gols_costarica)
    placares.append(("China", gols_china, gols_costarica, "Costa Rica"))
    

    # Grupo D
    gols_coreiadosul = int(input("\nCoreia do Sul: "))
    gols_polonia = int(input("Polônia: "))
    atualiza_pontos(pontos_grupoD, 'Coreia do Sul', gols_coreiadosul, 'Polônia', gols_polonia)
    placares.append(("Polônia", gols_polonia, gols_coreiadosul, "Coreia do Sul"))
    
    gols_estadosunidos = int(input("\nEstados Unidos: "))
    gols_portugal = int(input("Portugal: "))
    atualiza_pontos(pontos_grupoD, 'Estados Unidos', gols_estadosunidos, 'Portugal', gols_portugal)
    placares.append(("Estados Unidos", gols_estadosunidos, gols_portugal, "Portugal"))
    

    # Grupo E
    gols_irlanda = int(input("\nIrlanda: "))
    gols_camaroes = int(input("Camarões: "))
    atualiza_pontos(pontos_grupoE, 'Irlanda', gols_irlanda, 'Camarões', gols_camaroes)
    placares.append(("Irlanda", gols_irlanda, gols_camaroes, "Camarões"))
    
    gols_alemanha = int(input("\nAlemanha: "))
    gols_arabiasaudita = int(input("Arábia Saudita: "))
    atualiza_pontos(pontos_grupoE, 'Alemanha', gols_alemanha, 'Arábia Saudita', gols_arabiasaudita)
    placares.append(("Alemanha", gols_alemanha, gols_arabiasaudita, "Arábia Saudita"))
    

    # Grupo F
    gols_argentina = int(input("\nArgentina: "))
    gols_nigeria = int(input("Nigéria: "))
    atualiza_pontos(pontos_grupoF, 'Argentina', gols_argentina, 'Nigéria', gols_nigeria)
    placares.append(("Argentina", gols_argentina, gols_nigeria, "Nigéria"))


    gols_suecia = int(input("\nSuécia: "))
    gols_inglaterra = int(input("Inglaterra: "))
    atualiza_pontos(pontos_grupoF, 'Suécia', gols_suecia, 'Inglaterra', gols_inglaterra)
    placares.append(("Suécia", gols_suecia, gols_inglaterra, "Inglaterra"))
    

    # Grupo G
    gols_croacia = int(input("\nCroácia: "))
    gols_mexico = int(input("México: "))
    atualiza_pontos(pontos_grupoG, 'Croácia', gols_croacia, 'México', gols_mexico)
    placares.append(("Croácia", gols_croacia, gols_mexico, "México"))
    
    gols_italia = int(input("\nItália: "))
    gols_equador = int(input("Equador: "))
    atualiza_pontos(pontos_grupoG, 'Itália', gols_italia, 'Equador', gols_equador)
    placares.append(("Itália", gols_italia, gols_equador, "Equador"))
    

    # Grupo H
    gols_japao = int(input("\nJapão: "))
    gols_belgica = int(input("Bélgica: "))
    atualiza_pontos(pontos_grupoH, 'Japão', gols_japao, 'Bélgica', gols_belgica)
    placares.append(("Japão", gols_japao, gols_belgica, "Bélgica"))
    
    gols_russia = int(input("\nRússia: "))
    gols_tunisia = int(input("Tunísia: "))
    atualiza_pontos(pontos_grupoH, 'Rússia', gols_russia, 'Tunísia', gols_tunisia)
    placares.append(("Rússia", gols_russia, gols_tunisia, "Tunísia"))


    mostra_placares(placares)
    mostrar_pontos(pontos_grupoA, "Grupo A")
    mostrar_pontos(pontos_grupoB, "Grupo B")
    mostrar_pontos(pontos_grupoC, "Grupo C")
    mostrar_pontos(pontos_grupoD, "Grupo D")
    mostrar_pontos(pontos_grupoE, "Grupo E")
    mostrar_pontos(pontos_grupoF, "Grupo F")
    mostrar_pontos(pontos_grupoG, "Grupo G")
    mostrar_pontos(pontos_grupoH, "Grupo H")

    return "Final da Primeira Rodada"