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

## Calculate P and P' from F


## Triangulate using x, x' P, P'



## Scatter plot the correct 3D points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = pt[:,0]
y = pt[:,1]
z = pt[:,2]
ax.scatter(x, y, z, c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


## Save the computed extrinsic parameters (R1,R2,t1,t2) to data/extrinsics.npz
outfile = './SfM/data/extrinsics.npz'
R1 = I[:,0:3]
t1 = np.array([I[:,3]]).T
M2 = np.dot(np.linalg.inv(K2), P2)
R2 = M2[:,0:3]
t2 = np.array([M2[:,3]]).T
np.savez(outfile, R1=R1, R2=R2, t1=t1, t2=t2)



## Re-projection Error
