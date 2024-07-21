import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/pi/pyPrograms/camera/haarcascade_frontalface_alt2.xml')
#cat_cascade = cv2.CascadeClassifier('/home/pi/pyProgram/camera/haarcascade_frontalcatface_extended.xml')
cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    #faces = cat_cascade.detectMultiScale(gray, 1.1, 3)

# Detects cat faces in the input image


    

    for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x + w, y + h), (190, 0, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        # uwaga! jeśli w kodzie widzisz "amp;" po znaku and to usuń ten kawałek.
        # WordPress sam to dopisuje :(
        break

cap.release()
cv2.destroyAllWindows()
