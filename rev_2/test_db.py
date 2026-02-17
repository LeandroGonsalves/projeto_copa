import sqlite3

# conecta ao banco
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# pega os 5 primeiros países
cursor.execute("SELECT id, nome_pais, continente FROM dim_nations LIMIT 5;")
resultado = cursor.fetchall()

print(resultado)

conn.close()
