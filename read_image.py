import cv2

# * Leer la imagen
img = cv2.imread("./media/lena.png")
"""
    Obtener las dimensiones y la profundidad de la imagen
    AnchoxAltoxCapa
"""
print(img.shape)
# img_g = cv2.colorChange("./media/lena.png",)

# * Mostrar la imagen
cv2.imshow(" Lena My Baby ", img)

# * Para poder cerrar la imagen
"""
El 0 es para imagenes (static)
"""
cv2.waitKey(0)
cv2.destroyAllWindows()
print("La imagen se ha cerrado")



"""
Guardar la imagen modificada

cv2.write("video_hsv.mp4", variable_image)
"""


def main() :
    pass


if __name__ == "__main__" :
    main()