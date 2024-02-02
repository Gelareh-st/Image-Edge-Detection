import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

image= Image.open("./images/coins.png")

# Roberts Cross operator for edge detection
roberts_cross_h = np.array([[1, 0], [0, -1]])
roberts_cross_v = np.array([[0, 1], [-1, 0]])

# Filter the image with the Roberts Cross operator using 2D convolution
edges_h = convolve2d(image, roberts_cross_h, mode='same', boundary='wrap')
edges_v = convolve2d(image, roberts_cross_v, mode='same', boundary='wrap')

# Calculate the magnitude of edges from horizontal and vertical gradients
edges_mag = np.sqrt(edges_h**2 + edges_v**2)

# Convert the edges to black and white using a threshold
threshold = 100 
edges_bw = (edges_mag > threshold) * 255

##########################################################################################3
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_bw, cmap='gray')
plt.title('Edges Roberts Cross')
plt.axis('off')

plt.show()
