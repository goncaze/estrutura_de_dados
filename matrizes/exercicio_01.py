import os
import numpy as np

menu = """
[0] - Sair                  [1] - Criar um array 1D
[2] - Criar um array 2D     [3] - Imprimir os arrays
[4] - Operações básicas da matemática com esses vetores.
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


def criar_array2d() -> np.ndarray: ...


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
            ...
        case "3":
            os.system("cls")
            imprimir_arrays(arr_1d=array_1d)
            input()
        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case "7":
            ...
        case "8":
            ...
