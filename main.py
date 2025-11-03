from rich import print


pontos_grupoA = {'França': 0, 'Senegal': 0, 'Uruguai': 0, 'Dinamarca': 0}
pontos_grupoB = {'Espanha': 0, 'Paraguai': 0, 'África do Sul': 0, 'Eslovênia': 0}
pontos_grupoC = {'Brasil': 0, 'Turquia': 0, 'Costa Rica': 0, 'China': 0}
pontos_grupoD = {'Coreia do Sul': 0, 'Estados Unidos': 0, 'Portugal': 0, 'Polônia': 0}
pontos_grupoE = {'Alemanha': 0, 'Irlanda': 0, 'Camarões': 0, 'Arábia Saudita': 0}
pontos_grupoF = {'Suécia': 0, 'Inglaterra': 0, 'Argentina': 0, 'Nigéria': 0}
pontos_grupoG = {'México': 0, 'Itália': 0, 'Croácia': 0, 'Equador': 0}
pontos_grupoH = {'Japão': 0, 'Bélgica': 0, 'Rússia': 0, 'Tunísia': 0}


def rodada1():
    # Grupo A
    gols_franca = 0
    gols_senegal = 1
    gols_uruguai = 1
    gols_dinamarca = 2

    # Grupo B
    gols_paraguai = 2
    gols_africadosul = 2
    gols_espanha = 3
    gols_eslovenia = 1

    # Grupo C
    gols_brasil = 2
    gols_turquia = 1
    gols_costarica = 2
    gols_china = 0

    # Grupo D
    gols_coreiadosul = 2
    gols_polonia = 0
    gols_estadosunidos = 3
    gols_portugal = 2

    # Grupo E
    gols_alemanha = 8
    gols_arabiasaudita = 0
    gols_irlanda = 1
    gols_camaroes = 1

    # Grupo F
    gols_suecia = 1
    gols_inglaterra = 1
    gols_argentina = 1
    gols_nigeria = 0

    # Grupo G
    gols_mexico = 1
    gols_croacia = 0
    gols_italia = 2
    gols_equador = 0

    # Grupo H
    gols_japao = 2
    gols_belgica = 2
    gols_russia = 2
    gols_tunisia = 0


    print(f"\nPlacares da 1ª rodada:\
            \nFrança {gols_franca} x {gols_senegal} Senegal\
            \nUruguai {gols_uruguai} x {gols_dinamarca} Dinamarca\
            \nParaguai {gols_paraguai} x {gols_africadosul} África do Sul\
            \nEspanha {gols_espanha} x {gols_eslovenia} Eslovênia\
            \nBrasil {gols_brasil} x {gols_turquia} Turquia\
            \nCosta Rica {gols_costarica} x {gols_china} China\
            \nCoreia do Sul {gols_coreiadosul} x {gols_polonia} Polônia\
            \nEstados Unidos {gols_estadosunidos} x {gols_portugal} Portugal\
            \nAlemanha {gols_alemanha} x {gols_arabiasaudita} Arábia Saudita\
            \nIrlanda {gols_irlanda} x {gols_camaroes} Camarões\
            \nSuécia {gols_suecia} x {gols_inglaterra} Inglaterra\
            \nArgentina {gols_argentina} x {gols_nigeria} Nigéria\
            \nMéxico {gols_mexico} x {gols_croacia} Croácia\
            \nItália {gols_italia} x {gols_equador} Equador\
            \nJapão {gols_japao} x {gols_belgica} Bélgica\
            \nRússia {gols_russia} x {gols_tunisia} Tunísia\n")


    def francaXsenegal(gols_franca, gols_senegal):
        pontos_franca = 0
        pontos_senegal = 0

        if gols_franca > gols_senegal:
            pontos_franca += 3
        elif gols_franca < gols_senegal:
            pontos_senegal += 3
        else :
            pontos_franca += 1
            pontos_senegal += 1

        pontos_grupoA['França'] += pontos_franca
        pontos_grupoA['Senegal'] += pontos_senegal

        return pontos_franca, pontos_senegal


    def uruguaiXdinamarca(gols_uruguai, gols_dinamarca):
        pontos_uruguai = 0
        pontos_dinamarca = 0

        if gols_uruguai > gols_dinamarca:
            pontos_uruguai += 3
        elif gols_uruguai < gols_dinamarca:
            pontos_dinamarca += 3
        else :
            pontos_uruguai += 1
            pontos_dinamarca += 1

        pontos_grupoA['Uruguai'] += pontos_uruguai
        pontos_grupoA['Dinamarca'] += pontos_dinamarca

        return pontos_uruguai, pontos_dinamarca


    def paraguaiXafricadosul(gols_paraguai, gols_africadosul):
        pontos_paraguai = 0
        pontos_africadosul = 0

        if gols_paraguai > gols_africadosul:
            pontos_paraguai += 3
        elif gols_paraguai < gols_africadosul:
            pontos_africadosul += 3
        else :
            pontos_paraguai += 1
            pontos_africadosul += 1

        pontos_grupoB['Paraguai'] += pontos_paraguai
        pontos_grupoB['África do Sul'] += pontos_africadosul

        return pontos_paraguai, pontos_africadosul


    def espanhaXaeslovenia(gols_espanha, gols_eslovenia):
        pontos_espanha = 0
        pontos_eslovenia = 0

        if gols_espanha > gols_eslovenia:
            pontos_espanha += 3
        elif gols_espanha < gols_eslovenia:
            pontos_eslovenia += 3
        else :
            pontos_espanha += 1
            pontos_eslovenia += 1

        pontos_grupoB['Espanha'] += pontos_espanha
        pontos_grupoB['Eslovênia'] += pontos_eslovenia

        return pontos_espanha, pontos_eslovenia


    def brasilXturquia(gols_brasil, gols_turquia):
        pontos_brasil = 0
        pontos_turquia = 0

        if gols_brasil > gols_turquia:
            pontos_brasil += 3
        elif gols_brasil < gols_turquia:
            pontos_turquia += 3
        else:
            pontos_brasil += 1
            pontos_turquia += 1

        pontos_grupoC['Brasil'] += pontos_brasil
        pontos_grupoC['Turquia'] += pontos_turquia

        return pontos_brasil, pontos_turquia


    def costaricaXchina(gols_costarica, gols_china):
        pontos_costarica = 0
        pontos_china = 0

        if gols_costarica > gols_china:
            pontos_costarica += 3
        elif gols_costarica < gols_china:
            pontos_china += 3
        else:
            pontos_costarica += 1
            pontos_china += 1

        pontos_grupoC['Costa Rica'] += pontos_costarica
        pontos_grupoC['China'] += pontos_china

        return pontos_costarica, pontos_china


    def coreiaXpolonia(gols_coreiadosul, gols_polonia):
        pontos_coreia = 0
        pontos_polonia = 0

        if gols_coreiadosul > gols_polonia:
            pontos_coreia += 3
        elif gols_coreiadosul < gols_polonia:
            pontos_polonia += 3
        else:
            pontos_coreia += 1
            pontos_polonia += 1

        pontos_grupoD['Coreia do Sul'] += pontos_coreia
        pontos_grupoD['Polônia'] += pontos_polonia

        return pontos_coreia, pontos_polonia


    def estadosunidosXportugal(gols_estadosunidos, gols_portugal):
        pontos_eua = 0
        pontos_portugal = 0

        if gols_estadosunidos > gols_portugal:
            pontos_eua += 3
        elif gols_estadosunidos < gols_portugal:
            pontos_portugal += 3
        else:
            pontos_eua += 1
            pontos_portugal += 1

        pontos_grupoD['Estados Unidos'] += pontos_eua
        pontos_grupoD['Portugal'] += pontos_portugal

        return pontos_eua, pontos_portugal


    def alemanhaXarabiasaudita(gols_alemanha, gols_arabia):
        pontos_alemanha = 0
        pontos_arabia = 0

        if gols_alemanha > gols_arabia:
            pontos_alemanha += 3
        elif gols_alemanha < gols_arabia:
            pontos_arabia += 3
        else:
            pontos_alemanha += 1
            pontos_arabia += 1

        pontos_grupoE['Alemanha'] += pontos_alemanha
        pontos_grupoE['Arábia Saudita'] += pontos_arabia

        return pontos_alemanha, pontos_arabia


    def irlandaXcamaroes(gols_irlanda, gols_camaroes):
        pontos_irlanda = 0
        pontos_camaroes = 0

        if gols_irlanda > gols_camaroes:
            pontos_irlanda += 3
        elif gols_irlanda < gols_camaroes:
            pontos_camaroes += 3
        else:
            pontos_irlanda += 1
            pontos_camaroes += 1

        pontos_grupoE['Irlanda'] += pontos_irlanda
        pontos_grupoE['Camarões'] += pontos_camaroes

        return pontos_irlanda, pontos_camaroes


    def sueciaXinglaterra(gols_suecia, gols_inglaterra):
        pontos_suecia = 0
        pontos_inglaterra = 0

        if gols_suecia > gols_inglaterra:
            pontos_suecia += 3
        elif gols_suecia < gols_inglaterra:
            pontos_inglaterra += 3
        else:
            pontos_suecia += 1
            pontos_inglaterra += 1

        pontos_grupoF['Suécia'] += pontos_suecia
        pontos_grupoF['Inglaterra'] += pontos_inglaterra

        return pontos_suecia, pontos_inglaterra


    def argentinaXnigeria(gols_argentina, gols_nigeria):
        pontos_argentina = 0
        pontos_nigeria = 0

        if gols_argentina > gols_nigeria:
            pontos_argentina += 3
        elif gols_argentina < gols_nigeria:
            pontos_nigeria += 3
        else:
            pontos_argentina += 1
            pontos_nigeria += 1

        pontos_grupoF['Argentina'] += pontos_argentina
        pontos_grupoF['Nigéria'] += pontos_nigeria

        return pontos_argentina, pontos_nigeria


    def mexicoXcroacia(gols_mexico, gols_croacia):
        pontos_mexico = 0
        pontos_croacia = 0

        if gols_mexico > gols_croacia:
            pontos_mexico += 3
        elif gols_mexico < gols_croacia:
            pontos_croacia += 3
        else:
            pontos_mexico += 1
            pontos_croacia += 1

        pontos_grupoG['México'] += pontos_mexico
        pontos_grupoG['Croácia'] += pontos_croacia

        return pontos_mexico, pontos_croacia


    def italiaXecuador(gols_italia, gols_equador):
        pontos_italia = 0
        pontos_equador = 0

        if gols_italia > gols_equador:
            pontos_italia += 3
        elif gols_italia < gols_equador:
            pontos_equador += 3
        else:
            pontos_italia += 1
            pontos_equador += 1

        pontos_grupoG['Itália'] += pontos_italia
        pontos_grupoG['Equador'] += pontos_equador

        return pontos_italia, pontos_equador


    def japaoXbelgica(gols_japao, gols_belgica):
        pontos_japao = 0
        pontos_belgica = 0

        if gols_japao > gols_belgica:
            pontos_japao += 3
        elif gols_japao < gols_belgica:
            pontos_belgica += 3
        else:
            pontos_japao += 1
            pontos_belgica += 1

        pontos_grupoH['Japão'] += pontos_japao
        pontos_grupoH['Bélgica'] += pontos_belgica

        return pontos_japao, pontos_belgica


    def russiaXtunisia(gols_russia, gols_tunisia):
        pontos_russia = 0
        pontos_tunisia = 0

        if gols_russia > gols_tunisia:
            pontos_russia += 3
        elif gols_russia < gols_tunisia:
            pontos_tunisia += 3
        else:
            pontos_russia += 1
            pontos_tunisia += 1

        pontos_grupoH['Rússia'] += pontos_russia
        pontos_grupoH['Tunísia'] += pontos_tunisia

        return pontos_russia, pontos_tunisia


    francaXsenegal(gols_franca, gols_senegal)
    uruguaiXdinamarca(gols_uruguai, gols_dinamarca)
    paraguaiXafricadosul(gols_paraguai, gols_africadosul)
    espanhaXaeslovenia(gols_espanha, gols_eslovenia)
    brasilXturquia(gols_brasil, gols_turquia)
    costaricaXchina(gols_costarica, gols_china)
    coreiaXpolonia(gols_coreiadosul, gols_polonia)
    estadosunidosXportugal(gols_estadosunidos, gols_portugal)
    alemanhaXarabiasaudita(gols_alemanha, gols_arabiasaudita)
    irlandaXcamaroes(gols_irlanda, gols_camaroes)
    sueciaXinglaterra(gols_suecia, gols_inglaterra)
    argentinaXnigeria(gols_argentina, gols_nigeria)
    mexicoXcroacia(gols_mexico, gols_croacia)
    italiaXecuador(gols_italia, gols_equador)  
    japaoXbelgica(gols_japao, gols_belgica)
    russiaXtunisia(gols_russia, gols_tunisia)   


    print('\nPontuação atualizada do grupo A:') 
    for sel, pts in pontos_grupoA.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo B:') 
    for sel, pts in pontos_grupoB.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo C:') 
    for sel, pts in pontos_grupoC.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo D:') 
    for sel, pts in pontos_grupoD.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo E:') 
    for sel, pts in pontos_grupoE.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo F:') 
    for sel, pts in pontos_grupoF.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo G:') 
    for sel, pts in pontos_grupoG.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo H:') 
    for sel, pts in pontos_grupoH.items():
        print(f"{sel}: {pts}")


