import cv2
import numpy as np

image = cv2.imread('gorsel.jpg',0)
cv2.imshow("Original Image", image)

shape = image.shape
height = shape[0]
width = shape[1]

invertedImage = np.zeros([height,width], dtype=np.uint8)
for i in range(0, height):
    for j in range(0, width):
        invertedImage[i,j] = 255 - image[i,j]

cv2.imshow("Inverted Image",invertedImage)
cv2.waitKey()