from postgres.operacoes_bd import Operacoes


def menu():
    print("-- MENU POSTGRES -- ")
    print("\n 1 - Inserir aluno")
    print("\n 2 - Remover aluno")
    print("\n 3 - Buscar aluno")
    print("\n 4 - Sair")
    op = int(input("\n Digite sua opção:"))

    if op == 1:
        inserir()
    if op == 2:
        remover()
    if op == 3:
        buscar()
    if op == 4:
        exit()


def inserir():
    operacoes = Operacoes()
    nome_aluno = str(input("Digite o nome do aluno: "))
    matricula_aluno = int(input("Digite a matricula do aluno: "))

    operacoes.salvar_aluno(nome_aluno, matricula_aluno)


def buscar():
    operacoes = Operacoes()
    nome_aluno = input("Digite o nome do alubo a ser buscado:")
    operacoes.buscar_aluno(nome_aluno)


def remover():
    operacoes = Operacoes()
    nome_aluno = input("Digite o nome do alubo a ser removido:")
    operacoes.remover_aluno(nome_aluno)


menu()
