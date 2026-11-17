import cv2
import numpy as np
# 1. Make a blank black image: 300 rows tall, 400 columns wide, 3 channels
img = np.zeros((300, 400, 3), dtype=np.uint8)
print("shape:", img.shape, "dtype:", img.dtype)

# 2. "Paint" by assigning values to slices: img[rows, cols]
img[50:150, 50:200] = (255, 0, 0)
img[150:250, 200:350] = (0, 0, 255)

# 3. Read a single pixel. Note: [y, x], i.e. row first, then column
print("pixel at (100,100):", img[100, 100])

# 4. Save to disk, then load it back
cv2.imwrite("my_first_image.png", img)
loaded = cv2.imread("my_first_image.png")
print("same?", np.array_equal(img, loaded))

# 5. Show it in a window (press any key to close)
cv2.imshow("lesson 1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
