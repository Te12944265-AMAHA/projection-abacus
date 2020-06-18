import cv2
import numpy as np 
from features import *
import util

## Extract features from images and match
I1 = cv2.imread()
I2 = cv2.imread()
matches, loc1, locs2 = matchPics(I1, I2)

# process them
pts1 = None
pts2 = None

## Calculate F using 8-point alg
pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)
# We select only inlier points
pts1 = pts1[mask.ravel()==1]
pts2 = pts2[mask.ravel()==1]

# Calculate P and P' from F


# Triangulate using x, x' P, P'
