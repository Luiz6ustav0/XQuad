import cv2
import numpy as np 


def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread("jp.png")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("LH", "Tracking")
    lower_s = cv2.getTrackbarPos("LS", "Tracking")
    lower_v = cv2.getTrackbarPos("LV", "Tracking")

    upper_h = cv2.getTrackbarPos("UH", "Tracking")
    upper_s = cv2.getTrackbarPos("US", "Tracking")
    upper_v = cv2.getTrackbarPos("UV", "Tracking")

    lower_b = np.array([lower_h, lower_s, lower_v])
    upper_b = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_b, upper_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("frame", mask)
    cv2.imshow("frame", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
