import cv2
import numpy as np

def empty(a):
    pass

path = cv2.VideoCapture(0)

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
cv2.createTrackbar("Erode Ker", "Barras",0, 12, empty)
cv2.createTrackbar("Erode Iter", "Barras", 0, 12, empty)
cv2.createTrackbar("Dilate Ker", "Barras",0, 12, empty)
cv2.createTrackbar("Dilate Iter", "Barras", 0, 12, empty)

while True:

    _, img = path.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Barras")
    h_max = cv2.getTrackbarPos("Hue Max", "Barras")
    s_min = cv2.getTrackbarPos("Sat Min", "Barras")
    s_max = cv2.getTrackbarPos("Sat Max", "Barras")
    v_min = cv2.getTrackbarPos("Val Min", "Barras")
    v_max = cv2.getTrackbarPos("Val Max", "Barras")
    erode_kernel = cv2.getTrackbarPos("Erode Ker","Barras")
    erode_iter = cv2.getTrackbarPos("Erode Iter", "Barras")
    dilate_kernel = cv2.getTrackbarPos("Dilate Ker","Barras")
    dilate_iter = cv2.getTrackbarPos("Dilate Iter", "Barras")
    
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    img_erode = cv2.erode(mask, np.ones((erode_kernel, erode_kernel), np.uint8), iterations=erode_iter )
    img_dilate = cv2.dilate(mask, np.ones((dilate_kernel, dilate_kernel), np.uint8), iterations=dilate_iter)
    imgResult = cv2.bitwise_and(img,img,mask=img_dilate)

    cv2.imshow("Img", img)
    cv2.imshow("Img-HSV", imgHSV)
    cv2.imshow("Img-mask", mask)
    cv2.imshow("Img-Erode", img_erode)
    cv2.imshow("Img-Dilate", img_dilate)
    cv2.imshow("Img-result", imgResult)
        
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()