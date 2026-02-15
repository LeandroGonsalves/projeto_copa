from rich import print
from utils import input_gols, atualiza_pontos, mostra_pontos, mostra_placares
from pontos_grupos import (
    pontos_grupoA, pontos_grupoB, pontos_grupoC, pontos_grupoD,
    pontos_grupoE, pontos_grupoF, pontos_grupoG, pontos_grupoH
)


def rodada1():
    print(f"\n--- PLACARES DA 1ª RODADA ---")
    placares = []

    # Grupo A
    gols_franca = input_gols("França")
    gols_senegal = input_gols("Senegal")
    atualiza_pontos(pontos_grupoA, 'França', gols_franca, 'Senegal', gols_senegal)
    placares.append(("França", gols_franca, gols_senegal, "Senegal"))

    gols_uruguai = input_gols("Uruguai")
    gols_dinamarca = input_gols("Dinamarca")
    atualiza_pontos(pontos_grupoA, 'Uruguai', gols_uruguai, 'Dinamarca', gols_dinamarca)
    placares.append(("Uruguai", gols_uruguai, gols_dinamarca, "Dinamarca"))
    

    # Grupo B
    gols_paraguai = input_gols("Paraguai")
    gols_africadosul = input_gols("África do Sul")
    atualiza_pontos(pontos_grupoB, 'Paraguai', gols_paraguai, 'África do Sul', gols_africadosul)
    placares.append(("Paraguai", gols_paraguai, gols_africadosul, "África do Sul"))
    
    gols_espanha = input_gols("Espanha")
    gols_eslovenia = input_gols("Eslovênia")
    atualiza_pontos(pontos_grupoB, 'Espanha', gols_espanha, 'Eslovênia', gols_eslovenia)
    placares.append(("Espanha", gols_espanha, gols_eslovenia, "Eslovênia"))
    

    # Grupo C
    gols_brasil = input_gols("Brasil")
    gols_turquia = input_gols("Turquia")
    atualiza_pontos(pontos_grupoC, 'Brasil', gols_brasil, 'Turquia', gols_turquia)
    placares.append(("Brasil", gols_brasil, gols_turquia, "Turquia"))
        
    gols_china = input_gols("China")
    gols_costarica = input_gols("Costa Rica")
    atualiza_pontos(pontos_grupoC, 'China', gols_china, 'Costa Rica', gols_costarica)
    placares.append(("China", gols_china, gols_costarica, "Costa Rica"))
    

    # Grupo D
    gols_coreiadosul = input_gols("Coreia do Sul")
    gols_polonia = input_gols("Polônia")
    atualiza_pontos(pontos_grupoD, 'Coreia do Sul', gols_coreiadosul, 'Polônia', gols_polonia)
    placares.append(("Polônia", gols_polonia, gols_coreiadosul, "Coreia do Sul"))
    
    gols_estadosunidos = input_gols("Estados Unidos")
    gols_portugal = input_gols("Portugal")
    atualiza_pontos(pontos_grupoD, 'Estados Unidos', gols_estadosunidos, 'Portugal', gols_portugal)
    placares.append(("Estados Unidos", gols_estadosunidos, gols_portugal, "Portugal"))
    

    # Grupo E
    gols_irlanda = input_gols("Irlanda")
    gols_camaroes = input_gols("Camarões")
    atualiza_pontos(pontos_grupoE, 'Irlanda', gols_irlanda, 'Camarões', gols_camaroes)
    placares.append(("Irlanda", gols_irlanda, gols_camaroes, "Camarões"))
    
    gols_alemanha = input_gols("Alemanha")
    gols_arabiasaudita = input_gols("Arábia Saudita")
    atualiza_pontos(pontos_grupoE, 'Alemanha', gols_alemanha, 'Arábia Saudita', gols_arabiasaudita)
    placares.append(("Alemanha", gols_alemanha, gols_arabiasaudita, "Arábia Saudita"))
    

    # Grupo F
    gols_argentina = input_gols("Argentina")
    gols_nigeria = input_gols("Nigéria")
    atualiza_pontos(pontos_grupoF, 'Argentina', gols_argentina, 'Nigéria', gols_nigeria)
    placares.append(("Argentina", gols_argentina, gols_nigeria, "Nigéria"))


    gols_suecia = input_gols("Suécia")
    gols_inglaterra = input_gols("Inglaterra")
    atualiza_pontos(pontos_grupoF, 'Suécia', gols_suecia, 'Inglaterra', gols_inglaterra)
    placares.append(("Suécia", gols_suecia, gols_inglaterra, "Inglaterra"))
    

    # Grupo G
    gols_croacia = input_gols("Croácia")
    gols_mexico = input_gols("México")
    atualiza_pontos(pontos_grupoG, 'Croácia', gols_croacia, 'México', gols_mexico)
    placares.append(("Croácia", gols_croacia, gols_mexico, "México"))
    
    gols_italia = input_gols("Itália")
    gols_equador = input_gols("Equador")
    atualiza_pontos(pontos_grupoG, 'Itália', gols_italia, 'Equador', gols_equador)
    placares.append(("Itália", gols_italia, gols_equador, "Equador"))
    

    # Grupo H
    gols_japao = input_gols("Japão")
    gols_belgica = input_gols("Bélgica")
    atualiza_pontos(pontos_grupoH, 'Japão', gols_japao, 'Bélgica', gols_belgica)
    placares.append(("Japão", gols_japao, gols_belgica, "Bélgica"))
    
    gols_russia = input_gols("Rússia")
    gols_tunisia = input_gols("Tunísia")
    atualiza_pontos(pontos_grupoH, 'Rússia', gols_russia, 'Tunísia', gols_tunisia)
    placares.append(("Rússia", gols_russia, gols_tunisia, "Tunísia"))


    mostra_placares(placares)
    mostra_pontos(pontos_grupoA, "Grupo A")
    mostra_pontos(pontos_grupoB, "Grupo B")
    mostra_pontos(pontos_grupoC, "Grupo C")
    mostra_pontos(pontos_grupoD, "Grupo D")
    mostra_pontos(pontos_grupoE, "Grupo E")
    mostra_pontos(pontos_grupoF, "Grupo F")
    mostra_pontos(pontos_grupoG, "Grupo G")
    mostra_pontos(pontos_grupoH, "Grupo H")

    return "Final da Primeira Rodada"