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
    parser.add_argument('-filelist', default='/media/veec20/Data/duongdq/darknet/data/train_new.txt',
                        help='path to filelist\n')
    parser.add_argument('-output_dir', default='/media/veec20/Data/duongdq/darknet', type=str,
                        help='Output anchor directory\n')
    parser.add_argument('-num_clusters', default=0, type=int,
                        help='number of clusters\n')

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    f = open(args.filelist)

    lines = [line.rstrip('\n') for line in f.readlines()]

    annotation_dims = []
    with open('combine_train_new.txt', 'w') as outfile:
        for line in lines:
            line = line.replace('.jpg', '.txt')
            line = line.replace('.png', '.txt')
            line = line.replace('.jpeg', '.txt')
            line = line.replace('.JPG', '.txt')
            print(line)
            f2 = open(line)
            with open(line) as infile:
                outfile.write(infile.read())
                for line in f2.readlines():

                    line = line.rstrip('\n')


if __name__ == "__main__":
    main(sys.argv)
