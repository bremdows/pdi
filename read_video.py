import cv2

# * Obtener el video
video = cv2.VideoCapture("./media/alga3.mp4")

while True :
    # * Leer el video
    a, frame = video.read()
    # * Mostrar video
    cv2.imshow(" Alguitas loquitas", frame)
    
    # * Cerrar el video con cualquier tecla 
    """
    0xFF habilita el teclado para poder usar las teclas
    ord("q") se especifica la tecla q para cerrar el video abierto
    waitKey(number)
        number (int) : Define la velocidad con la cual se reproduce el video (define los frames por segundo) fps
    """
    if cv2.waitKey(30) & 0xFF == ord("q") :
        print("Gracias por ver el video")
        break
cv2.destroyAllWindows()
