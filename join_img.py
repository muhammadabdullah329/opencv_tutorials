import cv2
import numpy as np

img = cv2.imread("images/pic1.jpg")
imgGray = cv2.GaussianBlur(img,(7,7),0)

hor = np.hstack((img,imgGray))
ver = np.vstack((img,imgGray))

cv2.imshow("display",hor)
cv2.imshow("display1",ver)
cv2.waitKey(0)