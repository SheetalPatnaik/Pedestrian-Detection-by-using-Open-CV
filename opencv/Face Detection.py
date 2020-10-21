# -*- coding: utf-8 -*-

import numpy as np
import cv2

capture=cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
                                 #If this path doesnt work, download the haarcascade folder and place it in
                                 # User/Anaconda/Lib/sitepackage/cv2/data/

while True:
    ret,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("frame",frame)
        if cv2.waitKey(20) & 0xFF== ord('q'):
            cv2.release()
            cv2.destroyAllWindows()  
            break
        
    
  
     