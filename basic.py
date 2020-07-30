import cv2
import time 
import numpy as np

kernel= np.ones((5,5),np.uint8)
#reading image
img = cv2.imread("images/pic1.jpg")

#display
cv2.imshow("Output", img) #windowName + picture
cv2.waitKey(0)

#reading video
cap = cv2.VideoCapture("images/vid1.mp4")

#for webcam
'''
cap = cv2.VideoCapture(0)
cap.set(3,640)	#width
cap.set(4,480)	#height
cap.set(10,100)	#brightness
'''
last_time = time.time()
while True:
	success, img = cap.read()
	#img = cv2.UMat(img)
	'''
	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray
	imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #must be odd numbers

	#edge Detector
	imgCanny = cv2.Canny(imgBlur,100,200)
	imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)#thickness
	imgEroded = cv2.erode(imgDialation,kernel, iterations=1)
	'''
	fps = round(1/(time.time()-last_time),2)
	img = cv2.putText(img,str(fps),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
	last_time= time.time()
	
	cv2.imshow("Video",img)
	
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break