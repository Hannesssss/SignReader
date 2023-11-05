import numpy as np

def get_limits(color):
    # Define a wider range for hue (H) to detect a broader spectrum of yellows
    lowerLimit = np.array([13, 100, 100], dtype=np.uint8)
    upperLimit = np.array([30, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
