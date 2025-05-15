import os
import numpy as np

menu = """
[0] - Sair                  [1] - Criar um array 1D
[2] - Criar um array 2D     [3] - Imprimir os arrays
[4] - Adição                [5] - Subtração
[6] - Multiplicação         [7] - Divisão  
\n
"""

menu_array = """
[d] - Desistir
[i] - Inserir um número
[c] - Concluir
\n
"""

array_1d: np.ndarray = None
array_2d: np.ndarray = None


def criar_array1d() -> np.ndarray:
    lista = []
    while True:
        os.system("cls")
        print(menu_array)

        opc = input("Opção: ")

        match opc:
            case "d":
                break
            case "i":
                numero = input("\nNúmero: ")
                lista.append(float(numero))
            case "c":
                return np.array(lista)


def criar_array2d() -> np.ndarray:
    linha: int = int(input("\n Nº de linhas:"))
    coluna: int = int(input("\n Nº de colunas:"))

    lista: list = []

    for l in range(linha):
        linha: list = []
        for c in range(coluna):
            linha.append(float(input(f"[{l},{c}] = ")))
        lista.append(linha)

    return np.array(lista)


def imprimir_arrays(arr_1d: np.ndarray = None, arr_2d: np.ndarray = None):
    print()
    print(f"{type(arr_1d) = }")
    print()
    print(f"{arr_1d}")
    print()
    print(f"{type(arr_2d) = }")
    print()
    print(f"{arr_2d}")
    print()


def somar(arr_1d: np.ndarray = 0, arr_2d: np.ndarray = 0) -> tuple[np.array]:
    valor = float(input("Somar valor:  "))
    return arr_1d + valor, arr_2d + valor


def subtrair(arr_1d: np.ndarray = 0, arr_2d: np.ndarray = 0) -> tuple[np.array]:
    valor = float(input("subtrair valor:  "))
    return arr_1d - valor, arr_2d - valor


def multiplicar(arr_1d: np.ndarray = 0, arr_2d: np.ndarray = 0) -> tuple[np.array]:
    valor = float(input("multiplicar valor:  "))
    return arr_1d * valor, arr_2d * valor


def dividir(arr_1d: np.ndarray = 0, arr_2d: np.ndarray = 0) -> tuple[np.array]:
    valor = float(input("dividir valor:  "))
    return arr_1d / valor, arr_2d / valor


while True:
    os.system("cls")

    print(menu)

    opc = input("Opção: ")

    match opc:
        case "0":
            break
        case "1":
            array_1d = criar_array1d()
        case "2":
            os.system("cls")
            array_2d = criar_array2d()
        case "3":
            os.system("cls")
            imprimir_arrays(arr_1d=array_1d, arr_2d=array_2d)
            input()
        case "4":
            array_1d, array_2d = somar(arr_1d=array_1d, arr_2d=array_2d)
            imprimir_arrays(arr_1d=array_1d, arr_2d=array_2d)
            input()
        case "5":
            array_1d, array_2d = subtrair(arr_1d=array_1d, arr_2d=array_2d)
            imprimir_arrays(arr_1d=array_1d, arr_2d=array_2d)
            input()
        case "6":
            array_1d, array_2d = multiplicar(arr_1d=array_1d, arr_2d=array_2d)
            imprimir_arrays(arr_1d=array_1d, arr_2d=array_2d)
            input()
        case "7":
            array_1d, array_2d = dividir(arr_1d=array_1d, arr_2d=array_2d)
            imprimir_arrays(arr_1d=array_1d, arr_2d=array_2d)
            input()
