import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

img[:] = 255,0,0  					#whole image
#img[100:300,200:300] = 255,0,0		#selected pixels

#img , coordinates, rgb/bgr , thickness
cv2.line(img, (0,0),(img.shape[1],img.shape[0]),(0,255,0),3) 

cv2.rectangle(img,(0,0),(250,300),(0,0,255),1)
cv2.rectangle(img,(0,0),(150,200),(0,0,200),cv2.FILLED)

cv2.circle(img,(400,50),30,(255,255,0),5)

#img ,text, coordinates, font,scale, rgb/bgr , thickness
cv2.putText(img," OPENCV ", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)

#display
cv2.imshow("Img", img)
cv2.waitKey(0)
