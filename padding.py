import numpy as np
from random import *
from convolution import convolution

def padding(image, padding_size, kernel):
    # Se obtienen los tamaños de la matriz imagen
    image_row, image_col = image.shape

    padded_matrix = np.zeros((image_row + padding_size*2, image_col + padding_size*2))

    padded_matrix[padding_size:padding_size + image_row, padding_size:padding_size + image_col] = image
    
    return convolution(padded_matrix, kernel)


# Aquí creo 2 números aleatorios para crear la matriz (imagen)
axis_x = randint(4,8)
axis_y = randint(4,8)

# Se genera un número aleatorio para el tamaño del padding, (entre 1 y 4)
padding_size = randint(1,4)

# Se genera un número aleatorio para el tamaño del filtro, (entre 2 y 4)
k_sze = randint(2,4)

# Se crea una matriz de las dimensiones anteriores, con valores enteros entre el 0 y 20
matrix = np.random.randint(21, size=(axis_x, axis_y))

# Se crea un filtro nxn con el valor random obtenido anteriormente
kernel = np.random.randint(21, size=(k_sze,k_sze))

# Se imprimen las matrices de imagen y filtro
print('\n')
print("IMAGE:")
print(matrix)
print('\n')
print("FILTER:")
print(kernel)
print('\n')
print("PADDING:", padding_size)
print('\n')

# Llama a la función convolution con la matriz y el filtro. Imprime el resultado
res = padding(matrix, padding_size, kernel)
print("OUTPUT:")
print(res)