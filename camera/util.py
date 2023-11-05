import numpy as np
import cv2

def get_limits(color):
    # Define a narrower range for hue (H) to target yellow more specifically
    lowerLimit = np.array([20, 100, 100], dtype=np.uint8)
    upperLimit = np.array([30, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit