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
    
    cv.imshow('Image Captured by Webcam', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
    
webcam.release()
cv.destroyAllWindows()