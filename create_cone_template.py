import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/Users/fryderykkogl/Desktop/cone.png")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

shape = image.shape

empty = np.zeros(shape)

centre = (1285, -240)
radius = 300
color = (255, 0, 0)
thickness = 2*radius

image = cv2.circle(empty, centre, radius, color, thickness)

centre = (1285, -240)
radius = 2350
color = (255, 0, 0)
thickness = 200
image = cv2.circle(image, centre, radius, color, thickness)


centre = (1285, 100)
radius = 2350
color = (255, 0, 0)
thickness = 600
image = cv2.circle(image, centre, radius, color, thickness)

pts = [(1575, 250),
       (2735, 2300),
       (4000, 10),
       (1000, 100)]
thickness = 30
cv2.polylines(image, np.array([pts]), True, color, thickness)
pts = [(1600, 250),
       (2760, 2300),
       (4000, 10),
       (1000, 100)]
thickness = 55
cv2.polylines(image, np.array([pts]), True, color, thickness)

pts = [(1650, 250),
       (2810, 2300),
       (4000, 10),
       (1000, 100)]
thickness = 100
cv2.polylines(image, np.array([pts]), True, color, thickness)

pts = [(2100, -50),
       (3250, 2000),
       (4000, -1110),
       (1000, -1100)]
thickness = 1000
cv2.polylines(image, np.array([pts]), True, color, thickness)

cv2.flip(image[:, 1275:, :], 1, image[:, :1275, :])
x = 255 - image[:,:,0]

cv2.imwrite("us_cone.png", x)

plt.imshow(x, cmap="gray")
plt.show()
