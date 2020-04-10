import argparse
import os.path
from os import path
import sys
import numpy as np


def from_txt(path):
    with open('test.txt', 'a+') as f:
        for filename in os.listdir(folder):
            # print(filename)
            current_file = str(folder + filename)
            # print(current_file)
            f.write('%s\n' % current_file)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-filelist', default='/media/veec20/Data/duongdq/datasets/cocoapi/person_train2017_copy.txt',
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

    for line in lines:
        # line = line.replace('images','labels')
        # line = line.replace('img1','labels')
        # line = line.replace('JPEGImages', 'labels')

        line = line.replace('.jpg', '.txt')
        line = line.replace('.png', '.txt')
        line = line.replace('.jpeg', '.txt')
        line = line.replace('.JPG', '.txt')
        print(line)
        with open('valid_34_copy1.txt', 'a+') as gen:
            line = line.rstrip('\n')
            new = '/media/veec20/Data/duongdq/datasets/cocoapi/' + str(line)
            gen.write('%s\n' % new)
            print(new)


def from_file(folder):
    for filename in os.listdir(folder):
        current_file = str(folder + filename)
        if current_file.endswith('.jpg'):
            current_file_txt = str(current_file.replace(".jpg", "") + '.txt')
            if current_file.endswith('.jpg') and current_file_txt.endswith('.txt'):
                with open('test.txt', 'a+') as txt:
                    txt.write('%s\n' % current_file)
        elif current_file.endswith('.txt'):
            current_file_jpg = str(current_file.replace(".jpg", "") + '.txt')
            if current_file.endswith('.jpg') and current_file_jpg.endswith('.txt'):
                with open('test.txt', 'a+') as txt:
                    txt.write('%s\n' % current_file)
        else:
            os.remove(current_file)


if __name__ == "__main__":
    folder = '/media/veec20/Data/duongdq/datasets/src/test_copy/'
    # from_txt(folder)
    # main(sys.argv)
    from_file(folder)
