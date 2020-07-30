import cv2
import numpy as np
 
img = cv2.imread("images/doc.jpg")
 
width,height = 260,250
pts1 = np.float32([[80,155],[340,108],[137,400],[435,329]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

#cv2.imshow("imgOutput",imgOutput)

imgOutput = cv2.circle(imgOutput, (50,50),30,(0,0,255),cv2.FILLED)
imgOutput = cv2.circle(imgOutput, (50,50),10,(0,255,255),cv2.FILLED)
imgOutput = cv2.rectangle(imgOutput,(100,100),(200,200),(255,0,0),cv2.FILLED)
cv2.putText(imgOutput,"KHAWAR", (120,150),cv2.FONT_HERSHEY_COMPLEX,.5,(0,255,255),2)


cv2.imshow("imgOutput1",imgOutput)

matrix = cv2.getPerspectiveTransform(pts2,pts1)
imgOutput = cv2.warpPerspective(imgOutput,matrix,(img.shape[1],img.shape[0]))


outputgray = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(outputgray, 10, 255, cv2.THRESH_BINARY_INV)

img1_bg = cv2.bitwise_and(img,img,mask = mask)

final = cv2.add(img1_bg,imgOutput)

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
#cv2.imshow("Output1",mask)
cv2.imshow("Output2",final)

cv2.waitKey(0)