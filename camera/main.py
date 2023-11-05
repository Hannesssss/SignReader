import cv2
from util import get_limits
import numpy as np

yellow = [0, 255, 255]  # yellow in BGR colorspace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = getlimits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Find contours in the mask
    contours,  = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through detected contours
    for contour in contours:
        # Draw a bounding rectangle around the detected region
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()