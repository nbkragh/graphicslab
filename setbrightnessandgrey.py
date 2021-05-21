
from typing import final
import numpy as np
import sys
import cv2

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    if value < 0:
        lim = 0 - value
        v[v < lim] = 0
        v[v >= lim] -= -1*value
    else:
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

filename = sys.argv[1]
brightness = int(sys.argv[2])
print(filename)
cv2.imwrite(filename+"brightned.png", cv2.cvtColor(increase_brightness(cv2.imread(filename), brightness ), cv2.COLOR_BGR2GRAY))
