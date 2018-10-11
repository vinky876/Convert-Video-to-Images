import cv2
import numpy as np
cap=cv2.VideoCapture(r"C:\Users\vineet kumar\Desktop\rohit image\l6.mp4")
ret=True
i=0
j=712
while ret:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.imshow('s',frame)
    if(i%50==0):

        cv2.imwrite(r"C:\Users\vineet kumar\Desktop\dataset\left\left"+str(j)+".jpg",frame)
        j=j+1
    i=i+1
    if(cv2.waitKey(1)&0XFF==ord('q')):
        break
cv2.destroyAllWindows()
