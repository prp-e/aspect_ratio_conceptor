import cv2
import numpy as np 

height = 1024
width = 1024

image_array = np.ones((width, height, 3), dtype=np.uint8) * 255 

cv2.imwrite("final_image.jpg", image_array)