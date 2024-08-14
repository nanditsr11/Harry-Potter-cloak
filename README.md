# Harry-Potter-cloak

## Description
This project demonstrates the creation of an "invisible cloak" effect using OpenCV and Python. The effect makes the selected red color (e.g., a red cloak) appear transparent, revealing the background as if the object was invisible.

## Requirements
Python 3.x
OpenCV (cv2)
NumPy (numpy)
You can install the required packages using pip:
    pip install numpy opencv-python

## How It Works
Capture the Background: The code first captures the background by taking multiple frames (50 in this case) from the webcam and averaging them to create a background image.

Mask Creation: The code detects the color red in the frame using the HSV color space. Two masks are created to cover the entire range of red hues.

Morphological Transformations: To reduce noise, morphological transformations (like opening and dilation) are applied to the mask.

Masking: The code then creates two masks:

mask1 isolates the red-colored regions (the cloak).
mask2 is the inverse of mask1, isolating everything except the cloak.
Combining Frames:

The isolated cloak area is replaced with the captured background.
The rest of the image remains unchanged.
The two parts are combined to create the final output.
Displaying the Output: The final output is displayed in a window, where the cloak appears invisible, revealing the background instead.

## How to Run
Ensure your webcam is connected and recognized by the system.
Run the Python script:
    python invisible_cloak.py
A window will appear showing the video feed with the invisible cloak effect applied.
Press the Esc key to exit.

## Customization
Color: The code is currently set to detect the color red. You can adjust the lower_red and upper_red HSV ranges to detect other colors.
Background Capture: The code captures the background after a 2-second delay. You can adjust this delay and the number of frames captured to improve the background capture.
