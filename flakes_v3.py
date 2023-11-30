### NEW CODE, Nov.10, 2023
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, color

# Load the image
originalflakes = cv2.imread('10X_example_images/im_15.bmp')

# Convert to grayscale
originalflakesgray = cv2.cvtColor(originalflakes, cv2.COLOR_BGR2GRAY)

# Binarize the image
_, BW = cv2.threshold(originalflakesgray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find boundaries of all flakes
contours, _ = cv2.findContours(BW, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Plot original image with contours
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(originalflakes, cv2.COLOR_BGR2RGB))
# plt.title('Outlining all flakes')
for contour in contours:
    plt.plot(contour[:, 0, 0], contour[:, 0, 1], 'c', linewidth=2)

# Filter flakes by area and find centroids
areas = [cv2.contourArea(cnt) for cnt in contours]
BW2 = BW.copy()
for i, area in enumerate(areas):
    if area < 300:  # can be adjusted
        cv2.drawContours(BW2, [contours[i]], -1, (0, 0, 0), -1)
contours_filtered, _ = cv2.findContours(BW2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
centroids = [cv2.moments(cnt) for cnt in contours_filtered]
centroids = [(int(M['m10']/M['m00']), int(M['m01']/M['m00'])) for M in centroids if M['m00'] != 0]

# Plot centroids
plt.subplot(2, 2, 2)
plt.imshow(BW2, cmap='gray')
# plt.title('Centroids of all flake pieces')
plt.scatter(*zip(*centroids), color='m', marker='*')

# Plot colored outlines based on area thresholds
BW3 = np.zeros_like(BW)
BW4 = np.zeros_like(BW)
for i, area in enumerate(areas):
    if area < 2000:  # can be adjusted
        cv2.drawContours(BW3, [contours[i]], -1, (255, 255, 255), -1)
    elif area <= 500000:  # can be adjusted
        cv2.drawContours(BW4, [contours[i]], -1, (255, 255, 255), -1)

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(originalflakes, cv2.COLOR_BGR2RGB))
# plt.title('Good and bad flakes based on areas')
for contour in cv2.findContours(BW3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
    plt.plot(contour[:, 0, 0], contour[:, 0, 1], 'r', linewidth=2)
for contour in cv2.findContours(BW4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
    plt.plot(contour[:, 0, 0], contour[:, 0, 1], 'g', linewidth=2)

# Save the figure
plt.savefig('endflakes.png')
plt.show()