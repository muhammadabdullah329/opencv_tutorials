import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt,True)
            #print(perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
 
            if objCorner ==3: objectType ="Tri"
            elif objCorner == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCorner>4: objectType= "Circles"
            else:objectType="None"
 
 
 
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
	


img = cv2.imread("images/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,150,150)

getContours(imgCanny)

cv2.imshow("display",imgCanny)
cv2.imshow("display1",imgContour)
cv2.waitKey(0)