import cv2
import numpy as np
import time
import mediapipe as mp
import PoseEstimationModule as pm
from gtts import gTTS
from playsound import playsound
import streamlit as st
# Suryanamaskar

# var = gTTS(text="Currently Doing: Sarvangasana", lang='en')
# var.save("wel.mp3")
# playsound('wel.mp3')
# var1 = gTTS(text="वर्तमान में वक्रासन कर रहे हैं",lang='hi')
# var1.save("wel1.mp3")
# playsound('wel1.mp3')

def time_c(sec):
    mins=sec//60
    sec=sec%60
    hours=mins//60
    mins=mins%60
    return f"Time:{hours}:{mins}:{sec}"


def p1():
    # cap = cv2.VideoCapture("Resources/1.jpg")
    # cap = cv2.VideoCapture(0)
    # cap = cv2.imread("Resources/1.jpg")
    detect = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0

    while True:
        # success,img = cap.read()
        img = cv2.imread("Resources/Sarvangasana.png")
        # img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(600,700))
        img = detect.findPose(img,False)
        lmList = detect.getPose(img,False)
        # print(lmList)
        if(len(lmList)!=0):
            # right
            a1=detect.findAngle(img,0,24,28)
            if a1>145 or a1<135:
                print("Wrong Pose")
            # a2 = detect.findAngle(img,16,14,12)
            # if a2>305 and a2<295:
            #     print("Wrong pose")
            # print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

        cv2.imshow("Trainer",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    return img

def p2():
    st.write("Vakrasana")
    cap = cv2.VideoCapture("Resources/treePose.mp4")
    # cap = cv2.VideoCapture(0)
    detect = pm.poseDetector()
    FRAME_WINDOW = st.image([])
    count = 0
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        # img = cv2.imread("Resources/treePose.jpg")
        # img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(600,700))
        img = detect.findPose(img,False)
        lmList = detect.getPose(img,False)
        # print(lmList)
        if(len(lmList)!=0):
            # right
            now,now2=0,0
            timeTaken=""
            a1=detect.findAngle(img,27,25,23,draw=False)
            a2=detect.findAngle(img,13,20,14,draw=False)
            # print(a1)
            # a2=104 a1=51
            if a1<43 and a1>20 and a2<115 and a2>96:
                now = time.time()
            if a1>43 or a1<20:
                x1, y1 = lmList[27][1:]
                x2, y2 = lmList[25][1:]
                x3, y3 = lmList[23][1:]
                print("Wrong pose")
                cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x1, y1), 15, (0, 0, 255))
                cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (0, 0, 255))
                cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x3, y3), 15, (0, 0, 255))
                # playsound('bonk.mp3')
                now2 = time.time()
            else:
                print("Correct Legs")
                x1, y1 = lmList[27][1:]
                x2, y2 = lmList[25][1:]
                x3, y3 = lmList[23][1:]
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)

            if a2 > 115 or a2 < 96:
                x1, y1 = lmList[13][1:]
                x2, y2 = lmList[20][1:]
                x3, y3 = lmList[14][1:]
                # print("Wrong pose")
                cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x1, y1), 15, (0, 0, 255))
                cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (0, 0, 255))
                cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x3, y3), 15, (0, 0, 255))
                print("Wrong Pose")
                now2 = time.time()
                # playsound('bonk.mp3')
            else:
                print("Correct hands")
                x1, y1 = lmList[13][1:]
                x2, y2 = lmList[20][1:]
                x3, y3 = lmList[14][1:]
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)

            # print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)
            ele_time=now2-now
            timeTaken = time_c(ele_time)
            print(timeTaken)
            # cv2.putText(img, str(int(fps)), (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

        FRAME_WINDOW.image(img)
    else:
        st.write('Stopped')

    return img

if __name__ == '__main__':
    p2()
# p1()