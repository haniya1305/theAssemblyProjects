import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Displaying Image on the screen
# img = cv2.imread("cat.png", cv2.IMREAD_COLOR)
# cv2.imshow("Cat Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 2. Color Space
# image = cv2.imread('RGB.png')
# B, G, R = cv2.split(image)
#
# cv2.imshow("original", image)
# cv2.waitKey(0)

# cv2.imshow("blue", B) # or G or R
# cv2.waitKey(0)

# 3. Corner Point Detection on Images
# img = cv2.imread('shapes.png')

# original image -> gray scale image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack
# corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
# corners = np.int0.(corners)
#
# for i in corners:
#     x, y = i.ravel()
#     cv2.circle(img, (x, y), 2, 255, -1)
#
# plt.imshow(img), plt.show()

# 4. Coordinates of an image using event attributes
# def click_event(event, x, y, flags, params):
#     # checking for button click
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # displaying the coordinates on the console
#         print('(',x, ', ', y,')')
#         # displaying the coordinates on the image
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         fontSize = 1
#         coordinates = (x,y)
#         color = (0, 0, 255)
#         width = 2
#         cv2.putText(img, str(x) + ',' + str(y), coordinates, font, fontSize, color, width)
#         cv2.imshow('image', img)
#
# img = cv2.imread('cat.png')
# cv2.imshow('image', img)
# # setting mouse handler for the image and calling the click_event() function
# cv2.setMouseCallback('image', click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()