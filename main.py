from database.db import criar_tabelas
from utils.importer import importar_medicos_csv, importar_pacientes_json
from services import medico_service, paciente_service, consulta_service

def menu():
    while True:
        print("\n--- Menu Clínica Popular Vida+ ---")
        print("1. CRUD Pacientes")
        print("2. CRUD Médicos")
        print("3. Agendar Consulta")
        print("4. Listar Consultas de Paciente")
        print("5. Relatório por Médico")
        print("0. Sair")
        op = input("Escolha: ")

        if op == "1":
            print("a. Cadastrar\nb. Listar\nc. Atualizar\nd. Deletar")
            acao = input("Escolha: ").lower()
            if acao == "a": paciente_service.cadastrar_paciente()
            elif acao == "b": paciente_service.listar_pacientes()
            elif acao == "c": paciente_service.atualizar_paciente()
            elif acao == "d": paciente_service.deletar_paciente()
        elif op == "2":
            print("a. Cadastrar\nb. Listar\nc. Atualizar\nd. Deletar")
            acao = input("Escolha: ").lower()
            if acao == "a": medico_service.cadastrar_medico()
            elif acao == "b": medico_service.listar_medicos()
            elif acao == "c": medico_service.atualizar_medico()
            elif acao == "d": medico_service.deletar_medico()
        elif op == "3":
            consulta_service.agendar_consulta()
        elif op == "4":
            consulta_service.listar_consultas_paciente()
        elif op == "5":
            consulta_service.relatorio_consultas_por_medico()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    criar_tabelas()
    importar_medicos_csv()
    importar_pacientes_json()
    menu()