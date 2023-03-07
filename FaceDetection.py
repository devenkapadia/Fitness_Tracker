import cv2
import mediapipe as mp
import time

mpFace = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
Face = mpFace.FaceDetection()
cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = Face.process(imgRGB)
    # print(res.pose_landmarks)
    if res.detections:
        for id, det in enumerate(res.detections):
            # mpDraw.draw_detection(img, det)
            # print(id,det)
            # print(det.score)
            # print(  .location_data.relative_bounding_box)
            bboxC = det.location_data.relative_bounding_box
            ih,iw,ic = img.shape
            bbox = int(bboxC.xmin * iw),int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)

            cv2.rectangle(img, bbox, (0, 255, 255),2)
            cv2.putText(img, f"{int(det.score[0]*100)}%", (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {(int(fps))}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Faces", img)
    cv2.waitKey(1)