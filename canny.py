import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = './images/cameraman.png'
image = cv2.imread(image_path, 0)

# Apply Gaussian smoothing
blurred = cv2.GaussianBlur(image, (5, 5), 1)

# Compute gradients using Sobel operator
gradient_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

# Compute gradient magnitude and direction
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_direction = np.arctan2(gradient_y, gradient_x)

# Non-maximum suppression
gradient_direction = np.rad2deg(gradient_direction) % 180
edge_map = np.zeros_like(image)
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        direction = gradient_direction[i, j]
        mag = gradient_magnitude[i, j]
        if (0 <= direction < 22.5) or (157.5 <= direction <= 180):
            before = gradient_magnitude[i, j - 1]
            after = gradient_magnitude[i, j + 1]
        elif (22.5 <= direction < 67.5):
            before = gradient_magnitude[i - 1, j + 1]
            after = gradient_magnitude[i + 1, j - 1]
        elif (67.5 <= direction < 112.5):
            before = gradient_magnitude[i - 1, j]
            after = gradient_magnitude[i + 1, j]
        else:
            before = gradient_magnitude[i - 1, j - 1]
            after = gradient_magnitude[i + 1, j + 1]
        if mag >= before and mag >= after:
            edge_map[i, j] = mag

# Hysteresis thresholding
low_threshold = 30
high_threshold = 100
strong_edges = (edge_map > high_threshold)
weak_edges = (edge_map >= low_threshold) & (edge_map <= high_threshold)
edge_map_final = np.zeros_like(image)
edge_map_final[strong_edges] = 255
for i in range(1, edge_map.shape[0] - 1):
    for j in range(1, edge_map.shape[1] - 1):
        if weak_edges[i, j]:
            if np.any(strong_edges[i-1:i+2, j-1:j+2]):
                edge_map_final[i, j] = 255

#######################################################################################
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(edge_map_final, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

plt.show()
