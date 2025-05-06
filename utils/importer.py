import csv
import json
from database.db import conectar

def importar_medicos_csv():
    try:
        con = conectar()
        cur = con.cursor()
        with open("data/medicos.csv", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cur.execute("INSERT INTO medicos (nome, crm, especialidade) VALUES (?, ?, ?)",
                                (row["nome"], row["crm"], row["especialidade"]))
                except Exception:
                    continue
        con.commit()
    except Exception as e:
        print(f"Erro ao importar médicos: {e}")
    finally:
        con.close()

def importar_pacientes_json():
    try:
        con = conectar()
        cur = con.cursor()
        with open("data/pacientes.json", encoding="utf-8") as jsonfile:
            pacientes = json.load(jsonfile)
            for p in pacientes:
                try:
                    cur.execute("INSERT INTO pacientes (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)",
                                (p["nome"], p["cpf"], p["data_nascimento"], p["telefone"]))
                except Exception:
                    continue
        con.commit()
    except Exception as e:
        print(f"Erro ao importar pacientes: {e}")
    finally:
        con.close()