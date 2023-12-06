import time
import cv2
import mediapipe as mp
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = time.time()

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cv2.destroyAllWindows()