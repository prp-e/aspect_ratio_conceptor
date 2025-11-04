import cv2
import numpy as np 
import base64

def create_white_image(width_ratio, height_ratio):
    height = 128 * height_ratio
    width = 128 * width_ratio 

    image_array = np.ones((height, width, 3), dtype=np.uint8) * 255 

    return image_array

image_array = create_white_image(9, 16)
