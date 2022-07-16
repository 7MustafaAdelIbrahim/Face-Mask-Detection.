# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 20:20:14 2022

@author: 7mustafa
"""

import keras
from facedetection_v9 import FaceDetector

import cv2
import numpy as np
from keras.preprocessing.image import img_to_array

detector = FaceDetector()

model = keras.models.load_model('mask_detection_v3.h5')


cap = cv2.VideoCapture(0)
while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    frame,faces = detector.get_faces(frame,path=False)
    
    
    imageHeight, imageWidth = frame.shape[:-1]
    scale = 1 # this value can be from 0 to 1 (0,1] to change the size of the text relative to the image
    fontScale = min(imageWidth,imageHeight)/(600/scale)



    for face, box in faces:
        face = cv2.resize(face,(128,128))
        face = img_to_array(face)/255.0
        face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
        face = np.array([face])

        Masked = np.argmax(model.predict(face))
        

        if Masked:
            cv2.putText(frame,'No Mask', (box[0], box[1]-5), cv2.FONT_HERSHEY_SIMPLEX, fontScale, (255,0,0), 2)
            cv2.rectangle(frame, (box[0],box[1]), (box[2],box[3]), (255,0,0), 3)
        else:
            cv2.putText(frame,'Masked', (box[0], box[1]-5), cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0,255,0), 2)
            cv2.rectangle(frame, (box[0],box[1]), (box[2],box[3]), (0,255,0), 3)
            
    cv2.imshow('Mask Detector',cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()       
