from scripts.img_to_matrix import img_to_matrix
from scripts.matrix_to_img import matrix_to_img
from scripts.apply_filter import filtro_pixel, monta_kernel

img_to_matrix('imagem/image.jpg', (600, 600))  # cria a matriz

kernel = [[1, 2, 1],
          [2, 4, 2],
          [1, 2, 1]]

monta_kernel(kernel)  # cria o kernel

filtro_pixel('matriz/matriz.txt', 'kernel.txt')

matrix_to_img('matriz/matriz_filtrada.txt', 'resultado.jpg')  # cria a imagem
