from rich import print

def atualiza_pontos(grupo, selecao1, gols1, selecao2, gols2):
    grupo[selecao1]['gm'] += gols1
    grupo[selecao1]['gs'] += gols2
    grupo[selecao2]['gm'] += gols2
    grupo[selecao2]['gs'] += gols1

    if gols1 > gols2:
        grupo[selecao1]['pontos'] += 3
    elif gols1 < gols2:
        grupo[selecao2]['pontos'] += 3
    else:
        grupo[selecao1]['pontos'] += 1
        grupo[selecao2]['pontos'] += 1


def mostrar_pontos(grupo, nome_grupo):
    print(f"\n[b cyan]{nome_grupo}[/b cyan]")
    print("[bold]SELEÇÃO               P   GM   GS   SG[/bold]")

    tabela_ordenada = sorted(
        grupo.items(),
        key=lambda x: (
            x[1]['pontos'],
            (x[1]['gm'] - x[1]['gs']),
            x[1]['gm']
        ),
        reverse=True
    )
    
    for selecao, stats in tabela_ordenada:
        sg = stats['gm'] - stats['gs']
        print(f"{selecao:<20} {stats['pontos']:>2}   {stats['gm']:>2}   {stats['gs']:>2}   {sg:>2}")


def mostra_placares(placares):
    print("\n[b yellow]PLACARES DA RODADA[/b yellow]")
    for jogo in placares:
        print(f"{jogo[0]} {jogo[1]} x {jogo[2]} {jogo[3]}")