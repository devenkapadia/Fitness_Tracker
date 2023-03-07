import cv2
import mediapipe as mp
import time
import os
import HandTrackingModule as htm

wCam,hCam = 640,488

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

folderPath = 'FingerCount'
myList = os.listdir(folderPath)
# print(myList)
overlayList = []
for imPath in myList:
    path = f'{folderPath}/{imPath}'
    image = cv2.imread(f'{path}')
    # print(path)
    overlayList.append(image)
print(len(overlayList))


detect = htm.handDetector(detCon=0.7)
tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detect.findHands(img)
    lmList = detect.findPos(img,draw=False)
    # print(lmList)
    left=False
    right=False

    if len(lmList)!=0:
        fingers = []

        # Left hand
        # Thumb
        if lmList[17][1] > lmList[4][1]:
            left=True
            if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        if left:
            # 4 fingers
            for id in range(1, 5):
                print("Left")
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 3][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        # Right hand
        if lmList[4][1] > lmList[17][1]:
            right=True
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        if right:
            # 4 fingers
            for id in range(1, 5):
                print("Right")
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 3][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        # print(fingers)

        totFingers = fingers.count(1)
        # print(totFingers)


        h,w,c = overlayList[0].shape
        # print(h,w,c)
        # img[10:h, 20:w] = overlayList[0]

        cv2.rectangle(img,(20,255),(170,425),(0,255,255),cv2.FILLED)
        cv2.putText(img,str(totFingers),(45,390),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("FINGERT COUNTER",img)
    cv2.waitKey(1)