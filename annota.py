from darknet import performDetect
import cv2
import os, sys
import argparse
import glob
import matplotlib.image as mpimg
import numpy as np
import os.path


def annota(object_current):
    with open(current_file.replace(".jpg","")+".txt", 'w') as f:
        for item in object_current:
            f.write("%s " % item)
    f.close()


if __name__ == "__main__":
    folder = '/home/pcu/duong/darknet/data/ship1/exam/'
    images = []
    for filename in os.listdir(folder):
        try:
            img = mpimg.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
                print(filename)
        except:
            print('Cant import ' + filename)
        current_file = str(folder + filename)
        performDetect(current_file)
        object_current = performDetect(current_file)
        annota(object_current)
    images = np.asarray(images)

