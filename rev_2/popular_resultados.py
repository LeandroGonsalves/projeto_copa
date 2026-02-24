import sqlite3
import random

DB_PATH = "database/database.db"


def gerar_resultado_fake(id_partida):
    return (
        random.randint(0, 5),  # gols mandante
        random.randint(0, 5),  # gols visitante
        random.randint(0, 4),  # ca mandante
        random.randint(0, 1),  # cv mandante
        random.randint(0, 4),  # ca visitante
        random.randint(0, 1),  # cv visitante
        "Finalizado",
        id_partida
    )


def popular_resultados():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    update_sql = """
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

    for id_partida in range(1, 73):
        dados = gerar_resultado_fake(id_partida)
        cursor.execute(update_sql, dados)

    conn.commit()
    conn.close()

    print("✅ Resultados fake inseridos com sucesso!")


if __name__ == "__main__":
    popular_resultados()