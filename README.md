  
  

# Color Classification

  

Program to detect colors in different lightnings and conditions using generated color board.

  

---

  

# Table of contents

  

1. [Requirements](#requirements)

2. [How to use](#how-to-use)

3. [How it works](#how-it-works)

5. [Example](#example)

  
  

---

  

# Requirements <a name="requirements"></a>

  

- Linux (tested on Ubuntu 22.04 LTS)

  

- OpenCV, Numpy

```python

pip install -r ./requirements.txt

```

  

---

  

# How to use <a name="how-to-use"></a>

  

### Generating board

  

Before detecting colors we need to generate color board. For this purpose we will be using `generateBoard.py`. This file takes in two arguments, `--type` (for selecting specific aruco dictionary) and `--input_file` (for declaring target colors).


Example:

```bash

python3 generateBoard.py --type DICT_5X5_100 --input_file colors.txt

```

  

Colors file should look like this:

```
red: original=[255,0,0]
green: original=[0,255,0]
blue: original=[0,0,255]
```

It can have as many colors as user wants but remember to add spaces, commas...

  

`type` can only have one of these values:

  

```DICT_4X4_50,

DICT_4X4_100,

DICT_4X4_250,

DICT_4X4_1000,

DICT_5X5_50,

DICT_5X5_100,

DICT_5X5_250,

DICT_5X5_1000,

DICT_6X6_50,

DICT_6X6_100,

DICT_6X6_250,

DICT_6X6_1000,

DICT_7X7_50,

DICT_7X7_100,

DICT_7X7_250,

DICT_7X7_1000,

DICT_ARUCO_ORIGINAL

```

Default value is `DICT_ARUCO_ORIGINAL`

  

Generated board will have the same width to height ratio as A4 sheet so it can be easily printed.

  

---

  

### Detecting colors on board

  

When we have a printed board we need to take pictures of it in desired lightning.

  

Run `detectColors.py` and pass image as input.

  

```bash

python3 detectColors.py --type DICT_5X5_100 --image path/to/image.png --input_file colors.txt

```


  

`--input_file` should be the path to the file described in `Generate Board` section.

  

In order for Aruco tags to be detected we need to use the same `--type` as in `generateBoard.py`.

  

If algorithm detects right amount of aruco tags each color in input file will have `detectedColor` section.

  

---

  

### Classifying colors

  

Now is the time for classifying color by using `classifyColor.py`.

  

```bash

python3 classifyColor.py --input_file colors.txt --color [67,68,69] --method rgb --max_dist 0.3

```

  

`--input_file` is a path to colors file is step above.

  

`--color` is a color we want to classify in RGB.

  

`--method` can be either `hsv` or `rgb`. If you want to learn more, go to [How it works](#how-it-works). Default `rgb`.

  

`max_dist` is a float number in range <0, 1>. It controls maximum distance from template color for color to be classified as this template color. `0` means that input color needs to be exactly the same as some template color and `1` means that every input color will be classified as some template color. Default `0.2`.

  

# How it works <a name="how-it-works"></a>

  

Board generation is done using OpenCV. Aruco markers are placed in specific order (by ID) so we know which marker is in which corner. Input colors are generated from the top to the bottom (order is the same as in console input array).

  

#### Detecting colors consists of three steps:

- Aruco tag detection.

- Applying perspective transform to input image using detected markers so we get board colors in the same view as generated board.

- Calculating average colors for each section using `n_colors` and writing it to output file.

  

Classifying colors is done by picking closest color in given color space that is closer than `--max_dist`.

  

If `--method` is equal to `rgb` this calculation will take place in RGB color space.

If `--method` is equal to `hsv` this calculation will take place in HSV color space.

It is recommended to try classifying colors using both methods and pick better one for the job.

  

---


# Visualize detected colors

There is also visualize colors option. It shows which colors can be classified as each input color.

```bash
python3 visualizeColors.py --input_file colors.txt --max_dist 0.15
```
 
Running above commend will generate `visualizedColors.png` with grid of different colors. 

Rows in this file correspond to lines in colors.txt. First column represents original detected color and the rest shows different shades which can be classified as this color.
  

# Example <a name="example"></a>

  

TODO

  

kamerka do detect colors

//wizualizacja zakresow??

//cv Mean do average coloru z boarda

//słownik colorów

kółka do testowania hough circles

//plik z kolorami razem z generate board
