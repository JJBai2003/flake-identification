import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage import color
from skimage import io
import cv2 as cv

a = img.imread("10X_example_images/im_11.bmp")
# plt.imshow(a)
# plt.show()

grey_scale = color.rgb2gray(io.imread("10X_example_images/im_11.bmp"))
# plt.imshow(grey_scale)
# plt.show()

pic = cv.imread(
    "10X_example_images/im_11.bmp",
)
ret, thresh1 = cv.threshold(pic, 127, 255, cv.THRESH_BINARY_INV)
plt.imshow(pic)
plt.show()


# Figure 1: outlining ALL flakes
edged = cv.Canny(cv.cvtColor(pic, cv.COLOR_BGR2GRAY), 30, 200)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(pic, contours, -1, (0, 255, 0), 3)
plt.imshow(pic)
plt.show()

# Figure 2: finding centroids of all flake pieces with dust removed
