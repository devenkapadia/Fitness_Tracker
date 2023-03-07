import cv2
import numpy as np
import time
import mediapipe as mp
import PoseEstimationModule as pm

# Exercises
# hammer curls
# situps
# pushups

def hammerCurls_counter():
    # cap = cv2.VideoCapture("Resources/MyOwnVid.mp4")
    cap = cv2.VideoCapture(0)
    detect = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        # img = cv2.imread("Resources/gym_img.jpg")
        # img = cv2.rotate(img, cv2.ROTATE_180)
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

    cap.release()
    cv2.destroyAllWindows()

def sitUps_counter():
    cap = cv2.VideoCapture("Resources/situps.mp4")
    # cap = cv2.VideoCapture(0)
    detect = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        # img = cv2.imread("Resources/gym_img.jpg")
        # img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(500,700))
        img = detect.findPose(img,False)
        lmList = detect.getPose(img,False)
        # print(lmList)
        if(len(lmList)!=0):
            # right
            angle = detect.findAngle(img,25,24,12)
            print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)

            # min = 255 , max=295
            per = np.interp(angle,(255,295),(0,100))
            bar = np.interp(angle,(255,295),(50,300))
            # # print(angle,per)
            #
            # # check for curl
            color = (255,255,255)
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
            # #
            cv2.rectangle(img, (450, 50), (485, 300), color, 3)
            cv2.rectangle(img, (450, int(bar)), (485, 300), color, cv2.FILLED)
            cv2.putText(img, f'{100-int(per)}%', (400, 35), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            #
            # # # showing count
            cv2.rectangle(img, (20, 555), (130, 665), (0, 255, 255), cv2.FILLED)
            cv2.putText(img,str(int(count)),(45,645),cv2.FONT_HERSHEY_PLAIN,6,(255,0,0),15)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        cv2.imshow("Trainer",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def pushUps_counter():
    cap = cv2.VideoCapture("Resources/pushUps.mp4")
    # cap = cv2.VideoCapture(0)
    detect = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        # img = cv2.imread("Resources/gym_img.jpg")
        # img = cv2.rotate(img, cv2.ROTATE_180)
        img= cv2.resize(img,(1000,700))
        img = detect.findPose(img,False)
        lmList = detect.getPose(img,False)
        # print(lmList)
        if(len(lmList)!=0):
            # right
            angle = detect.findAngle(img,15,13,11)
            print(angle)
            # left
            # angle = detect.findAngle(img,15,13,11)

            # min = 65 , max=165
            per = np.interp(angle,(65,165),(0,100))
            bar = np.interp(angle,(65,165),(50,300))
            # # print(angle,per)
            #
            # # check for curl
            color = (255,255,255)
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
            # #
            cv2.rectangle(img, (850, 50), (885, 300), color, 3)
            cv2.rectangle(img, (850, int(bar)), (885, 300), color, cv2.FILLED)
            cv2.putText(img, f'{100-int(per)}%', (800, 35), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            #
            # # # showing count
            cv2.rectangle(img, (20, 555), (130, 665), (0, 255, 255), cv2.FILLED)
            cv2.putText(img,str(int(count)),(45,645),cv2.FONT_HERSHEY_PLAIN,6,(255,0,0),15)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        cv2.imshow("Trainer",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


sitUps_counter()
# hammerCurls_counter()
# pushUps_counter()
