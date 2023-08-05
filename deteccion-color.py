import cv2
import numpy as np

def empty(a):
    pass

path = './media/img/points.jpg'

cv2.namedWindow("Barras")
cv2.resizeWindow("Barras",500,500)
"""
Rango de valores para el formato HSV(0, 180)
Rango de valores para el formato RGB(0, 255)
"""
cv2.createTrackbar("Hue Min","Barras",0,180,empty)
cv2.createTrackbar("Hue Max","Barras",0,180,empty)
cv2.createTrackbar("Sat Min","Barras",0,255,empty)
cv2.createTrackbar("Sat Max","Barras",0,255,empty)
cv2.createTrackbar("Val Min","Barras",0,255,empty)
cv2.createTrackbar("Val Max","Barras",0,255,empty)
cv2.createTrackbar("Kernel", "Barras",0, 9, empty)
cv2.createTrackbar("Iteraciones", "Barras", 0, 3, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Barras")
    h_max = cv2.getTrackbarPos("Hue Max", "Barras")
    s_min = cv2.getTrackbarPos("Sat Min", "Barras")
    s_max = cv2.getTrackbarPos("Sat Max", "Barras")
    v_min = cv2.getTrackbarPos("Val Min", "Barras")
    v_max = cv2.getTrackbarPos("Val Max", "Barras")
    kernel = cv2.getTrackbarPos("Kernel","Barras")
    iteraciones = cv2.getTrackbarPos("Iteraciones", "Barras")
    
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    img_erode = cv2.erode(mask, np.ones((kernel, kernel), np.uint8), iterations=iteraciones )
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Img", img)
    cv2.imshow("Img-HSV", imgHSV)
    cv2.imshow("Img-mask", mask)
    cv2.imshow("Img-Erode", img_erode)
    cv2.imshow("Img-result", imgResult)
        
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()