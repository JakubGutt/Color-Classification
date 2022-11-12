import cv2
import imutils
import argparse
import numpy as np

W,H = 560, 800
offsetX = -0.05 * W
offsetY = -0.01 * H

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", type=str,
	default="DICT_ARUCO_ORIGINAL",
	help="type of ArUCo tag to generate")

ap.add_argument(
  "--image",
  type=str,
  required=True
)

args = vars(ap.parse_args())

image = cv2.imread(args['image'])

ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL
}

if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(
		args["type"]))
	sys.exit(0)

arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,
	parameters=arucoParams)

if len(corners) != 4:
    print("Cannot detect right amount of markers!")
    exit()

ids = ids.flatten()

ids, corners = zip(*sorted(zip(ids, corners)))
detected_points = np.zeros((4,2), dtype=np.float32)

cv_custom_point_order = [1,0,2,3]

for i, (markerCorner, markerID) in enumerate(zip(corners, ids)):
    corners = markerCorner.reshape((4, 2))

    detected_points[i][0] = int(corners[cv_custom_point_order[i]][0])
    detected_points[i][1] = int(corners[cv_custom_point_order[i]][1])

target_points = np.float32([[offsetX, offsetY], [W-offsetX,offsetY], [offsetX,H-offsetY], [W-offsetX, H-offsetY]])

matrix = cv2.getPerspectiveTransform(detected_points, target_points)

img = cv2.warpPerspective(image, matrix, (W,H), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))

cv2.imwrite("output.jpg", img)
