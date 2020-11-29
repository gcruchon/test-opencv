import cv2
import numpy as np
cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)

while True:
    success, img = cap.read()
    cv2.imshow("Cam", cv2.Canny(img, 100, 100))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
