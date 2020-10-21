# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:49:39 2020

@author: anish
"""

import numpy as np
import cv2

capture=cv2.VideoCapture(0)

while True:
    ret,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(frame)
    cv2.imshow("normal",frame)
    cv2.imshow("gray",gray)
    cv2.imshow("NEGTIVE",invert)
    if cv2.waitKey(20) & 0xFF== ord('q'):
        break
    
  
     