import cv2
from PIL import Image
from util import get_limits
color=[0,255,255]
cam=cv2.VideoCapture(0)
ret=True
while ret:
    ret,frame=cam.read()
    if not ret:
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_limit,upper_limit=get_limits(color)
    mask=cv2.inRange(hsv,lower_limit,upper_limit)
    mask_=Image.fromarray(mask)
    box=mask_.getbbox()
    if box is not None:
        x1,y1,x2,y2=box
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()