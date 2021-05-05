import numpy as np
from random import *

def padding(image, padding_size):
    # Se obtienen los tamaños de la matriz imagen
    image_row, image_col = image.shape

    padded_matrix = np.zeros((image_row + padding_size*2, image_col + padding_size*2))

    padded_matrix[padding_size:padding_size + image_row, padding_size:padding_size + image_col] = image
    
    return padded_matrix


# Aquí creo 2 números aleatorios para crear la matriz (imagen)
axis_x = randint(4,8)
axis_y = randint(4,8)

# Se genera un número aleatorio para el tamaño del padding, (entre 1 y 4)
padding_size = randint(1,4)

# Se crea una matriz de las dimensiones anteriores, con valores enteros entre el 0 y 20
matrix = np.random.randint(21, size=(axis_x, axis_y))

# Se imprimen las matrices de imagen y filtro
print('\n')
print("PADDING:", padding_size)
print('\n')

# Llama a la función convolution con la matriz y el filtro. Imprime el resultado
res = padding(matrix, padding_size)
print("OUTPUT:")
print(res)