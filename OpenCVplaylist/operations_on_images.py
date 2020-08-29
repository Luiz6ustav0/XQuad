import numpy as np
import cv2


img = cv2.imread("jp.png")

print("{}\n{}\n{}".format(img.shape, img.size, img.dtype))

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# something = img[180:240, 230:290]
# img[262:322, 100:160] = something


# in order to add images they need to have the same side
dst = cv2.resize(img, (512, 512))


cv2.imshow('test', img)

cv2.waitKey()