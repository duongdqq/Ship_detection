import shutil
from darknet import performDetect
import os
import matplotlib.image as mpimg
from skimage import io, draw
import numpy as np


def create_subset(folder_name):
    #  Copy all images of given category to new folder
    # os.mkdir(folder_name)
    images = []
    index_image = 0
    for filename in os.listdir(folder):
        current_file = str(folder + filename)
        if filename.endswith('.txt'):
            continue
        try:
            index_image += 1
            img = mpimg.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
                print(index_image, '---', filename)
        except:
            print('Cant import ' + filename)
        image = io.imread(folder+filename)
        if image.shape[1] < image.shape[0]:
            # shutil.copy(os.path.join('/media/veec20/Data/duongdq/darknet/data/S1/', filename), folder_name)
            os.remove(current_file)
            txt_remainder = str(current_file.replace(".jpg", "") + '.txt')
            if str(current_file.replace(".jpg", "")+'.txt'):
                os.remove(txt_remainder)
            print('Done creating data subset with images....')


if __name__ == "__main__":
    folder = '/media/veec20/Data/duongdq/darknet/data/horizontal_SeaShips/'
    create_subset(folder_name='horizontal')



