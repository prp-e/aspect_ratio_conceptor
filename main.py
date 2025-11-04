import cv2
import numpy as np 

def create_white_image(width_ratio, height_ratio):
    height = 1024 * height_ratio
    width = 1024 * width_ratio 

    image_array = np.ones((height, width, 3), dtype=np.uint8) * 255 

    return image_array

image_array = create_white_image(9, 16)
print(image_array.shape)
cv2.imwrite("final_image.jpg", image_array)