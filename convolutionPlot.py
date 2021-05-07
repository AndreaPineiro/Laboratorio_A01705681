# Se importan todas las librerías necesarias
import numpy as np
from random import *
import cv2
import matplotlib.pyplot as plt

# La función de convolución recibe la imagen y el kernel
def convolution(image, kernel, verbose=False):
    if len(image.shape) == 3:
        print("Found 3 Dimensions: {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Chanel. Shape {}".format(image.shape))
    else:
        print("Image Shape: {}".format(image.shape))

    # Se obtienen los tamaños de la matriz imagen
    image_row, image_col = image.shape
    # Se obtienen los tamaños de la matriz kernel
    kernel_row, kernel_col = kernel.shape
    
    # Se crea una matriz vacía de respuesta, con el respectivo tamaño que tendrá restando el kernel + 1
    res = np.zeros((image_row - kernel_row + 1, image_col - kernel_col + 1))
    
    # Este ciclo itera para recorrer cada una de las casillas en la matriz del resultado
    for matrix_row in range (res.shape[0]):
        for matrix_col in range (res.shape[1]):
            #np.sum suma el resultado después de hacer la multiplicacion de ambas matrices.
            res[matrix_row, matrix_col] = np.sum(kernel * image[matrix_row: matrix_row + kernel_row, matrix_col: matrix_col + kernel_col])
    
    # Se realiza el plot de la Imagen
    if verbose:
        plt.imshow(res, cmap='gray')
        plt.title("Output Image Using {}X{} Kernel".format(kernel_row, kernel_col))
        plt.show()

    return res

if __name__ == '__main__':
    # Se obtiene la imagen con cv2 y se inicializa la matriz del kernel
    image = cv2.imread("casa.jfif")
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Se manda llamar la función de convolucion con la imagen y el kernel
    image = convolution(image, kernel, True)