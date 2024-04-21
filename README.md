pip3.py walks directories named by a single digit like '0' and '1' and calls a list of functions with a screenshot image until it returns True. This process creates a pip0.json output file used by pipj.py to create the web page. 

The functions are in the pip3m.py import and their names are:

**isSysInfo()**

This screenshot opportunity is created when you enter the space station through the teleporter. The screen is identified by the double slashes // in the bottom left corner. OpenCV is used to capture the following information. It's extremely important that this information has a dark background so that the OCR can read it.
```
System Info
 Celestial Bodies: 5 Planets
 Dominant Lifeform: Korvax
 Economy: Construction // Flourishing
 Conflict level: Stable
```
**isVisited()**

This screenshot is identified by 'VISITED SYSTEMS' in the upper left of the screen. It's important to note that there are 3 different screens identified here. 

1. SetSysten screen with no visible system or planet 'card'.

This is used to set the System name prior to a batch of Resources and Biomes for that System.

2. Biome screen with cursor over the plant on the left side of the screen showing the Biome in a planet 'card'.

3. Sysinfo screen with the cursor over the system on the left side of the screen showing the SysInfo in a system 'card'.
This is good alternative to get SysInfo in a system without a space station.

**isGlyphs()**

This screenshot MUST follow the SysInfo screenshot to get captured.

Glyphs: 106202 900054

The NMS-Glyphs-Mono.ttf is used to display these hex digits correctly.

**isTechno()**

This screenshots is identified by 'Avaliable to Buy' in the upper right. These screens are either of the Galactic Terminal or Technology Merchants.

**isResource()**

This screenshot is identified by the Icons lined-up on the left side. These screens capture planet info and planet resources.

**isStellar()**

This screenshot is found in the missions 'Log' tab and selecting the Exploration Guide.
This captures the "Stellar Classification" for the system color.
Note: Yellow is F or G, Red is K or M, Green is E, Blue is B or O 

The Python libraries needed are:
```
import imutils
import cv2 # OpenCV
import numpy as np
import pytesseract
```
pytesseract OCR creates a lot of spelling error with roman numerals so the `fix` dictionary in pip3m.py is used to fix them.

POI's are added using the `poi` dictionary in pipj.py. The format is html syntax that is inserted between divs. The keys are planets or systems.

The indentation of the web page was based on the idea of this css `div {padding-left: 10px;}` and the `json` input.

Checkout the Demo.pdf and [visit](https://shirha.github.io/expedition/) the Github Pages for this project.

***

```
This is my recent environment created with [Miniforge](https://github.com/conda-forge/miniforge) / Mamba

Download and install Miniforge3-Windows-x86_64.exe v24.3
(base) C:\Users\shirha>mamba create --name opencv --clone base
(base) C:\Users\shirha>mamba activate opencv
(opencv) C:\Users\shirha>python --version
Python 3.10.14
(opencv) C:\Users\shirha>mamba install libopencv opencv py-opencv
(opencv) C:\Users\shirha>mamba install numpy
  All requested packages already installed
(opencv) C:\Users\shirha>mamba install tesseract
(opencv) C:\Users\shirha>mamba install pytesseract
(opencv) C:\Users\shirha>mamba install imutils

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\shirha\miniforge3\envs\opencv\Library\bin\tesseract.exe'
```






