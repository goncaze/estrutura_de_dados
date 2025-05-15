import numpy as np
import os

os.system("cls")

# print(np.__version__)
print()

array_um_d = np.array([1, 2, 3, 4, 5])  # LISTA
arr = np.array((1, 2, 3, 4, 5))  # TUPLA
print(array_um_d)
print(f"{type(array_um_d) = }")

print()

lista = [12, 23, 34, 45, 56]
print(lista)
print(f"{type(lista) = }")

print()

array_zero_d = np.array(180)
print(array_zero_d)
print(f"{type(array_zero_d) = }")

print()

array_dois_d = np.array([[1, 2], [7, 9]])
print(array_dois_d)
print(f"{type(array_dois_d) = }")

print()

array_tres_d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(array_tres_d)
print(f"{type(array_tres_d) = }")

print()

print(f"{array_zero_d.ndim = }")
print(f"{array_um_d.ndim = }")
print(f"{array_dois_d.ndim = }")
print(f"{array_tres_d.ndim = }")

print()


# [1] - Criar um array 1D
array_1d = np.array([1, 2, 3])

# [2] - Criar um array 2D
array_2d = np.array([[1, 2, 3], [3, 2, 1]])
