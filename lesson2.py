'''
Why BGR isn’t enough:
BGR describes a color as amounts of three lights mixed together. 
The problem: “green” isn’t a simple range in BGR. 
A sunlit leaf might be (60, 200, 90) and the same leaf in shadow (20, 70, 30). 
All three numbers changed, so “is this pixel green?” becomes messy math.


HSV reorganizes color the way humans think about it:

H: Hue, which color (red, yellow, green, blue…). It works like an angle around a color wheel.
S: Saturation, how vivid it is (grayish → pure color).
V: Value, how bright it is (dark → bright)
'''


import cv2
import numpy as np

img = cv2.imread("Download an image yourself here and read it")
if img is None:
    raise SystemExit("Couldn't load image")

# scales the image to 25% width and height. Phone photos are around 4000 px wide, which is far bigger than your screen. 
# None means “I’m giving you scale factors instead of an exact size.”
img = cv2.resize(img, None, fx=0.25, fy=0.25)
print("BGR shape:", img.shape)

# convert color. The second argument names the conversion: from BGR to grayscale. 
# The result has shape (h, w), with no third dimension, because each pixel is now one number. 
# Grayscale is common when color doesn’t matter (edges, shapes), and it’s 3× less data.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("BGR shape:", gray.shape)

# same function, different conversion. Shape stays (h, w, 3), 
# but now channel 0 is hue, 1 is saturation, and 2 is value. 
# (There’s also COLOR_BGR2RGB, which is the fix for the Lesson 1 problem before sending frames to models.)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("HSV shape:", hsv.shape)
center = hsv[img.shape[0]//2, img.shape[1]//2]
print("HSV of centre pixel:", center)

lower_orange = np.array([0, 100, 90])
upper_orange = np.array([20, 255, 255])
# checks every pixel: “are H, S, and V all between these bounds?” 
# Yes → 255 (white), no → 0 (black). The output is a mask, a black-and-white map of “where the green stuff is.” 
# That’s why unique values prints [0 255].
# S ≥ 40 throws out grayish pixels (concrete, overcast sky).
# V ≥ 40 throws out near-black pixels, where hue is basically noise.
mask = cv2.inRange(hsv, lower_orange, upper_orange)
print("mask shape:", mask.shape, "unique values:", np.unique(mask))


# keeps the original pixel wherever the mask is white and blacks it out everywhere else. 
# A stencil: spray paint only goes through the holes.
orange_only = cv2.bitwise_and(img, img, mask=mask)


# the fraction of white pixels. A robot could use exactly this to answer “am I looking at a crop row or bare soil?”
orange_fraction = cv2.countNonZero(mask) / mask.size
print(f"orange coverage: {orange_fraction:.1%}")

cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("mask", mask)
cv2.imshow("orange only", orange_only)
cv2.waitKey(0)
cv2.destroyAllWindows()