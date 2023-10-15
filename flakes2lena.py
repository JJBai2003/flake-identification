import matplotlib.pyplot as plt
import matplotlib.image as img 
from skimage import color
from skimage import io
import cv2 as cv

a = img.imread("im_11.bmp") 
# plt.imshow(a)
# plt.show()

grey_scale = color.rgb2gray(io.imread("im_11.bmp"))
# plt.imshow(grey_scale)
# plt.show()

pic = cv.imread("im_11.bmp",)
ret, thresh1 = cv.threshold(pic, 127, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
plt.imshow(pic)
plt.show()


# Figure 1: outlining flakes
