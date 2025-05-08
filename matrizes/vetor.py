import numpy as np

# print(np.__version__)
print()

arr = np.array([1, 2, 3, 4, 5])  # LISTA
arr = np.array((1, 2, 3, 4, 5))  # TUPLA
print(arr)
print(f"{type(arr) = }")

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
