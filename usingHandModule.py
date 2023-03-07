import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detect = htm.handDetector()
while True:
    success, img = cap.read()
    img = detect.findHands(img)
    lmLst = detect.findPos(img)
    if len(lmLst) != 0:
        print(lmLst[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Hand", img)
    cv2.waitKey(1)
