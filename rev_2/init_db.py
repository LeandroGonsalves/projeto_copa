import sqlite3

# cria (ou conecta) ao banco
conn = sqlite3.connect("database.db")

# abre o arquivo schema.sql e executa
#with open("dim_nations.sql", "r", encoding="utf-8") as f:
with open("dim_selecoes_copa.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Tabela criada com sucesso!")
