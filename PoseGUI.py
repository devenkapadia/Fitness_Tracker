import cv2
import mediapipe as mp
import time
import math
from tkinter import *

class poseDetector():
    def __init__(self,mode=False,complex=1,smooth=True,enSeg=False,smSeg=True,detCon = 0.5,trackCon=0.5):
        self.mode = mode
        self.complex = complex
        self.smooth = smooth
        self.enSeg = enSeg
        self.smSeg = smSeg
        self.detCon = detCon
        self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(self.mode,self.complex,self.smooth,self.enSeg,self.smSeg,self.detCon,self.trackCon)

    def findPose(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res = self.pose.process(imgRGB)
        if self.res.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.res.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPose(self,img,draw=True):
        self.lmList = []
        if self.res.pose_landmarks:
            for id, lm in enumerate(self.res.pose_landmarks.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 255, 0), cv2.FILLED)
                # if id == 16:
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self,img,p1,p2,p3,draw=True):
        x1,y1 = self.lmList[p1][1:]
        x2,y2 = self.lmList[p2][1:]
        x3,y3 = self.lmList[p3][1:]

        angle = math.degrees(math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2,x1-x2))
        if angle<0:
            angle+=360

        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img,(x3,y3),(x2,y2),(255,255,255),3)

            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0))
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0))
            cv2.circle(img, (x3, y3), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0))

            cv2.putText(img,str(int(angle)),(x2-20,y2+50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)

        return angle

def gui():
    root = Tk()
    root.title("GUI Trainer")
    btn = Button(root,text="Track",command=lambda: main(root))
    btn.pack()
    root.mainloop()


def main(t):
    t.destroy()
    cap = cv2.VideoCapture("Resources/gym_vid.mp4")
    pTime = 0
    detect = poseDetector()

    while True:
        success, img = cap.read()
        img = detect.findPose(img)
        lmlst = detect.getPose(img)
        if len(lmlst)!=0:
            print(lmlst[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Video", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    # main()
    gui()