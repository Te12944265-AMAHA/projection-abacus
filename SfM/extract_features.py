import cv2
import numpy as np
import scipy.optimize
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy.ndimage import gaussian_filter
from scipy.linalg import rq

img = cv2.imread('./SfM/image2.jpg', 0)
edges = cv2.Canny(img,10,200)
img0 = cv2.medianBlur(img, 5)
print(img0.dtype)
th3 = cv2.adaptiveThreshold(img0, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(131),plt.imshow(edges, 'gray'),plt.title('Input')
plt.subplot(132),plt.imshow(sobelx8u, 'gray'),plt.title('Output')
plt.subplot(133),plt.imshow(sobel_8u, 'gray'),plt.title('Output2')
plt.show()
