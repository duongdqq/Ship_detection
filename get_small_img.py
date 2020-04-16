import os
import cv2
import random
import shutil


def change_coordination():
    folder = '/media/veec20/Data/duongdq/Yolo_mark/data/test/'
    directory = '/media/veec20/Data/duongdq/Yolo_mark/data/change_cor/'
    os.chdir(directory)
    for filename in os.listdir(folder):
        if filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
            filename.replace('.png', '.jpg')
            filename.replace('.jpeg', '.jpg')
            filename.replace('.JPG', '.jpg')
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            height, width, chanel = img.shape
        else:
            continue
        txt_file = filename.replace('.jpg', '.txt')
        f = open(os.path.join(folder, txt_file))
        for line in f.readlines():
            line = line.rstrip('\n')
            # size of original obj
            id_class, x_center, y_center, w, h = line.split(' ')[0:5]
            id_class, x_center, y_center, w, h = int(id_class), float(x_center), float(y_center), float(w), float(h)
            x_center = int(x_center * width)
            y_center = int(y_center * height)
            w = int(w * width)
            h = int(h * height)
            with open(txt_file, 'a+') as f:
                f.write('%i %i %i %i %i\n' % (id_class, x_center, y_center, w, h))
        shutil.copy(os.path.join(folder, filename), directory)


def draw_new_img(folder):
    directory = '/media/veec20/Data/duongdq/Yolo_mark/data/test_new/'
    images = []
    crop_img = []
    dont_cut = 0
    for filename in os.listdir(folder):
        if filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
            filename.replace('.png', '.jpg')
            filename.replace('.jpeg', '.jpg')
            filename.replace('.JPG', '.jpg')
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img_shape = img.shape  # [height, width]
            print(img_shape)
            height, width, chanel = img.shape
            x_max_limit = width - 320
            y_max_limit = height - 180
            if x_max_limit < 400 or y_max_limit < 300:
                dont_cut += 1
                print('Do not cut: %i' % dont_cut)
                print(filename)
                continue
            for index in range(1, 5):
                x_center_random = random.randrange(320, x_max_limit, 25)
                y_center_random = random.randrange(180, y_max_limit, 25)
                # size of new image
                x_min_new_img = x_center_random - 320
                y_min_new_img = y_center_random - 180
                x_max_new_img = x_center_random + 320
                y_max_new_img = y_center_random + 180
                # cv2.rectangle(img, (x_min_new, y_min_new), (x_max_new, y_max_new), (0, 255, 0), 1)
                # cv2.circle(img, (x_center_random, y_center_random), 10, (255, 0, 0), 1)
                # cv2.imshow('new image in original image', img)
                crop = img[y_min_new_img:y_max_new_img, x_min_new_img:x_max_new_img]
                # cv2.imshow('Draw new image', crop)
                # cv2.waitKey(0)
                save_file(directory, crop, img, filename, x_min_new_img, y_min_new_img, x_max_new_img, y_max_new_img,
                          index)
                images.append(img)
                crop_img.append(crop)
        else:
            continue


