import numpy as np

# import cv2 as cv
# import PIL as pil
# from PIL import Image

import tensorflow as tf
from tensorflow import keras


import pandas as pd

import model as SVM

svm = SVM.create_model()

csv_file = pd.read_csv("test_xx_annotations_download_car_bus.csv" , nrows=167)

# print(csv_file.head())

csv_file['classes'] = pd.Categorical(csv_file['classes'])
csv_file['classes'] = csv_file.classes.cat.codes
classes = csv_file.pop('classes')

image = np.load("picture_array.npy")
# image_reshape = image.reshape([501 ,416*416*3])
image_tem = np.vsplit(image, 3)
image_reduce = image_tem[0]
print(image_reduce.shape)

# print(csv_file.head())

img_path = csv_file.pop('path')

# print(csv_file.head())

dataset = tf.data.Dataset.from_tensor_slices(( csv_file.values, classes.values))
image_set = tf.data.Dataset.from_tensor_slices((image_reduce))

for ele in dataset:
  print(ele)  

svm.summary()

svm.fit(dataset,image , epochs=20, batch_size=1, steps_per_epoch=256)
