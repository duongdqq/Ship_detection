# run
# python gen_anchors.py -filelist data/train.txt -output_dir ./ -num_clusters 9
'''
Created on Feb 20, 2017

@author: jumabek
'''
from os import listdir
from os.path import isfile, join
import argparse
# import cv2
import numpy as np
import sys
import os
import shutil
import random
import math


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-filelist', default='/media/veec20/Data/duongdq/datasets/data_change_id/person_train2017.txt',
                        help='path to filelist\n')
    parser.add_argument('-output_dir', default='/media/veec20/Data/duongdq/datasets/', type=str,
                        help='Output anchor directory\n')
    parser.add_argument('-num_clusters', default=0, type=int,
                        help='number of clusters\n')

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    f = open(args.filelist)

    lines = [line.rstrip('\n') for line in f.readlines()]

    size = np.zeros((1, 1, 3))
    for line in lines:

        # line = line.replace('images','labels')
        # line = line.replace('img1','labels')
        # line = line.replace('JPEGImages', 'labels')

        line = line.replace('.jpg', '.txt')
        line = line.replace('.png', '.txt')
        line = line.replace('.jpeg', '.txt')
        line = line.replace('.JPG', '.txt')
        txt = line

        print(line)
        f2 = open(line)
        file_path = line
        if os.stat(file_path).st_size == 0:
            continue
        os.remove(txt)
        for line in f2.readlines():
            line = line.rstrip('\n')
            id_class = line.split(' ')[0]
            x_center, y_center, w, h = line.split(' ')[1:5]
            # print(id_class)
            # print(x_center, y_center, w, h)
            if id_class == '0':
                with open(txt, 'a+') as f:
                    f.write("0 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '1':
                with open(txt, 'a+') as f:
                    f.write("0 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '2':
                with open(txt, 'a+') as f:
                    f.write("0 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '4':
                with open(txt, 'a+') as f:
                    f.write("0 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '5':
                with open(txt, 'a+') as f:
                    f.write("0 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '6':
                with open(txt, 'a+') as f:
                    f.write("1 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '7':
                with open(txt, 'a+') as f:
                    f.write("2 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            elif id_class == '8':
                with open(txt, 'a+') as f:
                    f.write("3 %s %s %s %s" % (x_center, y_center, w, h))
                    f.write('\n')
            f.close()
            print(id_class)


if __name__ == "__main__":
    main(sys.argv)
