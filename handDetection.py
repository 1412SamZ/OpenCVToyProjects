import cv2
import mediapipe as mp
from time import time



class handDetector():
    def __init__(self,
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5, ultra_mode=True):
        
        self.static_image_mode=static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            self.static_image_mode,
            self.max_num_hands,
            min_detection_confidence = self.min_detection_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils
        
        self.ultra_mode = ultra_mode
        
    
    
    def findHands(self, img):
        results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        h, w, c = img.shape
        
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                if self.ultra_mode:
                    for ldmk_id, ldm in enumerate(landmarks.landmark):
                        cx, cy = int(ldm.x * w), int(ldm.y * h)
                        cv2.circle(img, (cx, cy), 15,(255, 0, 0), cv2.FILLED)
                        cv2.putText(img,str(ldmk_id), (cx,cy), cv2.FONT_HERSHEY_COMPLEX, 2, 255)

                self.mpDraw.draw_landmarks(img, landmarks, self.mp_hands.HAND_CONNECTIONS)    



cap = cv2.VideoCapture(0)





    
        
if __name__ == "__main__":
    now_time = time()
    p_time = time()
    
    hand_detector = handDetector()
    
    while True:
        success, img = cap.read()
        hand_detector.findHands(img)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
    
    