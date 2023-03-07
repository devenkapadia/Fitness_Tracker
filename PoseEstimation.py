import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()
cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = pose.process(imgRGB)
    # print(res.pose_landmarks)
    if res.pose_landmarks:
        mpDraw.draw_landmarks(img, res.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(res.pose_landmarks.landmark):
            # print(id,lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 7, (255, 255, 0), cv2.FILLED)
            if id == 16:
                cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Pose", img)
    cv2.waitKey(1)