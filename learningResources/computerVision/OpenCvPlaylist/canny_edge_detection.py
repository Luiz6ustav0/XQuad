""" 
This algorithm can be broken down, basically, in 5 steps:
    1. Noise reduction
    2. Gradient calculation
    3. Non-maximum suppression
    4. Double threshold
    5. Edge Tracking by Hysteresis
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt 


img = cv2.imread("jp.png", 0)
canny = cv2.Canny(img, 100, 200, ) # Maybe add a trackbar?

titles = ['image', 'canny']
images = [img, canny]

for i in range(len(titles)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
