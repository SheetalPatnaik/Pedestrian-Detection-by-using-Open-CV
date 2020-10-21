import cv2
import time
import numpy as np

# Create our body classifier


car_classifier = cv2.CascadeClassifier("Haarcascade/cars.xml")
                                         #If this path doesnt work, download the haarcascade folder and place it in
                                         # User/Anaconda/Lib/sitepackage/cv2/data/
                                         
# Initiate video capture for video file
cap = cv2.VideoCapture('images/cars.avi')

# Loop once video is successfully loaded
while cap.isOpened():
    time.sleep(0.5)
    # Read first frame
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    
    caras=car_classifier.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=2) 
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in caras:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()