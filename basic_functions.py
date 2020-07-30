import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)

#reading image
img = cv2.imread("images/pic1.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #must be odd numbers

#edge Detector
imgCanny = cv2.Canny(imgBlur,100,200)
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)#thickness
imgEroded = cv2.erode(imgDialation,kernel, iterations=1)#reversing thickness

#display
cv2.imshow("Img", img) #windowName + picture
#cv2.imshow("GrayImg", imgGray) 
#cv2.imshow("blurImg", imgBlur)
cv2.imshow("CannyImg", imgCanny)
cv2.imshow("dialationImg", imgDialation)
cv2.imshow("ErodedImg", imgEroded)
cv2.waitKey(0)
