#MACHINE LEARNING

#OCV

#DAY 3

#QUESTION 1

import numpy as np
import cv2
faces=cv2.CascadeClassifier('faces.xml')
img=cv2.imread('team.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dfaces =faces.detectMultiScale(gray)
print(len(dfaces))
for (x,y,w,h) in dfaces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	eyes=cv2.CascadeClassifier('eyes.xml')
	roi_gray=gray[y:y+h,x:x+w]
	roi_color=img[y:y+h,x:x+w]
	deyes=eyes.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in deyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('dst',img)
print(gray.shape)
cv2.waitKey(0)
