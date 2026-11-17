'''
OpenCV:
Open source software library built for cv, image processing, and ML.
Ready made functions for working with images and video
Not a deep learning framework

Numpy: numpy is closely related to a lot of opencv functions, make sure to review numpy basics
Every opencv image is a numpy array, think of it like a spreadsheet where each cell is 
one pixel with values 0 (black) to 255 (white). A color image is three sheets stacked on top of each other, one for each color channel (BGR), so the shape of the array would be (height, width, 3)

Colours:
Unlike most models trained on RGB images, opencv stores colours in the order BGR (blue, green, red), 
so (255, 0, 0) gets you full blue with no green or red. Beware of this 
because most models on huggingface are trained on RGB, 
so passing an opencv image to them directly would swap red and blue. 

'''

import cv2
import numpy as np
# Creates a numpy array (np.) filled with zeros with height 300, width 400, and 3 color channels. 
# As said above, 0 is black, so right now we just have a pure black canvas of 300 x 400 = 120000 pixels, 
# with each cell holding 3 integers
img = np.zeros((300, 400, 3), dtype=np.uint8)

# img.shape gives (300, 400, 3) which shows the dimensions and dtype gives uint8
print("shape:", img.shape, "dtype:", img.dtype)

# Classic numpy slicing. Where 50:150 points to rows 50 to 149, 
# and 50:200 points to columns 50 to 199. 
# So this selects the area, and (255, 0, 0) like we said, is not red but blue. So this sets the area to blue. 
img[50:150, 50:200] = (255, 0, 0)
img[150:250, 200:350] = (0, 0, 255)

# This prints the pixel at row 100 and column 100, row first and column second
# returns [255 0 0]
print("pixel at (100,100):", img[100, 100])

# Saves the image as a PNG file
cv2.imwrite("my_first_image.png", img)

#loads the image that we just saved, or any image into a new array
loaded = cv2.imread("my_first_image.png")

# Check whether every number matches in the two arrays, this will return true
# True only because PNG is lossless
# saving as .jpg, and this will return false, because JPEG compression slightly changes pixel values
print("same?", np.array_equal(img, loaded))

# Opens a window titled “lesson 1” that shows the array as an image
cv2.imshow("lesson 1", img)

# waits forever until we press a key, then the image disappears 
# 1 in this case means 1ms, which is used for live video, showing a new frame every loop
# 3000 would then mean 3 seconds
cv2.waitKey(0)

# Closes the image
cv2.destroyAllWindows()