rodada1()

########################################################################

def rodada2():
    # Grupo A
    gols_franca = 0
    gols_senegal = 1
    gols_uruguai = 0
    gols_dinamarca = 1

    # Grupo B
    gols_paraguai = 1
    gols_africadosul = 1
    gols_espanha = 3
    gols_eslovenia = 0

    # Grupo C
    gols_brasil = 4
    gols_turquia = 1
    gols_costarica = 1
    gols_china = 0

    # Grupo D
    gols_coreiadosul = 1
    gols_polonia = 0
    gols_estadosunidos = 1
    gols_portugal = 4

    # Grupo E
    gols_alemanha = 1
    gols_arabiasaudita = 0
    gols_irlanda = 1
    gols_camaroes = 1

    # Grupo F
    gols_suecia = 2
    gols_inglaterra = 1
    gols_argentina = 0
    gols_nigeria = 1

    # Grupo G
    gols_mexico = 2
    gols_croacia = 2
    gols_italia = 1
    gols_equador = 1

    # Grupo H
    gols_japao = 1
    gols_belgica = 1
    gols_russia = 0
    gols_tunisia = 1


    print(f"\nPlacares da 2ª rodada:\
        \nDinamarca {gols_dinamarca} x {gols_senegal} Senegal\
        \nFrança {gols_franca} x {gols_uruguai} Uruguai\
        \nEspanha {gols_espanha} x {gols_paraguai} Paraguai\
        \nÁfrica do Sul {gols_africadosul} x {gols_eslovenia} Eslovênia\
        \nBrasil {gols_brasil} x {gols_china} China\
        \nCosta Rica {gols_costarica} x {gols_turquia} Turquia\
        \nCoreia do Sul {gols_coreiadosul} x {gols_estadosunidos} Estados Unidos\
        \nPortugal {gols_portugal} x {gols_polonia} Polônia\
        \nAlemanha {gols_alemanha} x {gols_irlanda} Irlanda\
        \nCamarões {gols_camaroes} x {gols_arabiasaudita} Arábia Saudita\
        \nSuécia {gols_suecia} x {gols_nigeria} Nigéria\
        \nArgentina {gols_argentina} x {gols_inglaterra} Inglaterra\
        \nItália {gols_italia} x {gols_croacia} Croácia\
        \nMéxico {gols_mexico} x {gols_equador} Equador\
        \nJapão {gols_japao} x {gols_russia} Rússia\
        \nTunísia {gols_tunisia} x {gols_belgica} Bélgica\n")
    

    def dinamarcaXsenegal(gols_dinamarca, gols_senegal):
        pontos_dinamarca = 0
        pontos_senegal = 0

        if gols_dinamarca > gols_senegal:
            pontos_dinamarca += 3
        elif gols_dinamarca < gols_senegal:
            pontos_senegal += 3
        else:
            pontos_dinamarca += 1
            pontos_senegal += 1

        pontos_grupoA['Dinamarca'] += pontos_dinamarca
        pontos_grupoA['Senegal'] += pontos_senegal

        return pontos_dinamarca, pontos_senegal


    def francaXuruguai(gols_franca, gols_uruguai):
        pontos_franca = 0
        pontos_uruguai = 0

        if gols_franca > gols_uruguai:
            pontos_franca += 3
        elif gols_franca < gols_uruguai:
            pontos_uruguai += 3
        else:
            pontos_franca += 1
            pontos_uruguai += 1

        pontos_grupoA['França'] += pontos_franca
        pontos_grupoA['Uruguai'] += pontos_uruguai

        return pontos_franca, pontos_uruguai


    def espanhaXparaguai(gols_espanha, gols_paraguai):
        pontos_espanha = 0
        pontos_paraguai = 0

        if gols_espanha > gols_paraguai:
            pontos_espanha += 3
        elif gols_espanha < gols_paraguai:
            pontos_paraguai += 3
        else:
            pontos_espanha += 1
            pontos_paraguai += 1

        pontos_grupoB['Espanha'] += pontos_espanha
        pontos_grupoB['Paraguai'] += pontos_paraguai

        return pontos_espanha, pontos_paraguai


    def africadosulXeslovenia(gols_africadosul, gols_eslovenia):
        pontos_africa = 0
        pontos_eslovenia = 0

        if gols_africadosul > gols_eslovenia:
            pontos_africa += 3
        elif gols_africadosul < gols_eslovenia:
            pontos_eslovenia += 3
        else:
            pontos_africa += 1
            pontos_eslovenia += 1

        pontos_grupoB['África do Sul'] += pontos_africa
        pontos_grupoB['Eslovênia'] += pontos_eslovenia

        return pontos_africa, pontos_eslovenia


    def brasilXchina(gols_brasil, gols_china):
        pontos_brasil = 0
        pontos_china = 0

        if gols_brasil > gols_china:
            pontos_brasil += 3
        elif gols_brasil < gols_china:
            pontos_china += 3
        else:
            pontos_brasil += 1
            pontos_china += 1

        pontos_grupoC['Brasil'] += pontos_brasil
        pontos_grupoC['China'] += pontos_china

        return pontos_brasil, pontos_china


    def costaricaXturquia(gols_costarica, gols_turquia):
        pontos_costarica = 0
        pontos_turquia = 0

        if gols_costarica > gols_turquia:
            pontos_costarica += 3
        elif gols_costarica < gols_turquia:
            pontos_turquia += 3
        else:
            pontos_costarica += 1
            pontos_turquia += 1

        pontos_grupoC['Costa Rica'] += pontos_costarica
        pontos_grupoC['Turquia'] += pontos_turquia

        return pontos_costarica, pontos_turquia


    def coreiaXestadosunidos(gols_coreiadosul, gols_estadosunidos):
        pontos_coreia = 0
        pontos_eua = 0

        if gols_coreiadosul > gols_estadosunidos:
            pontos_coreia += 3
        elif gols_coreiadosul < gols_estadosunidos:
            pontos_eua += 3
        else:
            pontos_coreia += 1
            pontos_eua += 1

        pontos_grupoD['Coreia do Sul'] += pontos_coreia
        pontos_grupoD['Estados Unidos'] += pontos_eua

        return pontos_coreia, pontos_eua


    def portugalXpolonia(gols_portugal, gols_polonia):
        pontos_portugal = 0
        pontos_polonia = 0

        if gols_portugal > gols_polonia:
            pontos_portugal += 3
        elif gols_portugal < gols_polonia:
            pontos_polonia += 3
        else:
            pontos_portugal += 1
            pontos_polonia += 1

        pontos_grupoD['Portugal'] += pontos_portugal
        pontos_grupoD['Polônia'] += pontos_polonia

        return pontos_portugal, pontos_polonia


    def alemanhaXirlanda(gols_alemanha, gols_irlanda):
        pontos_alemanha = 0
        pontos_irlanda = 0

        if gols_alemanha > gols_irlanda:
            pontos_alemanha += 3
        elif gols_alemanha < gols_irlanda:
            pontos_irlanda += 3
        else:
            pontos_alemanha += 1
            pontos_irlanda += 1

        pontos_grupoE['Alemanha'] += pontos_alemanha
        pontos_grupoE['Irlanda'] += pontos_irlanda

        return pontos_alemanha, pontos_irlanda


    def camaroesXarabiasaudita(gols_camaroes, gols_arabiasaudita):
        pontos_camaroes = 0
        pontos_arabia = 0

        if gols_camaroes > gols_arabiasaudita:
            pontos_camaroes += 3
        elif gols_camaroes < gols_arabiasaudita:
            pontos_arabia += 3
        else:
            pontos_camaroes += 1
            pontos_arabia += 1

        pontos_grupoE['Camarões'] += pontos_camaroes
        pontos_grupoE['Arábia Saudita'] += pontos_arabia

        return pontos_camaroes, pontos_arabia


    def sueciaXnigeria(gols_suecia, gols_nigeria):
        pontos_suecia = 0
        pontos_nigeria = 0

        if gols_suecia > gols_nigeria:
            pontos_suecia += 3
        elif gols_suecia < gols_nigeria:
            pontos_nigeria += 3
        else:
            pontos_suecia += 1
            pontos_nigeria += 1

        pontos_grupoF['Suécia'] += pontos_suecia
        pontos_grupoF['Nigéria'] += pontos_nigeria

        return pontos_suecia, pontos_nigeria


    def argentinaXinglaterra(gols_argentina, gols_inglaterra):
        pontos_argentina = 0
        pontos_inglaterra = 0

        if gols_argentina > gols_inglaterra:
            pontos_argentina += 3
        elif gols_argentina < gols_inglaterra:
            pontos_inglaterra += 3
        else:
            pontos_argentina += 1
            pontos_inglaterra += 1

        pontos_grupoF['Argentina'] += pontos_argentina
        pontos_grupoF['Inglaterra'] += pontos_inglaterra

        return pontos_argentina, pontos_inglaterra


    def italiaXcroacia(gols_italia, gols_croacia):
        pontos_italia = 0
        pontos_croacia = 0

        if gols_italia > gols_croacia:
            pontos_italia += 3
        elif gols_italia < gols_croacia:
            pontos_croacia += 3
        else:
            pontos_italia += 1
            pontos_croacia += 1

        pontos_grupoG['Itália'] += pontos_italia
        pontos_grupoG['Croácia'] += pontos_croacia

        return pontos_italia, pontos_croacia


    def mexicoXequador(gols_mexico, gols_equador):
        pontos_mexico = 0
        pontos_equador = 0

        if gols_mexico > gols_equador:
            pontos_mexico += 3
        elif gols_mexico < gols_equador:
            pontos_equador += 3
        else:
            pontos_mexico += 1
            pontos_equador += 1

        pontos_grupoG['México'] += pontos_mexico
        pontos_grupoG['Equador'] += pontos_equador

        return pontos_mexico, pontos_equador


    def japaoXrussia(gols_japao, gols_russia):
        pontos_japao = 0
        pontos_russia = 0

        if gols_japao > gols_russia:
            pontos_japao += 3
        elif gols_japao < gols_russia:
            pontos_russia += 3
        else:
            pontos_japao += 1
            pontos_russia += 1

        pontos_grupoH['Japão'] += pontos_japao
        pontos_grupoH['Rússia'] += pontos_russia

        return pontos_japao, pontos_russia


    def tunisiaXbelgica(gols_tunisia, gols_belgica):
        pontos_tunisia = 0
        pontos_belgica = 0

        if gols_tunisia > gols_belgica:
            pontos_tunisia += 3
        elif gols_tunisia < gols_belgica:
            pontos_belgica += 3
        else:
            pontos_tunisia += 1
            pontos_belgica += 1

        pontos_grupoH['Tunísia'] += pontos_tunisia
        pontos_grupoH['Bélgica'] += pontos_belgica

        return pontos_tunisia, pontos_belgica


    dinamarcaXsenegal(gols_dinamarca, gols_senegal)
    francaXuruguai(gols_franca, gols_uruguai)
    espanhaXparaguai(gols_espanha, gols_paraguai)
    africadosulXeslovenia(gols_africadosul, gols_eslovenia)
    brasilXchina(gols_brasil, gols_china)
    costaricaXturquia(gols_costarica, gols_turquia)
    coreiaXestadosunidos(gols_coreiadosul, gols_estadosunidos)
    portugalXpolonia(gols_portugal, gols_polonia)
    alemanhaXirlanda(gols_alemanha, gols_irlanda)
    camaroesXarabiasaudita(gols_camaroes, gols_arabiasaudita)
    sueciaXnigeria(gols_suecia, gols_nigeria)
    argentinaXinglaterra(gols_argentina, gols_inglaterra)
    italiaXcroacia(gols_italia, gols_croacia)
    mexicoXequador(gols_mexico, gols_equador)
    japaoXrussia(gols_japao, gols_russia)
    tunisiaXbelgica(gols_tunisia, gols_belgica)


    print('\nPontuação atualizada do grupo A:') 
    for sel, pts in pontos_grupoA.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo B:') 
    for sel, pts in pontos_grupoB.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo C:') 
    for sel, pts in pontos_grupoC.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo D:') 
    for sel, pts in pontos_grupoD.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo E:') 
    for sel, pts in pontos_grupoE.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo F:') 
    for sel, pts in pontos_grupoF.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo G:') 
    for sel, pts in pontos_grupoG.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo H:') 
    for sel, pts in pontos_grupoH.items():
        print(f"{sel}: {pts}")


