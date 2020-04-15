import os
import cv2
import random
import numpy as np
from skimage import io, draw


def get_small_img(folder):
    images = []
    radius = 100
    color = (255, 0, 0)
    thickness = 1
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img_shape = img.shape  # [height, width]
            print(img_shape)
            height, width, chanel = img.shape
            x_max_limit = width - 320
            y_max_limit = height - 180
            x_center_random = random.randrange(320, x_max_limit, 25)
            y_center_random = random.randrange(180, y_max_limit, 25)

            x_min_new = x_center_random - 320
            y_min_new = y_center_random - 180
            x_max_new = x_center_random + 320
            y_max_new = y_center_random + 180
            cv2.rectangle(img, (x_min_new, y_min_new), (x_max_new, y_max_new), (0, 255, 0), 1)
            cv2.circle(img, (x_center_random, y_center_random), 10, (255, 0, 0), 1)
            crop = img[y_min_new:y_max_new, x_min_new:x_max_new]
            cv2.imshow('original image', img)
            cv2.imshow('crop', crop)
            cv2.waitKey(0)
            calculate_overlap(filename, x_min_new, x_max_new)
        images.append(img)


def calculate_overlap(filename, x_min_new, y_min_new):
    txt_file = filename.replace('.jpg', '.txt')
    txt_file = filename.replace('.png', '.txt')
    txt_file = filename.replace('.jpg', '.txt')
    f = open(os.path.join(folder, txt_file))
    for line in f.readlines():
        line = line.rstrip('\n')
        x_center_obj, y_center_obj, w_obj, h_obj = line.split(' ')[1:5]
        x_center_obj, y_center_obj, w_obj, h_obj = float(x_center_obj), float(y_center_obj), float(w_obj), float(h_obj)
        print(x_center_obj)
        x_min_obj = x_center_obj - w_obj/2
        y_min_obj = y_center_obj - 180
        x_max_obj = x_center_obj + w_obj/2
        y_max_obj = y_center_obj + 180

    x_center_new = abs((x_max_obj - x_min_new))/2
    y_center_new = abs((y_max_obj - y_min_new))/2


if __name__ == '__main__':
    folder = '/media/veec20/Data/duongdq/datasets/test/'
    get_small_img(folder)
