import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage import color
from skimage import io
import cv2 as cv

a = img.imread("10X_example_images/im_15.bmp")
# plt.imshow(a)
# plt.show()

grey_scale = color.rgb2gray(io.imread("10X_example_images/im_15.bmp"))
# plt.imshow(grey_scale)
# plt.show()

pic = cv.imread(
    "10X_example_images/im_15.bmp",
)
ret, thresh1 = cv.threshold(pic, 127, 255, cv.THRESH_BINARY)

plt.subplot(2, 2, 1)
plt.imshow(pic)
# plt.show()


# Figure 1: outlining ALL flakes
edged = cv.Canny(cv.cvtColor(pic, cv.COLOR_BGR2GRAY), 3, 200)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(pic, contours, -1, (0, 255, 0), 3)
plt.subplot(2, 2, 2)
plt.imshow(pic)
# plt.show()

# Figure 2: finding centroids of all flake pieces with dust removed

# pic = cv.imread(
#     "10X_example_images/im_15.bmp",
# )
# edged = cv.Canny(cv.cvtColor(pic, cv.COLOR_BGR2GRAY), 30, 200)
# contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# areas = {}
# filtered_contours = []
# for i in range(len(contours)):
#     if cv.contourArea(contours[i]) > 1500:
#         areas[i] = cv.contourArea(contours[i])
#         filtered_contours.append(contours[i])
# print(areas)
# cv.drawContours(pic, filtered_contours, -1, (0, 255, 0), 3)
# plt.subplot(2, 2, 3)
# plt.imshow(pic)
# plt.show()


pic = cv.imread("10X_example_images/im_15.bmp")
thresh = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(thresh, 127, 255, cv.THRESH_BINARY)

# Remove smaller areas less than 300
BW2 = cv.morphologyEx(
    thresh, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE, (30, 50))
)

# Find the centroids
contours, hierarchy = cv.findContours(BW2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
centroids = []
for contour in contours:
    M = cv.moments(contour)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    centroids.append((cx, cy))

plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(pic, cv.COLOR_BGR2RGB))
for centroid in centroids:
    plt.plot(centroid[0], centroid[1], "m*")

# Figure 4: Colored outlines of good and bad flakes based on areas

pic2 = cv.imread("10X_example_images/im_15.bmp", cv.IMREAD_GRAYSCALE)
# thresh = cv.Canny(cv.cvtColor(pic2, cv.COLOR_BGR2GRAY), 70, 300)

# contours_small, hierarchy = cv.findContours(
#     thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE
# )
thresh = cv.Canny(pic2, 3, 200)

# thresh = cv.Canny(cv.cvtColor(pic2, cv.COLOR_BGR2GRAY), 100, 200)
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

contours_large = [contour for contour in contours if cv.contourArea(contour) >= 700]

# cv.drawContours(pic2, contours_small, -1, (255, 0, 0), 2)
cv.drawContours(pic2, contours_large, -1, (0, 0, 255), 2)  # Red for large flakes
# cv.drawContours(pic2, contours, -1, (0, 0, 255), 2)
plt.subplot(2, 2, 4)
plt.imshow(cv.cvtColor(pic2, cv.COLOR_BGR2RGB))
# plt.imshow(pic2)


plt.tight_layout()
plt.savefig("endflakes.png")
plt.show()
