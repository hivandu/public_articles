'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2024-10-13 23:01:08
'''
import numpy as np
import skimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import scipy.misc as sm

def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def load_data(dir_name = 'faces_imgs'):
    '''
    Load images from the 'faces_imgs' directory Images are in JPG and we convert it to gray scale images
    '''

    imgs = []
    valid_extensions = ['.jpg', '.jpeg', '.png'] # Add more extensions if needed
    for filename in os.listdir(dir_name):
        file_ext = os.path.splitext(filename)[1].lower() # Get file extension
        if os.path.isfile(os.path.join(dir_name, filename)) and file_ext in valid_extensions:
            img = mpimg.imread(os.path.join(dir_name, filename))
            img = rgb2gray(img)
            imgs.append(img)

    return imgs


def visualize(imgs, format=None, gray=False):
    plt.figure(figsize=(20, 40))
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1, 2, 0)
        plt_idx = i+1
        plt.subplot(2, 2, plt_idx)
        plt.imshow(img, format)
    plt.show()