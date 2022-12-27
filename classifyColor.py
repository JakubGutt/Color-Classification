import argparse
import ast
import math
import colorsys

ap = argparse.ArgumentParser()

ap.add_argument(
  "--input_file",
  type=str,
  default='inputColors.txt'
)

ap.add_argument(
  "--color",
  type=str,
  required=True
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

color = ast.literal_eval(args['color'])
template_colors = {}

with open(args['input_file']) as f:
    for line in f.readlines():
        splitted = line.split(' ')
        if len(splitted) != 3:
            print("Wrong input file")
            exit()
        template_colors[splitted[0][:-1]] = ast.literal_eval(splitted[-1].split('=')[1])

print(template_colors)

def distBetweenColors(col1, col2):
    if args['method'] == 'hsv':
        col1 = colorsys.rgb_to_hsv(col1[0]/255.0, col1[1]/255.0, col1[2]/255.0)
        col2 = colorsys.rgb_to_hsv(col2[0]/255.0, col2[1]/255.0, col2[2]/255.0)

    return math.sqrt((col1[0]-col2[0])**2 + (col1[1]-col2[1])**2 + (col1[2]-col2[2])**2)

closest_color = 0
closest_dist = 1e+8

for i, template_color in enumerate(template_colors):
    dist = distBetweenColors(template_colors[template_color], color)
    if dist < closest_dist:
        closest_color = i
        closest_dist = dist

max_dist = 0
if args['method'] == 'rgb':
    max_dist = args['max_dist'] * math.sqrt(195075) # Max distance in RGB space
elif args['method'] == 'hsv':
    max_dist = args['max_dist'] * math.sqrt(3) # Max distance in HSV space

if closest_dist > max_dist:
    print("Input color doesn't classify to any of template colors")
    exit()

print("Template colors: ", template_colors)
print("Closest color to", color, "is", template_colors[closest_color], "dist:", closest_dist)