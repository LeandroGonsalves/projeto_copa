import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)

db_path = os.path.join(BASE_DIR, "database.db")
sql_path = os.path.join(BASE_DIR, "ft_partidas.sql")

conn = sqlite3.connect(db_path)

with open(sql_path, "r", encoding="utf-8") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("✅ Tabela criada com sucesso!")