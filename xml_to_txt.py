import csv
import itertools
import xml.etree.ElementTree as ET
import os.path


def change_xml_to_txt():
    tree = ET.parse(current_file)
    root = tree.getroot()
    width = int(root[4][0].text)
    height = int(root[4][1].text)
    i = len(root)
    for i in range(6, i):
        with open(current_file.replace(".xml", "") + ".txt", 'a+') as f:
            f.write('0 ')
        for elem in root[i][3]:
            # print(elem.tag)
            if elem.tag == 'xmin':
                xmin = int(elem.text)
            elif elem.tag == 'ymin':
                ymin = int(elem.text)
            elif elem.tag == 'xmax':
                xmax = int(elem.text)
            elif elem.tag == 'ymax':
                ymax = int(elem.text)
        x_center = round((xmax + xmin)/(2 * width), 6)
        y_center = round((ymax + ymin)/(2 * height), 6)
        width_box = round((xmax - xmin)/width, 6)
        height_box = round((ymax - ymin)/height, 6)
        object = [x_center, y_center, width_box, height_box]
        for item in object:
            with open(current_file.replace(".xml", "") + ".txt", 'a+') as f:
                f.write('%s ' % item)
        with open(current_file.replace(".xml", "") + ".txt", 'a+') as f:
            f.write('\n')


if __name__ == "__main__":
    folder = '/media/veec20/Data/duongdq/Yolo_mark/data/SeaShips'
    for filename in os.listdir(folder):
        # print(filename)
        current_file = str(folder + filename)
        # print(current_file)
        change_xml_to_txt()
