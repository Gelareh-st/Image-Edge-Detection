import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from PIL import Image

image= Image.open("./images/coins.png")

# Sobel operator for edge detection (horizontal and vertical gradients)
sobel_h = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_v = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Filter the image with the Sobel operator using 2D convolution
edges_h = convolve2d(image, sobel_h, mode='same', boundary='wrap')
edges_v = convolve2d(image, sobel_v, mode='same', boundary='wrap')

# Calculate the magnitude of edges from horizontal and vertical gradients
edges_mag = np.sqrt(edges_h**2 + edges_v**2)

# Convert the edges to black and white using a threshold
threshold = 100  
edges_h = (edges_h > threshold) * 255
edges_v = (edges_v > threshold) * 255
edges_wh = (edges_mag > threshold) * 255

##############################################################################################33
plt.figure(figsize=(6, 6))

plt.subplot(2,2 , 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(edges_h, cmap='gray')
plt.title('Edges h')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(edges_v, cmap='gray')
plt.title('Edges v')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(edges_mag, cmap='gray')
plt.title('Edges Sobel')
plt.axis('off')

plt.show()

