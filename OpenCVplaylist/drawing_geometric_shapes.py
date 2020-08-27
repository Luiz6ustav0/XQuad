# Learning how to draw geometric shapes, put text and show images using numpy

import numpy as np
import cv2 


# reads image file 
img = cv2.imread('jp.png', 1)

# Creates a black img using numpy
img = np.zeros([512, 512, 3], np.uint8)

# Drawing lines
img = cv2.line(img, (0, 0), (255, 255), (255, 255, 0), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

# Drawing some shapes, -1 makes the shape filled with the color
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1)
img = cv2.circle(img, (447, 64), 63, (255, 0, 255), -1)

# Writing on the image using default fonts from cv2
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (10, 300), font, 3, (255, 255, 255), 5, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
