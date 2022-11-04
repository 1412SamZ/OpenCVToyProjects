import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(2)

mpDraw = mp.solutions.drawing_utils
faceDetection = mp.solutions.face_detection.FaceDetection()

while True:
    success, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
            h, w, c = img.shape
    
    cv2.imshow("image", img)
    
    cv2.waitKey(1)