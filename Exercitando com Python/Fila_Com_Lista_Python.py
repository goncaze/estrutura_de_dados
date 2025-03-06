import os


# imprime o titulo
def imprimir_titulo():
    titulo = "FILA DE ATENDIMENTO!"
    print(f"|{format('','.^70')}|")
    print(f"|{format(titulo,'.^70')}|")
    print(f"|{format('','.^70')}|")


# Programacao do menu contendo as operacoes disponi­veis
menu = """
    [1] - Criar/recriar         \t[2] - Enfileirar
    [3] - Denfileirar           \t[4] - Comprimento
    [5] - Esvaziar              \t[6] - Proximo
    [7] - Ultimo                \t[8] - Ver fila
    [0] - Encerrar o app
"""


# [1] - CRIAR/RECRIAR FILA DE ATENDIMENTO
def criar(fila: list):
    fila = list()


# [2] - enfileirar
def enfileirar(fila: list) -> str:
    try:  # tente executar o código abaixo
        cliente = input("Digite o nome do cliente: ")
        fila.append(cliente)  # Em caso de sucesso...
        return f"Cliente {cliente} na fila!"  # Retorne essa mensagem
    except Exception:  # Em caso de erro...
        return f"Cliente {cliente} não inserido na fila!"  # Retorne essa mensagem


# [3] - Desinfileirar
def desinfileirar(fila: list) -> str:
    try:  # tente executar o código abaixo
        elemento_removido = fila.pop(0)  # Em caso de sucesso...
        return f"{elemento_removido} em atendimento! "  # Retorne essa mensagem
    except Exception:  # Em caso de erro...
        return "Ninguém entrou em atendimento!"  # Retorne essa mensagem


# [4] - Tamanho (comprimento)
def comprimento(fila: list) -> int:
    comprimento = len(fila)
    return comprimento


# [5] - Esvaziar/Limpar
def esvaziar(fila: list):
    fila.clear()


# [6] - Proximo
def proximo(fila: list):
    proximo = fila[0] if len(fila) > 0 else ""
    print(f"Proximo: {proximo}")


# [7] - Ultimo
def ultimo(fila: list):
    ultimo = fila[-1] if len(fila) > 0 else ""
    print(f"Ultimo: {ultimo}")


# [8] - Apresentar itens da fila
def imprimir(fila: list) -> None:
    print()  # Imprimir uma linha vazia
    numero = 0
    for elemento in fila:
        print(f"\t[{numero}] - {elemento}")  # Imprimir conteudo da fila
        numero += 1


# Controlar menu
def controle_menu(menu: str, fila: list):  # funcao para controlar menu
    while True:  # laco de repeticao
        os.system("cls")  # limpar a tela
        imprimir_titulo()  # imprime o titulo
        print(menu)  # apresentar menu na tela

        # Capturar a selecao do usuario
        selecao = input("\tSelecione uma opcao: ")

        # Determinar a selecao desejada e invocar a
        # respctiva operacao desejada.
        match selecao:
            case "0":  # Se selecao igual a  '0'
                os.system("cls")  # Limpar tela
                print("Saindo do app!")  # Aviso de encerramento
                input()  # Aguardar o usuario pressionar ENTER
                break  # Interromper loop while
            case "1":  # Criar
                criar(fila)  # Reatribuindo uma fila vazia
                os.system("cls")  # Limpar tela
                print("A fila de atendimento foi recriada! ")
                input()
            case "2":  # enfileirar
                os.system("cls")  # Limpar tela
                print(enfileirar(fila))
                input()
            case "3":  # Desinfileirar
                os.system("cls")  # Limpar tela
                print(desinfileirar(fila))
                input()
            case "4":  # Comprimento da fila
                os.system("cls")  # Limpar tela
                compr = comprimento(fila)
                print(f"Comprimento da fila: {compr}")
                input()
            case "5":  # Esvaziar (limpar a fila)
                os.system("cls")  # Limpar tela
                esvaziar(fila)  # Limpando a fila vazia
                print("Fila esvaziada! ")
                input()
            case "6":  # Proximo da fila
                os.system("cls")  # Limpar tela
                print(format("PROXIMO DA FILA!", ".^70"))
                proximo(fila)
                input()
            case "7":  # Ultimo da fila
                os.system("cls")  # Limpar tela
                print(format("ULTIMO DA FILA!", ".^70"))
                ultimo(fila)
                input()
            case "8":  # Imprimir fila
                os.system("cls")  # Limpar tela
                imprimir(fila)
                input()


fila = ["Saci", "Kurupira", "Garantido", "Caprichoso"]

if __name__ == "__main__":
    # Invocar a funcao de menu
    controle_menu(menu, fila)
