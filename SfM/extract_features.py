import cv2
import numpy as np
import scipy.optimize
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy.ndimage import gaussian_filter
from scipy.linalg import rq

img = cv2.imread('./SfM/image4.jpg',0)
cv2.imshow('lol', img)
cv2.waitKey(0)
# Initiate STAR detector
orb = cv2.ORB()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
plt.imshow(img2)
plt.show()