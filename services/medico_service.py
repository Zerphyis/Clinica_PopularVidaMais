from database.db import conectar
from models.medico import Medico

def cadastrar_medico():
    try:
        nome = input("Nome: ")
        crm = input("CRM: ")
        especialidade = input("Especialidade: ")
        medico = Medico(nome, crm, especialidade)
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO medicos (nome, crm, especialidade) VALUES (?, ?, ?)",
                    (medico.nome, medico.crm, medico.especialidade))
        con.commit()
        print("Médico cadastrado.")
    except Exception as e:
        print(f"Erro ao cadastrar médico: {e}")
    finally:
        con.close()

def listar_medicos():
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM medicos")
        for m in cur.fetchall():
            print(m)
    except Exception as e:
        print(f"Erro ao listar médicos: {e}")
    finally:
        con.close()

def atualizar_medico():
    try:
        id_medico = input("ID do médico a atualizar: ")
        nome = input("Novo nome: ")
        especialidade = input("Nova especialidade: ")
        con = conectar()
        cur = con.cursor()
        cur.execute("UPDATE medicos SET nome=?, especialidade=? WHERE id=?", (nome, especialidade, id_medico))
        if cur.rowcount == 0:
            print("Médico não encontrado.")
        else:
            con.commit()
            print("Médico atualizado.")
    except Exception as e:
        print(f"Erro ao atualizar médico: {e}")
    finally:
        con.close()

def deletar_medico():
    try:
        id_medico = input("ID do médico a deletar: ")
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM medicos WHERE id=?", (id_medico,))
        if cur.rowcount == 0:
            print("Médico não encontrado.")
        else:
            con.commit()
            print("Médico deletado.")
    except Exception as e:
        print(f"Erro ao deletar médico: {e}")
    finally:
        con.close()
