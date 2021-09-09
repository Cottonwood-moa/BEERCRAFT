from django.shortcuts import render

# =================================
import tensorflow as tf
import tensorflow_hub as hub
# =================================
import IPython.display as display

import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np
import PIL.Image
import time
import functools
import test as t

print(t.test(1,2))

# def tensor_to_image(tensor):
#   tensor = tensor*255
#   tensor = np.array(tensor, dtype=np.uint8)
#   if np.ndim(tensor)>3:
#     assert tensor.shape[0] == 1
#     tensor = tensor[0]
#   transedImg = PIL.Image.fromarray(tensor)
#   transedImg.save("Test.png",'PNG')
#   return transedImg

# def load_img(path_to_img):
#   max_dim = 512
#   img = tf.io.read_file(path_to_img)
#   img = tf.image.decode_image(img, channels=3)
#   img = tf.image.convert_image_dtype(img, tf.float32)

#   shape = tf.cast(tf.shape(img)[:-1], tf.float32)
#   long_dim = max(shape)
#   scale = max_dim / long_dim

#   new_shape = tf.cast(shape * scale, tf.int32)

#   img = tf.image.resize(img, new_shape)
#   img = img[tf.newaxis, :]
#   return img

# Create your views here.
def index(request):
  if request.method == 'POST':
    # content_path = tf.keras.utils.get_file('YellowLabradorLooking_new.jpg', 'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg')
    # style_path = tf.keras.utils.get_file('kandinsky5.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')
    # content_image = load_img(content_path)
    # style_image = load_img(style_path)
    # hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')
    # stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    # transedImg = tensor_to_image(stylized_image)
    # return render(request, 'imageTrans/test.html',{'transedImg' : transedImg})
    return render(request, 'imageTrans/test.html')
  else:
    return render(request, 'imageTrans/index.html')
