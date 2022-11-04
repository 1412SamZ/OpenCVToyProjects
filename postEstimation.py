import cv2
import mediapipe as mp
from time import time 
import numpy as np

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(2)

def drawBodyPart(ldmk, w, h):
    cx, cy = int(ldmk.x * w), int(ldmk.y * h)
    cv2.rectangle(img_overlay, (cx-40, cy+40),(cx+40, cy-40), (0,20,0), -1)
    #cv2.rectangle(img_overlay, (cx-40, cy+42),(cx+40, cy-42), (0,233,0), 2)
    #cv2.rectangle(img, (cx-40, cy+42),(cx+40, cy-42), (0,233,0), 2)
    
    cv2.rectangle(img_overlay, (cx-20, cy-20),(cx+20, cy+0), (0,255,0),1 )
    cv2.rectangle(img, (cx-20, cy-20),(cx+20, cy+0), (0,255,0),1 )
    
    cv2.rectangle(img_overlay, (cx-20, cy-20),(cx+15, cy+0), (0,255,0),-1 )
    cv2.rectangle(img, (cx-20, cy-20),(cx+15, cy+0), (0,255,0),-1 )
    
    cv2.putText(img_overlay, "95", (cx-12, cy+22), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 1)
    cv2.putText(img, "95", (cx-12, cy+22), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 1)

    cv2.line(img_overlay, (cx-40, cy+40), (cx-40, cy-40), (0, 255, 0), 1) 
    cv2.line(img, (cx-40, cy+40), (cx-40, cy-40), (0, 255, 0), 1) 
    
    cv2.line(img_overlay, (cx+40, cy+40), (cx+40, cy-40), (0, 255, 0), 1) 
    cv2.line(img, (cx+40, cy+40), (cx+40, cy-40), (0, 255, 0), 1) 
    
    cv2.line(img_overlay, (cx+25, cy-40), (cx+40, cy-40), (0, 255, 0), 1) 
    cv2.line(img, (cx+25, cy-40), (cx+40, cy-40), (0, 255, 0), 1) 
    
    cv2.line(img_overlay, (cx-40, cy-40), (cx-25, cy-40), (0, 255, 0), 1) 
    cv2.line(img, (cx-40, cy-40), (cx-25, cy-40), (0, 255, 0), 1) 
    
    cv2.line(img_overlay, (cx+25, cy+40), (cx+40, cy+40), (0, 255, 0), 1) 
    cv2.line(img, (cx+25, cy+40), (cx+40, cy+40), (0, 255, 0), 1) 
    
    cv2.line(img_overlay, (cx-40, cy+40), (cx-25, cy+40), (0, 255, 0), 1) 
    cv2.line(img, (cx-40, cy+40), (cx-25, cy+40), (0, 255, 0), 1) 
    
    
def checkBodyPart(ldmk_id):
    return ldmk_id in [0, 11, 12, 25, 26]

def drawHealth(ldmk, w, h):
    cx, cy = int(ldmk.x * w), int(ldmk.y * h)
    cv2.rectangle(img_overlay, (cx-140, cy-150),(cx+140, cy-170), (0,255,0),2 )
    cv2.rectangle(img_overlay, (cx-140, cy-150),(cx+120, cy-170), (0,255,0),-1 )
    cv2.putText(img_overlay, "Human", (cx-130, cy-190), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.rectangle(img, (cx-140, cy-150),(cx+140, cy-170), (0,255,0),2 )
    cv2.rectangle(img, (cx-140, cy-150),(cx+120, cy-170), (0,255,0),-1 )
    cv2.putText(img, "Human", (cx-130, cy-190), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
def checkHead(ldmk_id):
    return ldmk_id == 0


p_time = 0
while True:
    
    success, img = cap.read()
    h, w, c = img.shape
    img_health = np.zeros([h, w, 3], dtype=np.uint8)
    img_overlay = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    if results.pose_landmarks:
        for ldmk_id, ldmk in enumerate(results.pose_landmarks.landmark):
            if checkBodyPart(ldmk_id):
                drawBodyPart(ldmk, w, h)
            if checkHead(ldmk_id):
                drawHealth(ldmk, w, h)
            
        #mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS) 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    n_time = time()
    fps = round(1/(n_time - p_time))
    p_time = n_time
    
    cv2.putText(img, str(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    alpha=0.4
    image_new = cv2.addWeighted(img_overlay, alpha, img, 1 - alpha, 0)
    cv2.imshow("image", image_new)
    cv2.waitKey(1)

