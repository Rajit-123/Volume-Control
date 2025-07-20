import cv2
import time
import requests

wcam , hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
ptime = 0




while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    ctime = time.time()
    fps = 1/(ctime- ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (40,50), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break