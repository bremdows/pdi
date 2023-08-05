import cv2
import numpy as np

img = cv2.imread("./media/img/ez_malo.jpg") # Imagen original

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Imagen a escala de grises

# * Canny() sirve para detectar los bordes de una imagen
"""
    Canny, los parámetros definen el nivel de detalle
"""
img_canny = cv2.Canny(img_gray, 100, 200) #b Imagen Canny
img_canny = cv2.Canny(img, 150, 200) #b Imagen Canny

# Aplicando los filtros morfologicos

"""
    Generando una matriz de unos con sus respectivas dimensiones 3x3, 5x5, 7x7
    Luego se define el formato de trabajo de la imagen (8 bits) => np.uint8
"""
kernel = np.ones((3, 3), np.uint8)

"""
    Tamaño del kernel es DP a la eliminación de pixeles (afecta al resultado)
    Las iteraciones define la cantidad de veces que el kernel recorrera la imagen
    Iteraciones = 2, primero recorrer la imagen original y en la segunda recorrera el resultado que se obtuvo luego de pasar pro el primero filtro
"""
img_dilate = cv2.dilate(img_canny, kernel, iterations=1)
img_erode = cv2.erode(img_dilate, kernel, iterations=1)
for i in range(1, 4) :
    img_erode = cv2.erode(img_dilate, kernel, iterations=i)
    cv2.imwrite(f"Erosion-{i}.png", img_erode)


# Mostrando la imagen

# cv2.imshow("Lunar - BGR", img) 
# cv2.imshow("Lunar - GRAY", img_gray) 
# cv2.imshow("Lunar Canny", img_canny)
# cv2.imshow("Lunar - Dilatado", img_dilate)
# cv2.imshow("Lunar - Erosionado", img_erode)


cv2.waitKey(0)
cv2.destroyAllWindows()