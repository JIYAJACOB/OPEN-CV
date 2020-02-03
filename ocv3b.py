import numpy as np
import cv2
cats=cv2.CascadeClassifier('cats.xml')
img=cv2.imread('cats.jpg')
print img.shape
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dfaces=cats.detectMultiScale(gray)
print(len(dfaces))
for(x,y,w,h) in dfaces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	eyes=cv2.CascadeClassifier('eyes.xml')
	roi_gray=gray[y:y+h,x:x+w]	
	roi_color=img[y:y+h,x:x+w]	
	deyes=cats.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in deyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('dst',img)
cv2.waitKey(0)
	

