import os  # Módulo para operações do S.O.

# LISTA DE VEGETAIS
lista_vegetais = ["Berinjela", "Chuchu", "Maxixe"]


# imprime o título LISTA DE VEGETAIS
def imprimir_titulo():
    titulo = "LISTA DE VEGETAIS!"
    print(f"|{format('','.^70')}|")
    print(f"|{format(titulo,'.^70')}|")
    print(f"|{format('','.^70')}|")


# Programação do menu contendo as operações disponíveis
menu = """
    [1] - Criar/recriar         \t[2] - Inserir
    [3] - Excluir               \t[4] - Alterar
    [5] - Listar                \t[6] - Esvaziar
    [7] - Pesquisar             \t[8] - Tamanho (comprimento)
    [0] - Encerrar o app
"""


# [2] - Inserir
def inserir(lista: list) -> None:
    vegetal = input("Digite o nome do vegetal: ")
    lista.append(vegetal)


# [3] - Excluir
def excluir(lista: list, index: int) -> str:
    item_excluido = lista.pop(index)
    return item_excluido


# [5] - Listar/Apresentar itens da lista
def imprimir_lista(lista: list) -> None:
    print()  # Imprimir uma linha vazia
    numero = 0
    for item in lista:
        print(f"\t[{numero}] - {item}")  # Imprimir conteúdo da lista
        numero += 1


# [8] - Tamanho (comprimento)
def comprimento(lista: list) -> int:
    comprimento = len(lista)
    return comprimento


# Controlar menu
def controle_menu(menu: str, lista: list):  # função para controlar menu
    while True:  # laço de repetição
        os.system("cls")  # limpar a tela
        imprimir_titulo()  # imprime o título LISTA DE VEGETAIS
        print(menu)  # apresentar menu na tela

        # Capturar a seleção do usuário
        selecao = input("\tSelecione uma opção: ")

        # Determinar a seleção desejada e invocar a
        # respctiva operação desejada.
        match selecao:
            case "0":  # Se seleção igual à '0'
                os.system("cls")  # Limpar tela
                print("Saindo do app!")  # Aviso de encerramento
                input()  # Aguardar o usuário pressionar ENTER
                break  # Interromper loop while
            case "1":  # Criar
                lista = []  # Reatribuindo uma lista vazia
                os.system("cls")  # Limpar tela
                print("A lista de vegetais foi recriada! ")
                input()
            case "2":  # Inserir
                os.system("cls")  # Limpar tela
                inserir(lista)
                print("Vegetal inserido na lista! ")
                input()
            case "3":  # Excluir
                os.system("cls")  # Limpar tela
                imprimir_lista(lista)
                indice_vegetal = input("\nNumero do vegetal para excluir: ")
                indice_vegetal = int(indice_vegetal)
                vegetal = excluir(lista, indice_vegetal)
                print(f"\nItem {vegetal} excluído da lista! ")
                input()
            case "4":  # Alterar
                ...  # Tarefa para a turma desenvolver
            case "5":  # Listar (apresentar)
                os.system("cls")  # Limpar tela
                print(format("APRESENTAÇÃO DA LISTA DE VEGETAIS!", ".^70"))
                imprimir_lista(lista)
                input()
            case "6":  # Esvaziar (limpar a lista)
                os.system("cls")  # Limpar tela
                lista.clear()  # Limpando a lista vazia
                print("Limpeza da lista, concluída! ")
                input()
            case "7":  # Pesquisar
                ...  # Tarefa para a turma desenvolver
            case "8":  # Comprimento da lista
                os.system("cls")  # Limpar tela
                compr = comprimento(lista)
                print(f"Comprimento da lista: {compr}")
                input()


if __name__ == "__main__":
    # Invocar a função de menu
    controle_menu(menu, lista_vegetais)
