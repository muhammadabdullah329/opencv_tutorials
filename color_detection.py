import cv2
import numpy as np
'''
cap = cv2.VideoCapture(0)
cap.set(3,640)	#width
cap.set(4,480)	#height
cap.set(10,150)	#brightness
'''
def empty(a):
	pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,480)

cv2.createTrackbar("Hue Min","Trackbars",111,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",125,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",113,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",217,255,empty)
cv2.createTrackbar("Val Min","Trackbars",26,255,empty)
cv2.createTrackbar("Val Max","Trackbars",95,255,empty)

while True:

	img = cv2.imread("images/img.jpg")
	img = cv2.resize(img, (0,0), None, 0.2,0.2)
	#success, img = cap.read()
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
	h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
	s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
	s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
	v_min = cv2.getTrackbarPos("Val Min","Trackbars")
	v_max = cv2.getTrackbarPos("Val Max","Trackbars")

	#print(h_min,h_max,s_min,s_max,v_min,v_max)
	
	lower = np.array([h_min,s_min,v_min])
	upper = np.array([h_max,s_max,v_max])
	mask = cv2.inRange(imgHSV,lower,upper)
	imgResult=cv2.bitwise_and(img,img,mask=mask)

	cv2.imshow("display",img)
	cv2.imshow("display1",imgHSV)
	cv2.imshow("mask",mask)
	cv2.imshow("result",imgResult)
	
	cv2.waitKey(1)