import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
Face = mpFaceMesh.FaceMesh(max_num_faces=2)
cap = cv2.VideoCapture(0)
pTime = 0
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=1)

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = Face.process(imgRGB)
    # print(res.pose_landmarks)
    if res.multi_face_landmarks:
        for faceLms in res.multi_face_landmarks:
            mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_FACE_OVAL,drawSpec,drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                print(id,lm)
                ih,iw,ic=img.shape
                x,y = int(lm.x*iw),int(lm.y*ih)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {(int(fps))}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Faces", img)
    cv2.waitKey(1)