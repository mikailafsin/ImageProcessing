import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("gorsel.jpg", 0)
cv2.imshow("Image Processing", image)
cv2.waitKey()

shape = image.shape
height = shape[0]
width = shape[1]

arrayOfHistogram = np.zeros(256)

for i in range(0, height):
    for j in range(0, width):
        arrayOfHistogram[image[i][j]] = arrayOfHistogram[image[i][j]] + 1

print(arrayOfHistogram)

plt.figure("Histogram")
plt.xlabel("0-255 Color Values of Pixels")
plt.ylabel("Intensitive of the Points")
plt.plot(arrayOfHistogram)
plt.show()