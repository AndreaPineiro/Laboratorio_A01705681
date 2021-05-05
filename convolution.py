# Se importan todas las librerías necesarias
import numpy as np
from random import *

# Esta función auxiliar recibe un fragmento de la imagen y realiza
# las multiplicaciones para el resultado de la casilla
def conv_aux(fragment, kernel):
    k_row, k_col = kernel.shape
    result = 0
    for row in range(k_row):
        for col in range(k_col):
            result += fragment[row, col] * kernel[row, col]
    
    return result

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
            res[matrix_row, matrix_col] = conv_aux(image[matrix_row: matrix_row + kernel_row, matrix_col: matrix_col + kernel_col], kernel)
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