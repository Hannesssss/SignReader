import cv2
from util import get_limits

yellow = [0, 255, 255]  # Yellow in BGR colorspace

# Load an image from a file
image = cv2.imread('30_sign_010.jpg')

# Convert the image to the HSV colorspace
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Get the lower and upper HSV limits for yellow
lowerLimit, upperLimit = get_limits(color=yellow)

# Create a mask by thresholding the HSV image
mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through detected contours
for contour in contours:
    # Draw a bounding rectangle around the detected region
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the processed image with bounding rectangles
cv2.imshow('Image with Yellow Object Tracking', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
