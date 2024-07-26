import cv2
import mediapipe as mp
import numpy as np


media_pose = mp.solutions.pose
media_draw = mp.solutions.drawing_utils
pose = media_pose.Pose()

cap = cv2.VideoCapture('pose02.mp4')
spec1 = media_draw.DrawingSpec(thickness=2,
                               circle_radius=3,
                               color=(0, 0, 255))
spec2 = media_draw.DrawingSpec(thickness=2,
                               circle_radius=3,
                               color=(0, 255, 0))

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    # img = cv2.resize(img, (800, 600))

    h, w, c = img.shape
    blank = np.zeros((h, w, c))
    blank.fill(255)
    result = pose.process(img)

    media_draw.draw_landmarks(blank, result.pose_landmarks,
                              media_pose.POSE_CONNECTIONS,
                              spec1, spec2)


    cv2.imshow('Original', img)
    cv2.imshow('Pose', blank)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()