def save_file(directory, crop, img, filename, x_min_new_img, y_min_new_img, x_max_new_img, y_max_new_img, index):
    txt_file = filename.replace('.jpg', '.txt')
    f = open(os.path.join(folder, txt_file))
    for line in f.readlines():
        line = line.rstrip('\n')
        # size of original obj
        id_class, x_center_obj, y_center_obj, w_obj, h_obj = line.split(' ')[0:5]
        id_class, x_center_obj, y_center_obj, w_obj, h_obj = int(id_class), int(x_center_obj), int(y_center_obj), \
                                                             int(w_obj), int(h_obj)
        x_min_obj = int(x_center_obj - w_obj / 2)
        y_min_obj = y_center_obj - 180
        x_max_obj = int(x_center_obj + w_obj / 2)
        y_max_obj = y_center_obj + 180
        # Draw coordination of original obj
        cv2.rectangle(img, (x_min_obj, y_min_obj), (x_max_obj, y_max_obj), (255, 0, 0), 1)
        cv2.circle(img, (x_center_obj, y_center_obj), 10, (255, 0, 0), 1)
        # cv2.imshow('Draw label of original obj', img)
        # cv2.waitKey(0)

        # size of new object ( compared to new image)
        if x_max_obj <= x_min_new_img:  # Outside left
            x_center_obj_new = 0
            width_obj_new = 0
        elif x_min_obj < x_min_new_img < x_max_obj < x_max_new_img:  # Inside left
            x_center_obj_new = int((x_max_obj - x_min_new_img) / 2)
            width_obj_new = x_max_obj - x_min_new_img
        elif x_min_new_img < x_min_obj < x_max_obj < x_max_new_img:  # Inside
            x_center_obj_new = int((x_max_obj - x_min_obj) / 2 + x_min_obj - x_min_new_img)
            width_obj_new = x_max_obj - x_min_obj
        elif x_min_new_img < x_min_obj < x_max_new_img < x_max_obj:  # Inside right
            x_center_obj_new = int((x_max_new_img - x_min_obj) / 2 + x_min_obj - x_min_new_img)
            width_obj_new = x_max_new_img - x_min_obj
        elif x_max_new_img <= x_min_obj:  # Outside right
            x_center_obj_new = 0
            width_obj_new = 0
        elif x_min_obj < x_min_new_img < x_max_new_img < x_max_obj:  # obj cover new img
            x_center_obj_new = int((x_max_new_img - x_min_new_img) / 2)
            width_obj_new = x_max_new_img - x_min_new_img
        else:
            print('error x')

        if y_max_obj <= y_min_new_img:  # Outside top
            y_center_obj_new = 0
            height_obj_new = 0
        elif y_min_obj < y_min_new_img < y_max_obj < y_max_new_img:  # Inside top
            y_center_obj_new = int((y_max_obj - y_min_new_img) / 2)
            height_obj_new = y_max_obj - y_min_new_img
        elif y_min_new_img < y_min_obj < y_max_obj < y_max_new_img:  # Inside
            y_center_obj_new = int((y_max_obj - y_min_obj) / 2 + x_min_obj - x_min_new_img)
            height_obj_new = y_max_obj - y_min_obj
        elif y_min_new_img < y_min_obj < y_max_new_img < y_max_obj:  # Inside bottom
            y_center_obj_new = int((y_max_new_img - y_min_obj) / 2 + y_min_obj - y_min_new_img)
            height_obj_new = y_max_new_img - y_min_obj
        elif y_max_new_img <= y_min_obj:  # Outside bottom
            y_center_obj_new = 0
            height_obj_new = 0
        elif y_min_obj < y_min_new_img < y_max_new_img < y_max_obj:  # obj cover new img
            y_center_obj_new = int((y_max_new_img - y_min_new_img) / 2)
            height_obj_new = y_max_new_img - y_min_new_img
        else:
            print('error y')

        # if new object is too small
        if (width_obj_new * height_obj_new) < 100:
            continue
        cv2.circle(crop, (x_center_obj_new, y_center_obj_new), 5, (0, 255, 0), 1)
        # cv2.imshow('Draw label of new obj', crop)
        # cv2.waitKey(0)
        # transfer size to rate
        x_center_obj_new /= 640
        y_center_obj_new /= 360
        width_obj_new /= 640
        height_obj_new /= 360
        # save
        filename_new = filename.replace('.jpg', str(index) + '.jpg')
        txt_file_new = txt_file.replace('.txt', str(index) + '.txt')
        os.chdir(directory)
        cv2.imwrite(filename_new, crop)
        with open(txt_file_new, 'a+') as f:
            f.write('%i %f %f %f %f\n' % (id_class, x_center_obj_new, y_center_obj_new, width_obj_new, height_obj_new))


if __name__ == '__main__':
    folder = '/media/veec20/Data/duongdq/Yolo_mark/data/change_cor/'
    # change_coordination()
    draw_new_img(folder)
