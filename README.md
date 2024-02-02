# Image-Edge-Detection

Image edge detection is the process of identifying and locating the boundaries of objects in an image.Edge detection algorithms work by analyzing the changes in pixel intensity values across an image. Edges correspond to areas where the intensity changes abruptly, such as the boundary between a foreground object and the background.

## 1. Sobel Operator

This method uses two 3x3 kernels to calculate the gradient in the x and y directions and then combines them to find the edges.
### Filter Mask
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/822f179e-1a82-48b9-98e2-6d2ba96d89d7)

### Output
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/5871bf4f-ece1-4a39-a7dc-fff7e4895c73)



## 2. Canny Edge Detection

This is a popular method that uses a multi-stage algorithm to detect edges. It involves applying a Gaussian filter to smooth the image, calculating the gradient magnitude and direction, suppressing non-maximum edges, and finally applying hysteresis thresholding to obtain the final edges.

### Output
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/c270a948-2170-451e-b659-93679b234dab)


## 3. Laplacian of Gaussian (LoG)

This method applies a Gaussian filter to the image and then applies the Laplacian operator to detect edges.

### Filter Mask
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/62f13021-e6f2-4a92-8344-a37fac444ce5)

### Output
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/3c774ee3-62e0-406d-bd6a-5a6707d415c4)


## 4. Roberts Cross Operator

This method uses two 2x2 kernels to calculate the gradient in the x and y directions and then combines them to find the edges.

### Filer Mask
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/4b2e8eea-a64f-4b42-a7d1-4287a0a5bf2c)


### Output
![image](https://github.com/Gelareh-st/Image-Edge-Detection/assets/85786544/b4a2a70f-9a2a-49f5-80b6-a1401b29c6eb)

