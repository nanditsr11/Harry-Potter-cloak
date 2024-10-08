import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)     
background = 0

for i in range(50):
    ret, background = cap.read()

while(cap.isOpened()): 
    ret, img = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255]) # values is for red colour Cloth
    # upper_red = np.array([0, 0, 0])
    mask1 = cv2.inRange(hsv, lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red =  np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    #Combining the masks so that It can be viewd as in one frame
    mask1 = mask1 +mask2
    
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    mask2 =cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background,background,mask=mask1)
    #The basic work of bitwise_and is to combine these background and store it in res1

        
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Cloak',final_output)
    k = cv2.waitKey(10)
    if k==27: 
        break
cap.release()
cv2.destroyAllWindows()