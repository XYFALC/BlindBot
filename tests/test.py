import math
import numpy as np

def calculatedegrees(x1, y1, x2, y2):
    degrees = np.arctan2(x2 - x1, y2 - y1) * 180 / np.pi
    if degrees < 0: degrees += 360
    return round(degrees)


x1 = 7252
y1 = 3070
x2 = 7260
y2 = 3086

print(calculatedegrees(x1, y1, x2, y2))
