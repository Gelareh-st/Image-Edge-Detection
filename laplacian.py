import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

image= Image.open("./images/coins.png")

# Define the Laplacian matrix with different alpha values
def laplacian_matrix(alpha):
    laplacian = np.array([[0, 1, 0],
                          [1, -4, 1],
                          [0, 1, 0]])
    return alpha * laplacian

# Define alpha values for the Laplacian matrix
alphas = [1.5, 1.0, 0.5]

#################################################################################################
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

for i, alpha in enumerate(alphas, start=2):
    laplacian = laplacian_matrix(alpha)
    edges = convolve2d(image, laplacian, mode='same', boundary='wrap')
    
    # Convert the edges to black and white using a threshold
    threshold = 100 
    edges_bw = (edges > threshold) * 255
    
    plt.subplot(2, 2, i)
    plt.imshow(edges_bw, cmap='gray')
    plt.title(f'Edges (Laplacian, α={alpha})')
    plt.axis('off')

plt.show()
