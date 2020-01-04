import matplotlib.image as mpimg
import os.path


if __name__ == "__main__":
    folder = '/home/tom/duong/darknet/data/seaships/1/'
    images = []
    for filename in os.listdir(folder):
        try:
            img = mpimg.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
                print('data/obj/' + filename)
        except:
            print('Cant import ' + filename, '\n')

