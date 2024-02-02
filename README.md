# Image-Edge-Detection

Image edge detection is the process of identifying and locating the boundaries of objects in an image.Edge detection algorithms work by analyzing the changes in pixel intensity values across an image. Edges correspond to areas where the intensity changes abruptly, such as the boundary between a foreground object and the background.

## 1. Sobel Operator

This method uses two 3x3 kernels to calculate the gradient in the x and y directions and then combines them to find the edges.

## 2. Canny Edge Detection

This is a popular method that uses a multi-stage algorithm to detect edges. It involves applying a Gaussian filter to smooth the image, calculating the gradient magnitude and direction, suppressing non-maximum edges, and finally applying hysteresis thresholding to obtain the final edges.

## 3. Laplacian of Gaussian (LoG)

This method applies a Gaussian filter to the image and then applies the Laplacian operator to detect edges.

### Filter Mask
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/62f13021-e6f2-4a92-8344-a37fac444ce5)



## 4. Roberts Cross Operator

This method uses two 2x2 kernels to calculate the gradient in the x and y directions and then combines them to find the edges.
