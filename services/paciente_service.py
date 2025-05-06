from database.db import conectar
from models.paciente import Paciente

def cadastrar_paciente():
    try:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        nascimento = input("Data de nascimento (YYYY-MM-DD): ")
        telefone = input("Telefone: ")
        paciente = Paciente(nome, cpf, nascimento, telefone)
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO pacientes (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)",
                    (paciente.nome, paciente.cpf, paciente.data_nascimento, paciente.telefone))
        con.commit()
        print("Paciente cadastrado.")
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}")
    finally:
        con.close()

def listar_pacientes():
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM pacientes")
        for p in cur.fetchall():
            print(p)
    except Exception as e:
        print(f"Erro ao listar pacientes: {e}")
    finally:
        con.close()

def atualizar_paciente():
    try:
        id_paciente = input("ID do paciente a atualizar: ")
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        con = conectar()
        cur = con.cursor()
        cur.execute("UPDATE pacientes SET nome=?, telefone=? WHERE id=?", (nome, telefone, id_paciente))
        if cur.rowcount == 0:
            print("Paciente não encontrado.")
        else:
            con.commit()
            print("Paciente atualizado.")
    except Exception as e:
        print(f"Erro ao atualizar paciente: {e}")
    finally:
        con.close()

def deletar_paciente():
    try:
        id_paciente = input("ID do paciente a deletar: ")
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM pacientes WHERE id=?", (id_paciente,))
        if cur.rowcount == 0:
            print("Paciente não encontrado.")
        else:
            con.commit()
            print("Paciente deletado.")
    except Exception as e:
        print(f"Erro ao deletar paciente: {e}")
    finally:
        con.close()
