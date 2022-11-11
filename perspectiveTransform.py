import numpy as np
import cv2

# read input
img = cv2.imread("masno.jpg")

# specify desired output size 
width = 700
height = 500

# specify conjugate x,y coordinates (not y,x)
offset = 150

input = np.float32([[700, 742], [1387,744], [1360,269], [729,378]])
# output = np.float32([[offset,height-offset], [width-offset,height-offset], [width-offset, offset], [offset,offset]])
output = np.float32([[width-offset,height-offset], [offset,height-offset], [offset,offset], [width-offset, offset]])


# compute perspective matrix
matrix = cv2.getPerspectiveTransform(input,output)

print(matrix.shape)
print(matrix)

# do perspective transformation setting area outside input to black
imgOutput = cv2.warpPerspective(img, matrix, (width,height), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))
print(imgOutput.shape)

# save the warped output
cv2.imwrite("output.jpg", imgOutput)

# show the result
cv2.imshow("result", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()