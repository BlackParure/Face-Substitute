import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def grasp_image_information(path):
    """
    grasp the pgm image informations(azimuth, elevation, body, etc.)
    :param path: the path of the image
    :return: a dictonary contains the information of the pgm image
    """
    img_info = {}
    img_info["array"] = np.array(cv2.imread(path))

    img_name = os.path.split(path)[-1]
    img_details = img_name[11: -4]

    if img_details == "_Ambient":
        img_info["type"] = "Ambient"
    else:
        img_info["type"] = "Non-Ambient"
        img_info["azimuth"] = int(img_details[1: 5])
        img_info["elevation"] = int(img_details[7: 10])
    return img_info

def file_filter(path):
    """
    only return the path of the .pgm image under the objective path
    :param path: the path of the directory
    :return: list of pgm image
    """
    files = os.listdir(path)
    images = []
    for file in files:
        if file.endswith(".pgm"):
            images.append(os.path.join(path, file))
    return images

def cache_images(path):
    """
    cache_images in a list
    :param path: the path of the directory
    :return: a list that contains the information of the images
    """
    images = []
    images_path = file_filter(path)
    for image_path in images_path:
        images.append(grasp_image_information(image_path))

    return images

if __name__ == "__main__":
    images_path = r"D:\library\python\opencv\04\yaleB02"
    imgs = cache_images(images_path)
    print(imgs)
