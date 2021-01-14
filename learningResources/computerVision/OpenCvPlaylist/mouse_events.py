import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str((x, y)), (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)

def click_event_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)


img = np.zeros((720, 1280), np.uint8)
# img = cv2.imread('jp.png')
cv2.imshow('image', img)

points = []

cv2.setMouseCallback('image', click_event_circle)

cv2.waitKey(0)
cv2.destroyAllWindows
