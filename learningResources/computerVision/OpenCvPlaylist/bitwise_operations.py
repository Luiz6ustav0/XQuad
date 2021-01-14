import cv2
import numpy as np 

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255, 255, 255), -1)

img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (0,500), (250,0), (255, 255, 255), -1)

# bitAnd = cv2.bitwise_and(img2, img1)
# bitOr = cv2.bitwise_or(img2, img1)
# bitXOr = cv2.bitwise_xor(img2, img1)
bitNot = cv2.bitwise_not(img2)

cv2.imshow('bitwise operations', bitNot)
cv2.imshow('img', img1)

cv2.waitKey()
