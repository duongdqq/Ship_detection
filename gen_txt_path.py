import csv
import itertools
import xml.etree.ElementTree as ET
import os.path

if __name__ == "__main__":
    folder = '/media/veec20/Data/duongdq/datasets/data_change_id/person_train2017/'
    with open('person_train2017.txt', 'a+') as f:
        for filename in os.listdir(folder):
            # print(filename)
            current_file = str(folder + filename)
            # print(current_file)
            f.write('%s' % current_file)
            f.write('\n')