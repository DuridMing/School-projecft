import numpy as np
import cv2 as cv
import PIL as pil
from PIL import Image


import pandas as pd



csv_file = pd.read_csv("test_xx_annotations_download_car_bus.csv" ,nrows=500)


csv_file['classes'] = pd.Categorical(csv_file['classes'])
csv_file['classes'] = csv_file.classes.cat.codes
classes = csv_file.pop('classes')

print(csv_file.head())

img_path = csv_file.pop('path')

all_images_array = np.empty([1,416, 416, 3], dtype="float32" )

count = 0

ori = "picture_array"
array_file_name = "picture_array"
fcount = 0

for path in img_path:
    image = cv.imread(path)
    resize_image = cv.resize(image, (416, 416), interpolation=cv.INTER_AREA)
    # print(image.shape)
    # print(resize_image.shape)

    pimage = Image.fromarray(resize_image)
    image_array = np.asarray(pimage)
    image_array = np.expand_dims(image_array, axis=0)
    # print(image_array.shape)
    # print(all_images_array.shape)

    # print(image_array)
    # print(classes)
    all_images_array = np.append(all_images_array, image_array, axis=0)
    print(all_images_array.shape)
    count += 1

    if count % 250 == 0:
        np.save(array_file_name, all_images_array)
    if count % 5000 == 0:
        fcount += 1
        array_file_name = ori + "_" + str(fcount)
        all_images_array = np.empty([416, 416, 3, 1], dtype="float32")

