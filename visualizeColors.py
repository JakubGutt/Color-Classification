import argparse
import ast
import math
import colorsys
import numpy as np
import cv2

ap = argparse.ArgumentParser()

ap.add_argument(
  "--input_file",
  type=str,
  default='inputColors.txt'
)

ap.add_argument(
  "--method",
  type=str,
  default="rgb"
)

ap.add_argument(
  "--max_dist",
  type=float,
  default=0.2
)

args = vars(ap.parse_args())

if args['method'] not in ['rgb', 'hsv']:
    print("Unidentified method!!")
    exit()

template_colors = {}

with open(args['input_file']) as f:
    for line in f.readlines():
        splitted = line.split(' ')
        if len(splitted) != 3:
            print("Wrong input file")
            exit()
        template_colors[splitted[0][:-1]] = ast.literal_eval(splitted[-1].split('=')[1])

print(template_colors)

max_dist = 0
if args['method'] == 'rgb':
    max_dist = args['max_dist'] * math.sqrt(195075) # Max distance in RGB space
elif args['method'] == 'hsv':
    max_dist = args['max_dist'] * math.sqrt(3) # Max distance in HSV space

W, H = 2480, 3508
image = np.zeros((H, W, 3), np.uint8)
points = [[0,0,-1], [0,0,1], [1,0,0], [-1,0,0], [0,1,0], [0,-1,0]]
col_size = W // 6
row_size = H // len(template_colors)

# Variable names r,g,b are not accurate, it can be hsv 
for i, color in enumerate(template_colors):
    for j, dir in enumerate(points):
        r = template_colors[color][0] + dir[0] * max_dist
        g = template_colors[color][1] + dir[1] * max_dist
        b = template_colors[color][2] + dir[2] * max_dist
        cv2.rectangle(image, (j*col_size, i*row_size), ((j+1)*col_size, (i+1)*row_size), (b,g,r), -1)

cv2.imwrite("visualizedColors.png", image)
