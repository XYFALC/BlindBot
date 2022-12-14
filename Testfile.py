import math
import numpy as np

def calculatedegrees(x1, y1, x2, y2):
    degrees = np.arctan2(y2 - y1, x2 - x1) * 180/np.pi
    degrees = degrees - 90
    return round(abs(degrees))

x1 = 7252
y1 = 3070
x2 = 7260
y2 = 3086

print(calculatedegrees(x1, y1, x2, y2))
