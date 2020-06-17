import cv2
import numpy as np
import scipy.optimize
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy.ndimage import gaussian_filter
from scipy.linalg import rq

img = cv2.imread('./SfM/image0.jpg')
print(img.dtype)
b, g, r = cv2.split(img)

img_inverted = cv2.merge((b, g, r))
cv2.imshow('img', img_inverted)
cv2.waitKey(0)