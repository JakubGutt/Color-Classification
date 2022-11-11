import cv2
import numpy as np

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)

num = 4

# allocate memory for the output ArUCo tag and then draw the ArUCo
# tag on the output image
tag = np.zeros((300, 300, 1), dtype="uint8")
cv2.aruco.drawMarker(arucoDict, num+5, 300, tag, 1)

# write the generated ArUCo tag to disk and then display it to our
# screen
cv2.imwrite(str(num)+".png", tag)