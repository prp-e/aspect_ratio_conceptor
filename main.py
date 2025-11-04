from uuid import uuid4
import cv2
import numpy as np 
import base64

def create_white_image(width_ratio, height_ratio):
    '''Creates a blue image to be distinguished easier'''
    height = 128 * height_ratio
    width = 128 * width_ratio 

    image_array = np.zeros((height, width, 3), dtype=np.uint8) * 255 
    image_array[:, :, 0] = 255
    
    return image_array

def base64_image_creator(image_array):
    _, encoded_image = cv2.imencode(".jpg", image_array)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode("utf-8")

    return base64_image

def save_image(base64_image):
    image_binary = base64.b64decode(base64_image)
    final_name = f'{uuid4()}.jpg'

    with open(final_name, 'wb') as img:
        img.write(image_binary)