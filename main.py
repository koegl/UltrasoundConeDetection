import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/Users/fryderykkogl/Desktop/cone.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, threshold1=0, threshold2=10)

plt.imshow(edges, cmap="gray")
plt.show()
