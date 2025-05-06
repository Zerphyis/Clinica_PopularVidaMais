import sqlite3

DB_NAME = "vida_mais.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            crm TEXT UNIQUE,
            especialidade TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE,
            data_nascimento TEXT,
            telefone TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER,
            medico_id INTEGER,
            data TEXT,
            observacoes TEXT,
            FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
            FOREIGN KEY (medico_id) REFERENCES medicos(id)
        )
    """)
    con.commit()
    con.close()