#MACHINE LEARNING

#DAY 3

#OCV

#QUESTION 2

import numpy as np
import cv2
faces=cv2.CascadeClassifier('cars.xml')
img=cv2.imread('car.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dfaces=faces.detectMultiScale(gray)
print(len(dfaces))
for(x,y,w,h) in dfaces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cars=cv2.CascadeClassifier('cars.xml')
	roi_gray=gray[y:y+h,x:x+w]	
	roi_color=img[y:y+h,x:x+w]	
	deyes=cars.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in deyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('dst',img)
cv2.waitKey(0)
	
