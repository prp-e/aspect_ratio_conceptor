import cv2
import numpy as np 
import base64

def create_white_image(width_ratio, height_ratio):
    height = 128 * height_ratio
    width = 128 * width_ratio 

    image_array = np.ones((height, width, 3), dtype=np.uint8) * 255 

    return image_array

image_array = create_white_image(1, 1)
_, encoded_image = cv2.imencode(".jpg", image_array)
base64_image = base64.b64encode(encoded_image.tobytes()).decode("utf-8")

print(base64_image)