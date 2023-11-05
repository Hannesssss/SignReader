import cv2
import pytesseract
from util import get_limits

yellow = [0, 255, 255]  # Yellow in BGR colorspace

# Load an image from a file
image = cv2.imread('30_sign_012.jpg')

# Convert the image to the HSV colorspace
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Get the lower and upper HSV limits for yellow
lowerLimit, upperLimit = get_limits(color=yellow)

# Create a mask by thresholding the HSV image
mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize an empty list to store recognized speed limits
recognized_speed_limits = []

# Iterate through detected contours
for contour in contours:
    # Draw a bounding rectangle around the detected region
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Crop the bounding rectangle region
    roi = image[y:y + h, x:x + w]

    # Apply OCR to recognize the speed limit text within the ROI
    speed_text = pytesseract.image_to_string(roi, config='--psm 6')

    # Append the recognized speed limit to the list
    recognized_speed_limits.append(speed_text)

# Display the processed image with bounding rectangles
cv2.imshow('Image with Yellow Object Tracking', image)

# Create a new window with the recognized speed limit
if recognized_speed_limits:
    speed_limit_image = image.copy()
    speed_text = recognized_speed_limits[0]  # Assume the first recognized limit
    cv2.putText(speed_limit_image, speed_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Recognized Speed Limit', speed_limit_image)

cv2.waitKey(0)

# Close the image windows
cv2.destroyAllWindows()

# Print recognized speed limits
for speed_limit in recognized_speed_limits:
    print("Recognized Speed Limit:", speed_limit)
