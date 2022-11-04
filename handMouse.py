import pyautogui
import numpy as np
from library.utils import handDetector
import cv2

print('Press Ctrl-C to quit.')
cap = cv2.VideoCapture(2)
hand_detector = handDetector()

moveXp, moveYp = 0, 0
speed = 1500
try:
    while True:
        success, img = cap.read()
        try:
            moveX, moveY = hand_detector.findHandPosition(img)
            
        except:
            moveX, moveY = 0, 0 
            continue
            
        move_delta_x, move_delta_y = int(-speed*(moveX - moveXp)), int(speed*(moveY - moveYp))


        num_seconds = 0.1
        
        
        moveXp, moveYp = moveX, moveY
        pyautogui.moveRel(move_delta_x, move_delta_y, duration=num_seconds)
        #print(move_delta_x, move_delta_y)

except KeyboardInterrupt:
    print('\n')


