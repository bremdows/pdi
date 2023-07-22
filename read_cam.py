import cv2

"""
    Para el video mediante una camara web es necesario indicar el puerto de la cámara web
    por defecto es: 0
    Si se conecta otra nueva, obtendría el siguiente valor: 1
    etc, etc
"""
web_cam = cv2.VideoCapture(0)
while True:
    a, frame = web_cam.read()
    
    # print(frame.shape)

    frame_g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """
    Cambiar el tamaño de la resolución
    Args :
        Ancho (int)
        Alto (int)
    """
    frame_g_change = cv2.resize(frame_g, (100, 100))
    # print(frame_g_change.shape)
    """
        Seleccionar un area del video
        ROI : Region Of Interest
        El area a seleccionar se hace mediante las coordenadas [x, y]
        X, Y toman un rango de valores
    """
    frame_roi = frame_hsv[ 200 : 350, 60:300]

    cv2.imshow("Soy io - Camarita", frame)
    cv2.imshow("Soy io in BLACK AND WHITE ", frame_g)
    cv2.imshow(" Frame in HSV ", frame_hsv)
    
    # Imagen cambiada
    cv2.imshow(" Humilde en pequeño ", frame_g_change)
    # Area seleccionada
    cv2.imshow(" ROI of my face ", frame_roi)
    
    if cv2.waitKey(30) & 0XFF == ord("q") :
        print("Cerrando la web CAM") 
        break
cv2.destroyAllWindows()
"""
    Luego de usar la web CAM esta se queda prendida por defecto, para apagarla se usa la función release 
"""
web_cam.release()