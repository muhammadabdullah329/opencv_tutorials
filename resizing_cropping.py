import cv2
import numpy as np

#reading image
img = cv2.imread("images/pic1.jpg")

print(img.shape)

imgResize = cv2.resize(img, (150,200))

imgCropped = img[0:200,50:250]

#display
cv2.imshow("Img", img) #windowName + picture
cv2.imshow("ImgResize", imgResize)
cv2.imshow("Imgcropped", imgCropped)
cv2.waitKey(0)
