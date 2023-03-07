import cv2
import streamlit as st
import time
import numpy as np
import PoseEstimationModule as pm
from audio import play



def BicepCurls_counter():
    st.title("I AM BOT!!!")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture("Resources/MyOwnVid.mp4")
    # cap = cv2.VideoCapture(0)
    detect = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0
    play("wel1.mp3")

    while run:
        success,img = cap.read()
        # img = cv2.imread("Resources/gym_img.jpg")
        img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(500,700))
        img = detect.findPose(img,False)
        lmList = detect.getPose(img,False)
        # print(lmList)
        if(len(lmList)!=0):
            # right
            angle = detect.findAngle(img,16,14,12)
            # print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)

            # min = 30 , max=170
            per = np.interp(angle,(30,170),(100,0))
            bar = np.interp(angle,(30,170),(50,300))
            # print(angle,per)

            # check for curl
            color = (0,0,0)
            if per==100:
                color = (0, 255, 255)
                if dir==0:
                    count+=0.5
                    dir=1
            if per==0:
                color = (0, 255, 255)
                if dir==1:
                    count+=0.5
                    dir=0
            print(count)
            #
            cv2.rectangle(img, (450, 50), (485, 300), color, 3)
            cv2.rectangle(img, (450, int(bar)), (485, 300), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (400, 35), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            #
            # # showing count
            cv2.rectangle(img, (20, 555), (130, 665), (0, 255, 255), cv2.FILLED)
            cv2.putText(img,str(int(count)),(45,645),cv2.FONT_HERSHEY_PLAIN,6,(255,0,0),15)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        cv2.imshow("Trainer",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        FRAME_WINDOW.image(img)
    else:
        st.write('Stopped')

    cap.release()
    cv2.destroyAllWindows()

BicepCurls_counter()



