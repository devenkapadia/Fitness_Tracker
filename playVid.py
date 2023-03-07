import cv2
import streamlit as st
import mediapipe as mp
import time
import numpy as np
import PoseEstimationModule as pm

count = 0

def BicepCurls_counter():
    st.write("Hammer Curls Counter")

    FRAME_WINDOW = st.image([])
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("Resources/myOwnVid.mp4")
    detect = pm.poseDetector()
    dir = 0
    pTime = 0
    global count
    count = 0

    while True:
        success,img = cap.read()
        # img = cv2.imread(0)
        img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(500,600))
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
                color = (0, 0, 255)
                if dir==0:
                    count+=0.5
                    dir=1
            if per==0:
                color = (0, 0, 255)
                if dir==1:
                    count+=0.5
                    dir=0
            print(count)
            #
            cv2.rectangle(img, (50, 50), (75, 300), color, 3)
            cv2.rectangle(img, (50, int(bar)), (75, 300), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (50, 35), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            #
            # # showing count
            cv2.rectangle(img, (20, 365), (130, 475), (0, 255, 255), cv2.FILLED)
            cv2.putText(img,str(int(count)),(45,445),cv2.FONT_HERSHEY_PLAIN,6,(255,0,0),15)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        # cv2.imshow("Trainer",img)
        FRAME_WINDOW.image(img)
    else:
        st.write('Stopped')

    return img


def SitUps_counter():
    st.write("Sit Ups Counter")

    FRAME_WINDOW = st.image([])
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("Resources/situps.mp4")
    detect = pm.poseDetector()
    dir = 0
    pTime = 0
    global count
    count = 0

    while True:
        success,img = cap.read()
        # img = cv2.imread(0)
        # img = cv2.rotate(img, cv2.ROTATE_180)
        # img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(500,700))
        img = detect.findPose(img,False)
        lmList = detect.getPose(img,False)
        # print(lmList)
        if (len(lmList) != 0):
            # right
            angle = detect.findAngle(img, 25, 24, 12)
            print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)

            # min = 255 , max=295
            per = np.interp(angle, (255, 295), (0, 100))
            bar = np.interp(angle, (255, 295), (50, 300))
            # # print(angle,per)
            #
            # # check for curl
            color = (255, 255, 255)
            if per == 100:
                color = (0, 255, 255)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 255)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)
            # #
            cv2.rectangle(img, (450, 50), (485, 300), color, 3)
            cv2.rectangle(img, (450, int(bar)), (485, 300), color, cv2.FILLED)
            cv2.putText(img, f'{100 - int(per)}%', (400, 35), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            #
            # # # showing count
            cv2.rectangle(img, (20, 555), (130, 665), (0, 255, 255), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 645), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 0), 15)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        # cv2.imshow("Trainer",img)
        FRAME_WINDOW.image(img)
    else:
        st.write('Stopped')

    return img


def PushUps_counter():
    st.write("Push Ups Counter")

    FRAME_WINDOW = st.image([])
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("Resources/pushUps.mp4")
    detect = pm.poseDetector()
    dir = 0
    pTime = 0
    global count
    count = 0

    while True:
        success, img = cap.read()
        # img = cv2.imread("Resources/gym_img.jpg")
        # img = cv2.rotate(img, cv2.ROTATE_180)
        img = cv2.resize(img, (1000, 700))
        img = detect.findPose(img, False)
        lmList = detect.getPose(img, False)
        # print(lmList)
        if (len(lmList) != 0):
            # right
            angle = detect.findAngle(img, 15, 13, 11)
            print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)

            # min = 65 , max=165
            per = np.interp(angle, (65, 165), (0, 100))
            bar = np.interp(angle, (65, 165), (50, 300))
            # # print(angle,per)
            #
            # # check for curl
            color = (255, 255, 255)
            if per == 100:
                color = (0, 255, 255)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 255)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)
            # #
            cv2.rectangle(img, (850, 50), (885, 300), color, 3)
            cv2.rectangle(img, (850, int(bar)), (885, 300), color, cv2.FILLED)
            cv2.putText(img, f'{100 - int(per)}%', (800, 35), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            #
            # # # showing count
            cv2.rectangle(img, (20, 555), (130, 665), (0, 255, 255), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 645), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 0), 15)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        # cv2.imshow("Trainer",img)
        FRAME_WINDOW.image(img)
    else:
        st.write('Stopped')

    return img

def retData():
    global count
    cal = 0.1875*count
    return count, cal

if __name__ == '__main__':
    BicepCurls_counter()
