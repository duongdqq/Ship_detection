import xml.etree.ElementTree as ET
import os.path


def change_type(current_file):
    tree = ET.parse(current_file)
    root = tree.getroot()
    width = int(root[4][0].text)
    height = int(root[4][1].text)
    for elem in root[6][4]:
        print(elem.tag)
        if elem.tag == 'xmin':
            x = int(elem.text)
            new = round(x / width, 6)
        elif elem.tag == 'ymin':
            x = int(elem.text)
            new = round(x / height, 6)
        elif elem.tag == 'xmax':
            x = int(elem.text)
            new = round(x / width, 6)
        elif elem.tag == 'ymax':
            x = int(elem.text)
            new = round(x / height, 6)
        print(new)
        with open(current_file.replace(".xml","")+".txt", 'a') as f:
            f.write('0 ' + "%s " % new)
        f.close()


if __name__ == "__main__":
    folder = '/home/pcu/duong/darknet/xml/'
    for filename in os.listdir(folder):
        # print(filename)
        current_file = str(folder + filename)
        print(current_file)
        change_type(current_file)