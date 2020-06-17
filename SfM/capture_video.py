import cv2
import numpy as np 

cap = cv2.VideoCapture(1) # create a VideoCapture object

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./SfM/output.avi',fourcc, 20.0, (640,480))
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)

        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite('./SfM/image%d.jpg'%(i), frame)
            i += 1
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()