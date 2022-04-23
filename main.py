import cv2 as cv
import sys

# This reads an image using opencv
img = cv.imread(cv.samples.findFile("starry_night.jpg"))

if img is None:
    sys.exit("Could not read the image.")

# This shows an image using opencv
cv.imshow("Display window", img)

# we wait until the user presses any key to stop showing the image
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)

