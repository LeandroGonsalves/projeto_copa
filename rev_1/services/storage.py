import csv
import json
import os

DATABASE_FILE = "database.csv"


def inicializar_database():
    """
    Esta função cria o arquivo CSV caso ele ainda não exista.

    Ela também cria o cabeçalho com as colunas:
    - id_copa
    - competition_name
    - data_json
    """
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id_copa", "competition_name", "data_json"])


def salvar_competicao(id_copa, competition_name, data):
    data_json = json.dumps(data)

    with open(DATABASE_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id_copa", "competition_name", "data_json"])
        writer.writerow([id_copa, competition_name, data_json])


def carregar_competicao():
    if not os.path.exists(DATABASE_FILE):
        return None

    with open(DATABASE_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            return None
        
        row = rows[0]
        return {
            "id_copa": row["id_copa"],
            "competition_name": row["competition_name"],
            "data": json.loads(row["data_json"])
        }
