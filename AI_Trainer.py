import cv2
import numpy as np
import time
import mediapipe as mp
import PoseEstimationModule as pm

cap = cv2.VideoCapture("Resources/gym_vid.mp4")
detect = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success,img = cap.read()
    # img = cv2.imread("Resources/gym_img.jpg")
    # img= cv2.resize(img,(500,700))
    img = detect.findPose(img,False)
    lmList = detect.getPose(img,False)
    # print(lmList)
    if(len(lmList)!=0):
        # right
        # detect.findAngle(img,16,14,12)
        # left

        # min = 30 , max=170
        angle = detect.findAngle(img,15,13,11)
        per = np.interp(angle,(30,170),(100,0))
        bar = np.interp(angle,(30,170),(50,300))
        # per = np.interp(angle,(30,170),(0,100))
        # bar = np.interp(angle,(30,170),(300,50))
        # print(angle,per)

        # check for curl
        color = (255,0,0)
        if per==100:
            color = (0, 255, 0)
            if dir==0:
                count+=0.5
                dir=1
        if per==0:
            color = (0, 0, 255)
            if dir==1:
                count+=0.5
                dir=0
        # print(count)

        cv2.rectangle(img, (480, 50), (515, 300), color, 3)
        cv2.rectangle(img, (480, int(bar)), (515, 300), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (530, 185), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)

        cv2.rectangle(img, (20, 255), (130, 395), (0, 255, 255), cv2.FILLED)
        cv2.putText(img,str(int(count)),(45,340),cv2.FONT_HERSHEY_PLAIN,6,(255,0,0),15)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("Trainer",img)
    cv2.waitKey(1)
