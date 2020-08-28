import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str((x, y)), (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)


# img = np.zeros((720, 1280), np.uint8)
img = cv2.imread('jp.png')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows
