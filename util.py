import numpy as np
import cv2
def get_limits(color):
    c=np.uint8([[color]])
    hsv=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    hue=hsv[0][0][0]
    if hue>=165:
        lower_limit=np.array([hue-10,100,100],dtype=np.uint8)
        upper_limit=np.array([180,255,255],dtype=np.uint8)
    elif hue<=15:
        lower_limit=np.array([0,100,100],dtype=np.uint8)
        upper_limit=np.array([hue+10,255,255],dtype=np.uint8)
    else:
        lower_limit=np.array([hue-10,100,100],dtype=np.uint8)
        upper_limit=np.array([hue+10,255,255],dtype=np.uint8)
    
    return lower_limit,upper_limit


