

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

Before detecting colors we need to generate color board. For this purpose we will be using `generateBoard.py`. This file takes in two arguments, `--type` (for selecting specific aruco dictionary) and `--colors` (for declaring target colors).

Example:
```bash
python3 generateBoard.py --type DICT_5X5_100 --colors "[(190, 180, 170), (23, 24, 25)]"
``` 

`--colors` can have arbitrary length.  Please note that color array is inside quotes and single RGB color is inside parentheses.

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
python3 detectColors.py --type DICT_5X5_100 --image path/to/image.png --n_colors 2
```

where `--n_colors` is the length of `--colors` array when generating board. 

In order for Aruco tags to be detected we need to use the same `--type` as in `generateBoard.py`.

If algorithm detects right amount of aruco tags `detectedColors.txt` will be created. Each line in this file corresponds to average RGB color on detected board. It will be used later as reference points for each color.

---

### Classifying colors 

Now is the time for classifying color by using `classifyColor.py`.

```bash
python3 classifyColor.py --template_colors /path/to/generated/txt/file.txt --color [67,68,69] --method rgb --max_dist 0.3
``` 

`--template_colors` is a path to generated `detectedColors.txt` file is step above. Default `./detectedColors.txt`.

`--color` is a color we want to classify in RGB.

`--method` can be either `hsv` or `rgb`. If you want to learn more, go to [How it works](#how-it-works). Default `rgb`.

`max_dist` is a float number in range <0, 1>. It controls maximum distance from template color for color to be classified as this template color. `0` means that input color needs to be exactly the same as some template color and `1` means that every input color will be classified as some template color. Default `0.2`.

# How it works <a name="how-it-works"></a>

Board generation is done using OpenCV. Aruco markers are placed in specific order (by ID) so we know which marker is in which corner. Input colors are generated from the top to the bottom (order is the same as in console input array).

#### Detecting colors consists of three steps:
-  Aruco tag detection.
- Applying perspective transform to input image using detected markers so we get board colors in the same view as generated board.
- Calculating average colors for each section using `n_colors` and writing it to output file.

Classifying colors is done by picking closest color in given color space that is closer than `--max_dist`.

If `--method` is equal to `rgb` this calculation will take place in RGB color space. 
If `--method` is equal to `hsv` this calculation will take place in HSV color space. 
It is recommended to try classifying colors using both methods and pick better one for the job.

---

# Example <a name="example"></a>

TODO

kamerka do detect colors
wizualizacja zakresow??
//cv Mean do average coloru z boarda
//słownik colorów
kółka do testowania hough circles
//plik z kolorami razem z generate board

generate board dostaje plik z kolorami, detect colors, dopisuje do tego pliku jak te kolory wygladaja na zdjeciu a classify colors dostaje gotowy plik zeby miec nazwy