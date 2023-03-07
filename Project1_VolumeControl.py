import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

###################
wCam,hCam = 720,500
###################


cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
print(volRange)
minVol = volRange[0]
maxVol = volRange[1]
vol=0
volBar=400
volPer=0

detect = htm.handDetector(detCon=0.7)

while True:
    success,img=cap.read()
    img = detect.findHands(img)
    lmList = detect.findPos(img)
    if len(lmList)!=0:

        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx,cy = (x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),10,(255,255,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,255,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,255,0),2)
        cv2.circle(img,(cx,cy),10,(255,255,0),cv2.FILLED)

        lenght = math.hypot(x2-x1,y2-y1)
        # print(lenght)

        # Hand range = 15-190
        # Vol range = -63-0
        vol = np.interp(lenght,[15,190],[minVol,maxVol])
        volBar = np.interp(lenght,[15,190],[400,150])
        volPer = np.interp(lenght,[15,190],[0,100])
        # print(vol)
        # volu   me.SetMasterVolumeLevel(vol, None)
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (40, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Volume Controller",img)
    cv2.waitKey(1)