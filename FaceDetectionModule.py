import cv2
import mediapipe as mp
import time

class faceDetector():
    def __init__(self,detCon=0.5):
        self.detCon = detCon

        self.mpFace = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.Face = self.mpFace.FaceDetection(detCon)

    def findFaces(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res = self.Face.process(imgRGB)
        bboxes = []
        if self.res.detections:
            for id, det in enumerate(self.res.detections):
                bboxC = det.location_data.relative_bounding_box
                ih,iw,ic = img.shape
                bbox = int(bboxC.xmin * iw),int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)

                bboxes.append([id,bbox,det.score,])
                if draw:
                    img = self.fancyDraw(img,bbox)
                    cv2.putText(img, f"{int(det.score[0]*100)}%", (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
        return img,bboxes

    def fancyDraw(self,img,bbox,l=30,t=5,rt=1):
        print("in fancy draw")
        x,y,w,h = bbox
        x1,y1 = x+w,y+h

        cv2.rectangle(img, bbox, (0, 0, 255), rt)

        # Top left x,y
        cv2.line(img,(x,y),(x+l ,y),(0,0,255),t)
        cv2.line(img,(x,y),(x ,y+l),(0,0,255),t)

        # Top left x1,y
        cv2.line(img,(x1,y),(x1-l ,y),(0,0,255),t)
        cv2.line(img,(x1,y),(x1 ,y+l),(0,0,255),t)

        # Top left
        cv2.line(img,(x,y1),(x+l ,y1),(0,0,255),t)
        cv2.line(img,(x,y1),(x ,y1-l),(0,0,255),t)

        # Top left
        cv2.line(img,(x1,y1),(x1-l ,y1),(0,0,255),t)
        cv2.line(img,(x1,y1),(x1 ,y1-l),(0,0,255),t)

        return img

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detect = faceDetector()

    while True:
        success, img = cap.read()
        img,bboxes = detect.findFaces(img)
        print(bboxes)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f"FPS: {(int(fps))}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f"FPS: {cTime-time.time()}", (90, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Faces", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()