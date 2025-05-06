from database.db import conectar

def agendar_consulta():
    try:
        paciente_id = input("ID do paciente: ")
        medico_id = input("ID do médico: ")
        data = input("Data da consulta (YYYY-MM-DD HH:MM): ")
        obs = input("Observações: ")
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO consultas (paciente_id, medico_id, data, observacoes) VALUES (?, ?, ?, ?)",
                    (paciente_id, medico_id, data, obs))
        con.commit()
        print("Consulta agendada.")
    except Exception as e:
        print(f"Erro ao agendar consulta: {e}")
    finally:
        con.close()

def listar_consultas_paciente():
    try:
        paciente_id = input("ID do paciente: ")
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT c.id, m.nome, c.data, c.observacoes
            FROM consultas c
            JOIN medicos m ON c.medico_id = m.id
            WHERE c.paciente_id = ?
            ORDER BY c.data
        """, (paciente_id,))
        consultas = cur.fetchall()
        if consultas:
            for c in consultas:
                print(f"Consulta {c[0]} - Médico: {c[1]} - Data: {c[2]} - Obs: {c[3]}")
        else:
            print("Nenhuma consulta encontrada para este paciente.")
    except Exception as e:
        print(f"Erro ao listar consultas: {e}")
    finally:
        con.close()

def relatorio_consultas_por_medico():
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT m.nome, COUNT(c.id) as total
            FROM consultas c
            JOIN medicos m ON c.medico_id = m.id
            GROUP BY m.nome
        """)
        for linha in cur.fetchall():
            print(f"{linha[0]} - {linha[1]} consultas")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    finally:
        con.close()