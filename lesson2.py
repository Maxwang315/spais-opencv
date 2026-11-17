import cv2
import numpy as np

# 1. Load the photo (check for None: imread fails silently)
img = cv2.imread("Chaewon.jpg")
if img is None:
    raise SystemExit("Couldn't load Chaewon.jpg - check the file name and folder")

# Shrink big phone photos so windows fit on screen
img = cv2.resize(img, None, fx=1, fy=1)
print("BGR shape:", img.shape)

# 2. Grayscale: 3 channels -> 1 channel (brightness only)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("gray shape:", gray.shape)

# 3. HSV: same 3 channels, different meaning (hue, saturation, value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
center = hsv[img.shape[0] // 2, img.shape[1] // 2]
print("HSV of center pixel:", center)

# 4. Mask: which pixels fall inside our "orange" range?
lower_orange = np.array([0, 100, 90])
upper_orange = np.array([20, 255, 255])
mask = cv2.inRange(hsv, lower_orange, upper_orange)
print("mask shape:", mask.shape, "unique values:", np.unique(mask))

# 5. Keep only the orange pixels from the original photo
orange_only = cv2.bitwise_and(img, img, mask=mask)

# 6. A real number a robot could use: how much of the view is vegetation?
ornage_fraction = cv2.countNonZero(mask) / mask.size
print(f"orange coverage: {ornage_fraction:.1%}")

cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("mask", mask)
cv2.imshow("orange only", orange_only)
cv2.waitKey(0)
cv2.destroyAllWindows()
