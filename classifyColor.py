import argparse
import ast
import math

ap = argparse.ArgumentParser()

ap.add_argument(
  "--template_colors",
  type=str,
  default='detectedColors.txt'
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
  type=int,
  default=20
)

args = vars(ap.parse_args())

if args['method'] not in ['rgb', 'hsv']:
    print("Unidentified method!!")
    exit()

color = ast.literal_eval(args['color'])
template_colors = []

with open(args['template_colors']) as f:
    for line in f.readlines():
        template_color = []
        for val in line.split(","):
            template_color.append(int(val))
        template_colors.append(template_color)

def distBetweenColors(col1, col2):
    return math.sqrt((col1[0]-col2[0])**2 + (col1[1]-col2[1])**2 + (col1[2]-col2[2])**2)

closest_color = 0
closest_dist = 1e+8
for i, template_color in enumerate(template_colors):
    dist = distBetweenColors(template_color, color)
    if dist < closest_dist:
        closest_color = i
        closest_dist = dist

if closest_dist > args['max_dist']:
    print("Input color doesn't classify to any of template colors")
    exit()

print("Template colors: ", template_colors)
print("Closest color to", color, "is", template_colors[closest_color], "dist:", closest_dist)