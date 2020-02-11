
import cv2
import time


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    ret,img = cap.read()
    cv2.imshow('img',img)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