rodada2()

########################################################################


def rodada3():
    # Grupo A
    gols_franca = 0
    gols_senegal = 3
    gols_uruguai = 3
    gols_dinamarca = 2

    # Grupo B
    gols_paraguai = 3
    gols_africadosul = 2
    gols_espanha = 3
    gols_eslovenia = 1

    # Grupo C
    gols_brasil = 5
    gols_turquia = 3
    gols_costarica = 2
    gols_china = 0

    # Grupo D
    gols_coreiadosul = 1
    gols_polonia = 3
    gols_estadosunidos = 1
    gols_portugal = 0

    # Grupo E
    gols_alemanha = 2
    gols_arabiasaudita = 0
    gols_irlanda = 3
    gols_camaroes = 0

    # Grupo F
    gols_suecia = 1
    gols_inglaterra = 0
    gols_argentina = 1
    gols_nigeria = 0

    # Grupo G
    gols_mexico = 1
    gols_croacia = 0
    gols_italia = 1
    gols_equador = 1

    # Grupo H
    gols_japao = 2
    gols_belgica = 3
    gols_russia = 2
    gols_tunisia = 0


    print(f"\nPlacares da 3ª rodada:\
        \nDinamarca {gols_dinamarca} x {gols_franca} França\
        \nSenegal {gols_senegal} x {gols_uruguai} Uruguai\
        \nÁfrica do Sul {gols_africadosul} x {gols_espanha} Espanha\
        \nEslovênia {gols_eslovenia} x {gols_paraguai} Paraguai\
        \nCosta Rica {gols_costarica} x {gols_brasil} Brasil\
        \nTurquia {gols_turquia} x {gols_china} China\
        \nPortugal {gols_portugal} x {gols_coreiadosul} Coreia do Sul\
        \nPolônia {gols_polonia} x {gols_estadosunidos} Estados Unidos\
        \nCamarões {gols_camaroes} x {gols_alemanha} Alemanha\
        \nArábia Saudita {gols_arabiasaudita} x {gols_irlanda} Irlanda\
        \nNigéria {gols_nigeria} x {gols_inglaterra} Inglaterra\
        \nSuécia {gols_suecia} x {gols_argentina} Argentina\
        \nEquador {gols_equador} x {gols_croacia} Croácia\
        \nMéxico {gols_mexico} x {gols_italia} Itália\
        \nTunísia {gols_tunisia} x {gols_japao} Japão\
        \nBélgica {gols_belgica} x {gols_russia} Rússia\n")


    def dinamarcaXfranca(gols_dinamarca, gols_franca):
        pontos_dinamarca = 0
        pontos_franca = 0

        if gols_dinamarca > gols_franca:
            pontos_dinamarca += 3
        elif gols_dinamarca < gols_franca:
            pontos_franca += 3
        else:
            pontos_dinamarca += 1
            pontos_franca += 1

        pontos_grupoA['Dinamarca'] += pontos_dinamarca
        pontos_grupoA['França'] += pontos_franca

        return pontos_dinamarca, pontos_franca


    def senegalXuruguai(gols_senegal, gols_uruguai):
        pontos_senegal = 0
        pontos_uruguai = 0

        if gols_senegal > gols_uruguai:
            pontos_senegal += 3
        elif gols_senegal < gols_uruguai:
            pontos_uruguai += 3
        else:
            pontos_senegal += 1
            pontos_uruguai += 1

        pontos_grupoA['Senegal'] += pontos_senegal
        pontos_grupoA['Uruguai'] += pontos_uruguai

        return pontos_senegal, pontos_uruguai


    def africadosulXespanha(gols_africadosul, gols_espanha):
        pontos_africa = 0
        pontos_espanha = 0

        if gols_africadosul > gols_espanha:
            pontos_africa += 3
        elif gols_africadosul < gols_espanha:
            pontos_espanha += 3
        else:
            pontos_africa += 1
            pontos_espanha += 1

        pontos_grupoB['África do Sul'] += pontos_africa
        pontos_grupoB['Espanha'] += pontos_espanha

        return pontos_africa, pontos_espanha


    def esloveniaXparaguai(gols_eslovenia, gols_paraguai):
        pontos_eslovenia = 0
        pontos_paraguai = 0

        if gols_eslovenia > gols_paraguai:
            pontos_eslovenia += 3
        elif gols_eslovenia < gols_paraguai:
            pontos_paraguai += 3
        else:
            pontos_eslovenia += 1
            pontos_paraguai += 1

        pontos_grupoB['Eslovênia'] += pontos_eslovenia
        pontos_grupoB['Paraguai'] += pontos_paraguai

        return pontos_eslovenia, pontos_paraguai


    def costaricaXbrasil(gols_costarica, gols_brasil):
        pontos_costarica = 0
        pontos_brasil = 0

        if gols_costarica > gols_brasil:
            pontos_costarica += 3
        elif gols_costarica < gols_brasil:
            pontos_brasil += 3
        else:
            pontos_costarica += 1
            pontos_brasil += 1

        pontos_grupoC['Costa Rica'] += pontos_costarica
        pontos_grupoC['Brasil'] += pontos_brasil

        return pontos_costarica, pontos_brasil


    def turquiaXchina(gols_turquia, gols_china):
        pontos_turquia = 0
        pontos_china = 0

        if gols_turquia > gols_china:
            pontos_turquia += 3
        elif gols_turquia < gols_china:
            pontos_china += 3
        else:
            pontos_turquia += 1
            pontos_china += 1

        pontos_grupoC['Turquia'] += pontos_turquia
        pontos_grupoC['China'] += pontos_china

        return pontos_turquia, pontos_china 


    def portugalXcoreiadosul(gols_portugal, gols_coreiadosul):
        pontos_portugal = 0
        pontos_coreiadosul = 0

        if gols_portugal > gols_coreiadosul:
            pontos_portugal += 3
        elif gols_portugal < gols_coreiadosul:
            pontos_coreiadosul += 3
        else:
            pontos_portugal += 1
            pontos_coreiadosul += 1

        pontos_grupoD['Portugal'] += pontos_portugal
        pontos_grupoD['Coreia do Sul'] += pontos_coreiadosul

        return pontos_portugal, pontos_coreiadosul


    def poloniaXestadosunidos(gols_polonia, gols_estadosunidos):
        pontos_polonia = 0
        pontos_estadosunidos = 0

        if gols_polonia > gols_estadosunidos:
            pontos_polonia += 3
        elif gols_polonia < gols_estadosunidos:
            pontos_estadosunidos += 3
        else:
            pontos_polonia += 1
            pontos_estadosunidos += 1

        pontos_grupoD['Polônia'] += pontos_polonia
        pontos_grupoD['Estados Unidos'] += pontos_estadosunidos

        return pontos_polonia, pontos_estadosunidos


    def camaroesXalemanha(gols_camaroes, gols_alemanha):
        pontos_camaroes = 0
        pontos_alemanha = 0

        if gols_camaroes > gols_alemanha:
            pontos_camaroes += 3
        elif gols_camaroes < gols_alemanha:
            pontos_alemanha += 3
        else:
            pontos_camaroes += 1
            pontos_alemanha += 1

        pontos_grupoE['Camarões'] += pontos_camaroes
        pontos_grupoE['Alemanha'] += pontos_alemanha

        return pontos_camaroes, pontos_alemanha


    def arabiasauditaXirlanda(gols_arabiasaudita, gols_irlanda):
        pontos_arabia = 0
        pontos_irlanda = 0

        if gols_arabiasaudita > gols_irlanda:
            pontos_arabia += 3
        elif gols_arabiasaudita < gols_irlanda:
            pontos_irlanda += 3
        else:
            pontos_arabia += 1
            pontos_irlanda += 1

        pontos_grupoE['Arábia Saudita'] += pontos_arabia
        pontos_grupoE['Irlanda'] += pontos_irlanda

        return pontos_arabia, pontos_irlanda


    def nigeriaXinglaterra(gols_nigeria, gols_inglaterra):
        pontos_nigeria = 0
        pontos_inglaterra = 0

        if gols_nigeria > gols_inglaterra:
            pontos_nigeria += 3
        elif gols_nigeria < gols_inglaterra:
            pontos_inglaterra += 3
        else:
            pontos_nigeria += 1
            pontos_inglaterra += 1

        pontos_grupoF['Nigéria'] += pontos_nigeria
        pontos_grupoF['Inglaterra'] += pontos_inglaterra

        return pontos_nigeria, pontos_inglaterra 


    def argentinaXsuecia(gols_argentina, gols_suecia):
        pontos_argentina = 0
        pontos_suecia = 0

        if gols_argentina > gols_suecia:
            pontos_argentina += 3
        elif gols_argentina < gols_suecia:
            pontos_suecia += 3
        else:
            pontos_argentina += 1
            pontos_suecia += 1

        pontos_grupoF['Argentina'] += pontos_argentina
        pontos_grupoF['Suécia'] += pontos_suecia

        return pontos_argentina, pontos_suecia


    def croaciaXitalia(gols_croacia, gols_italia):
        pontos_croacia = 0
        pontos_italia = 0

        if gols_croacia > gols_italia:
            pontos_croacia += 3
        elif gols_croacia < gols_italia:
            pontos_italia += 3
        else:
            pontos_croacia += 1
            pontos_italia += 1

        pontos_grupoG['Croácia'] += pontos_croacia
        pontos_grupoG['Itália'] += pontos_italia

        return pontos_croacia, pontos_italia


    def equadorXmexico(gols_equador, gols_mexico):
        pontos_equador = 0
        pontos_mexico = 0

        if gols_equador > gols_mexico:
            pontos_equador += 3
        elif gols_equador < gols_mexico:
            pontos_mexico += 3
        else:
            pontos_equador += 1
            pontos_mexico += 1

        pontos_grupoG['Equador'] += pontos_equador
        pontos_grupoG['México'] += pontos_mexico

        return pontos_equador, pontos_mexico


    def tunisiaXjapao(gols_tunisia, gols_japao):
        pontos_tunisia = 0
        pontos_japao = 0

        if gols_tunisia > gols_japao:
            pontos_tunisia += 3
        elif gols_tunisia < gols_japao:
            pontos_japao += 3
        else:
            pontos_tunisia += 1
            pontos_japao += 1

        pontos_grupoH['Tunísia'] += pontos_tunisia
        pontos_grupoH['Japão'] += pontos_japao  

        return pontos_tunisia, pontos_japao


    def belgicaXrussia(gols_belgica, gols_russia):
        pontos_belgica = 0
        pontos_russia = 0

        if gols_belgica > gols_russia:
            pontos_belgica += 3
        elif gols_belgica < gols_russia:
            pontos_russia += 3
        else:
            pontos_belgica += 1
            pontos_russia += 1

        pontos_grupoH['Bélgica'] += pontos_belgica
        pontos_grupoH['Rússia'] += pontos_russia

        return pontos_belgica, pontos_russia

    dinamarcaXfranca(gols_dinamarca, gols_franca)
    senegalXuruguai(gols_senegal, gols_uruguai)
    africadosulXespanha(gols_africadosul, gols_espanha)
    esloveniaXparaguai(gols_eslovenia, gols_paraguai)
    costaricaXbrasil(gols_costarica, gols_brasil)
    turquiaXchina(gols_turquia, gols_china)
    portugalXcoreiadosul(gols_portugal, gols_coreiadosul)
    poloniaXestadosunidos(gols_polonia, gols_estadosunidos)
    camaroesXalemanha(gols_camaroes, gols_alemanha)
    arabiasauditaXirlanda(gols_arabiasaudita, gols_irlanda)
    nigeriaXinglaterra(gols_nigeria, gols_inglaterra)
    argentinaXsuecia(gols_argentina, gols_suecia)
    croaciaXitalia(gols_croacia, gols_italia)
    equadorXmexico(gols_equador, gols_mexico)
    tunisiaXjapao(gols_tunisia, gols_japao)
    belgicaXrussia(gols_belgica, gols_russia)


    print('\nPontuação atualizada do grupo A:') 
    for sel, pts in pontos_grupoA.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo B:') 
    for sel, pts in pontos_grupoB.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo C:') 
    for sel, pts in pontos_grupoC.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo D:') 
    for sel, pts in pontos_grupoD.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo E:') 
    for sel, pts in pontos_grupoE.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo F:') 
    for sel, pts in pontos_grupoF.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo G:') 
    for sel, pts in pontos_grupoG.items():
        print(f"{sel}: {pts}")

    print('\nPontuação atualizada do grupo H:') 
    for sel, pts in pontos_grupoH.items():
        print(f"{sel}: {pts}")

rodada3()