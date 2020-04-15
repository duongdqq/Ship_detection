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

            x_min = x_center_random - 320
            y_min = y_center_random - 180
            x_max = x_center_random + 320
            y_max = y_center_random + 180
            # cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            # cv2.circle(img, (x_center_random, y_center_random), radius, color, thickness)
            crop = img[y_min:y_max, x_min:x_max]
            cv2.imshow('crop', crop)
            cv2.waitKey(0)

            images.append(img)


if __name__ == '__main__':
    folder = '/media/veec20/Data/duongdq/datasets/test/'
    get_small_img(folder)
