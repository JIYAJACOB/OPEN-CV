#MACHINE LEARNING

#OCV

#DAY 3

#QUESTION 4

#erosion

import cv2
import numpy as np

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel)
img=np.hstack((img,erosion))
cv2.imshow('dst',img)
cv2.waitKey(0)


#dialation

import cv2
import numpy as np

img = cv2.imread('j.png',0)
kernel = np.ones((2,2),np.uint8)
#erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel)
img=np.hstack((img,dilation))
cv2.imshow('dst',img)
cv2.waitKey(0)

