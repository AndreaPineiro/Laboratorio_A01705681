# Se importan todas las librerías necesarias
import numpy as np
from random import *

# La función de convolución recibe la imagen y el kernel
def convolution(image, kernel):
    # Se obtienen los tamaños de la matriz imagen
    image_row, image_col = image.shape
    # Se obtienen los tamaños de la matriz kernel
    kernel_row, kernel_col = kernel.shape
    
    # Se crea una matriz vacía de respuesta, con el respectivo tamaño que tendrá restando el kernel + 1
    res = np.zeros((image_row - kernel_row + 1, image_col - kernel_col + 1))
    
    # Este ciclo itera para recorrer cada una de las casillas en la matriz del resultado
    for matrix_row in range (res.shape[0]):
        for matrix_col in range (res.shape[1]):
            # Inicializa la suma en 0 y para cada casilla, suma la multiplicacion del kernel con las casillas correspondientes de la matriz
            result = 0
            for k_row in range(kernel_row):
                for k_col in range(kernel_row):
                    result += image[matrix_row + k_row, matrix_col + k_col] * kernel[k_row, k_col]
            # Escribe la suma en la casilla correspondiente
            res[matrix_row, matrix_col] = result
    return res

# Aquí creo 2 números aleatorios para crear la matriz (imagen)
axis_x = randint(4,8)
axis_y = randint(4,8)

# Se genera un número aleatorio para el tamaño del filtro, (entre 2 y 4)
k_sze = randint(2,4)

# Se crea una matriz de las dimensiones anteriores, con valores enteros entre el 0 y 20
matrix = np.random.randint(21, size=(axis_x, axis_y))
# Se crea un filtro nxn con el valor random obtenido anteriormente
filter = np.random.randint(21, size=(k_sze,k_sze))

# Se imprimen las matrices de imagen y filtro
print("IMAGE:")
print(matrix)
print('\n')
print("FILTER:")
print(filter)
print('\n')

# Llama a la función convolution con la matriz y el filtro. Imprime el resultado
res = convolution(matrix,filter)
print("OUTPUT:")
print(res)