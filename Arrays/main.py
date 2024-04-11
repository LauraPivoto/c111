import numpy as np

array = np.linspace(0, 1, 21)
print(array)

array2 = np.arange(0, 51, 2)
print(array2)

array3 = np.arange(100, 49, -2)

array4 = np.concatenate((array2, array3))
array4.sort()

print(array4)

print(np.flip(np.sort(array4)))

matriz = np.ones((3, 4))
print("Matriz 3x4 de uns:")
print(matriz)

array_1d = matriz.flatten()
print("\nArray 1-D:")
print(array_1d)


matriz = np.random.randint(1, 10, size=(3, 4))
print("Matriz:")
print(matriz)

num_linhas = matriz.shape[0]
num_colunas = matriz.shape[1]
print(num_linhas)
print(num_colunas)

total_elementos = num_linhas * num_colunas
print(total_elementos)

array = matriz.flatten()
print(array)
#O comprimento é 12, então é par.