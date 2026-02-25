import sqlite3

DB_PATH = "database/database.db"


def atualizar_dados_jogo(dados_validados):
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()

    update_table = f""" 
        UPDATE ft_partidas
        SET
            gols_mandante = ?,
            gols_visitante = ?,
            ca_mandante = ?,
            cv_mandante = ?,
            ca_visitante = ?,
            cv_visitante = ?,
            status_partida = ?
        WHERE id_partida = ?
    """

    cursor.execute(update_table, (
        dados_validados['gols_mandante'],
        dados_validados['gols_visitante'],
        dados_validados['ca_mandante'],
        dados_validados['cv_mandante'],
        dados_validados['ca_visitante'],
        dados_validados['cv_visitante'],
        dados_validados['status_partida'],
        dados_validados['id_partida']
    ))

    #print("Linhas afetadas:", cursor.rowcount)

    conn.commit()
    conn.close()
    
    return


def buscar_partidas():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # importante
    cursor = conn.cursor()

    query = """
        SELECT 
            dp.grupo,
            dp.rodada,
            dp.data_partida,
            dp.horario,
            dn_m.nome_pais AS mandante,
            fp.gols_mandante,
            fp.ca_mandante,
            fp.cv_mandante,
            dn_v.nome_pais AS visitante,
            fp.gols_visitante,
            fp.ca_visitante,
            fp.cv_visitante,
            fp.status_partida 
        FROM ft_partidas fp
        INNER JOIN dim_partidas dp
            ON fp.id_partida = dp.id_partida
        INNER JOIN dim_nations dn_m
            ON dp.id_mandante = dn_m.id
        INNER JOIN dim_nations dn_v
            ON dp.id_visitante = dn_v.id
    """

    cursor.execute(query)

    resultados = cursor.fetchall()

    conn.close()

    return [dict(row) for row in resultados]


def buscar_classificacao():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # importante
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM vw_classificacao
        ORDER BY grupo, posicao
    """)

    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return dados


def gerar_segunda_fase(dados):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = open("database/dim_chaveamento.sql").read()

    cursor.execute(query)
    
    cursor.commit()
    conn.close()
    