'''
    Programmer....: (C) Marcos Nhaga
    Date..........: 05/02/2025
    Observations..: First program in OpenCV
'''

import cv2 as cv

webcam = cv.VideoCapture(0)

if not webcam.isOpened:
    print("Unable to access the webcam!")
    exit()
    
while True:
    retorno, frame = webcam.read()
    
    if not retorno:
        print("Error capturing webcam.")
        break
    
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('Original Image', frame)
    cv.imshow('Gray Image', frameGray)
    
    if cv.waitKey(1) == ord('q'):
        break
    
webcam.release()
cv.destroyAllWindows()