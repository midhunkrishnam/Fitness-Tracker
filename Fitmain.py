import cv2
import poseModule as pm
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\ganav\Downloads\dlproject\projecrt\Fitness_Tracker\WhatsApp Video 2023-06-30 at 8.16.49 AM.mp4')
detector = pm.poseDetector()

count = 0
dir = 0

while True:
    sucess,img = cap.read()
    img = cv2.resize(img,(1280,720)) #resize video
    
    img = detector.findPose(img,draw=False)
    
    lmlist = detector.findPosition(img,draw=False)
    
    if len(lmlist) !=0:
        angle1 = detector.findAngle(img,24,26,28)

        low = 40
        high = 170

        per = np.interp(angle1,(low,high),(0,100))
        

        if per ==0:
            if dir ==1:
                count +=0.5
                dir=0

        if per ==100:
            if dir ==0:
                count+=0.5
                dir = 1
    

        img = cv2.putText(img,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
    cv2.imshow("fitness tracking",img)
    if cv2.waitKey(1) & 0XFF == 27:
        break