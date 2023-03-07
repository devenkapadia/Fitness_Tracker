import cv2
import mediapipe as mp
import time

class FaceMeshDetector():
     def __init__(self,staticMode=False,maxFace=2,refLms=False,detCon=0.5,trackCon=0.5):
         self.staticMode = staticMode
         self.maxFace = maxFace
         self.refLms = refLms
         self.detCon = detCon
         self.trackCon = trackCon

         self.mpDraw = mp.solutions.drawing_utils
         self.mpFaceMesh = mp.solutions.face_mesh
         self.Face = self.mpFaceMesh.FaceMesh(self.staticMode,self.maxFace,self.refLms,self.detCon,self.trackCon)
         self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

     def findFaceMesh(self,img,draw=True):
         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
         self.res = self.Face.process(imgRGB)
         # print(self.res.pose_landmarks)
         faces = []
         if self.res.multi_face_landmarks:
             for faceLms in self.res.multi_face_landmarks:
                 if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_FACE_OVAL, self.drawSpec, self.drawSpec)
                 face = []
                 for id,lm in enumerate(faceLms.landmark):
                     # print(lm)
                     ih, iw, ic = img.shape
                     x,y = int(lm.x*iw),int(lm.y*ih)
                     face.append([x,y])
                 faces.append(face)
         return img,faces
         # return img

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detect = FaceMeshDetector()
    while True:
        success, img = cap.read()
        img,faces = detect.findFaceMesh(img)
        if len(faces)!=0:
            print(len(faces))
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS: {(int(fps))}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Faces", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()