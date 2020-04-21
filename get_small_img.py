import os
import cv2
import random
import shutil


def change_coordination():
    os.chdir(directory)
    for filename in os.listdir(folder_original):
        if filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
            filename = filename.replace('.png', '.jpg')
            filename = filename.replace('.jpeg', '.jpg')
            filename = filename.replace('.JPG', '.jpg')
        img = cv2.imread(os.path.join(folder_original, filename))
        txt_file = filename.replace('.jpg', '.txt')
        if img is not None:
            height, width, chanel = img.shape
        else:
            continue
        f = open(os.path.join(folder_original, txt_file))
        if os.stat(folder_original + txt_file).st_size == 0:
            shutil.copy(os.path.join(folder_original, txt_file), directory)
            shutil.copy(os.path.join(folder_original, filename), directory)
            continue
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
        shutil.copy(os.path.join(folder_original, filename), directory)


def draw_new_img(folder_target):
    images = []
    crop_img = []
    dont_cut = 0

    for filename in os.listdir(folder_target):
        if filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
            filename = filename.replace('.png', '.jpg')
            filename = filename.replace('.jpeg', '.jpg')
            filename = filename.replace('.JPG', '.jpg')
        txt_file = filename.replace('.jpg', '.txt')
        img = cv2.imread(os.path.join(folder_target, filename))
        if img is not None:
            height, width, chanel = img.shape  # [height, width]
            print(img.shape)
            x_max_limit = width - 480
            y_max_limit = height - 270
            if height <= 600 or width <= 1000:
                dont_cut += 1
                print('Do not cut: %i' % dont_cut)
                print(filename)
                shutil.copy(os.path.join(directory, filename), directory_target)
                shutil.copy(os.path.join(folder_original, txt_file), directory_target)
                continue
            else:
                number = 5
                step = 20
                x_min_limit = 480
                y_min_limit = 270
            for index in range(1, number):
                x_center_random = random.randrange(x_min_limit, x_max_limit, step)
                y_center_random = random.randrange(y_min_limit, y_max_limit, step)
                # size of new image
                x_min_new_img = x_center_random - 480
                y_min_new_img = y_center_random - 270
                x_max_new_img = x_center_random + 480
                y_max_new_img = y_center_random + 270
                # show cut image on original image
                # cv2.rectangle(img, (x_min_new, y_min_new), (x_max_new, y_max_new), (0, 255, 0), 1)
                # cv2.circle(img, (x_center_random, y_center_random), 10, (255, 0, 0), 1)
                # cv2.imshow('new image in original image', img)

                crop = img[y_min_new_img:y_max_new_img, x_min_new_img:x_max_new_img]
                # cv2.imshow('new image', crop)
                # cv2.waitKey(0)
                save_file(crop, filename, x_min_new_img, y_min_new_img, x_max_new_img, y_max_new_img,
                          index, txt_file)
                images.append(img)
                crop_img.append(crop)


def save_file(crop, filename, x_min_new_img, y_min_new_img, x_max_new_img, y_max_new_img, index,
              txt_file):
    f = open(os.path.join(folder_target, txt_file))
    filename_new = filename.replace('.jpg', str(index) + '.jpg')
    txt_file_new = txt_file.replace('.txt', str(index) + '.txt')
    os.chdir(directory_target)
    for line in f.readlines():
        line = line.rstrip('\n')
        # size of original obj
        id_class, x_center_obj, y_center_obj, w_obj, h_obj = line.split(' ')[0:5]
        id_class, x_center_obj, y_center_obj, w_obj, h_obj = int(id_class), int(x_center_obj), int(y_center_obj), \
                                                             int(w_obj), int(h_obj)
        x_min_obj = int(x_center_obj - w_obj / 2)
        y_min_obj = int(y_center_obj - h_obj / 2)
        x_max_obj = int(x_center_obj + w_obj / 2)
        y_max_obj = int(y_center_obj + h_obj / 2)

        # show label of original obj
        # cv2.rectangle(img, (x_min_obj, y_min_obj), (x_max_obj, y_max_obj), (255, 0, 0), 1)
        # cv2.circle(img, (x_center_obj, y_center_obj), 10, (255, 0, 0), 1)
        # cv2.imshow('label on original image', img)
        # cv2.waitKey(0)

        # size of new object on new image
        if x_max_obj <= x_min_new_img:  # Outside left(
            x_center_obj_new = 0
            width_obj_new = 0
        elif x_min_obj <= x_min_new_img <= x_max_obj <= x_max_new_img:  # Inside left
            x_center_obj_new = int((x_max_obj - x_min_new_img) / 2)
            width_obj_new = x_max_obj - x_min_new_img
        elif x_min_new_img <= x_min_obj <= x_max_obj <= x_max_new_img:  # Inside
            x_center_obj_new = int((x_max_obj - x_min_obj) / 2 + x_min_obj - x_min_new_img)
            width_obj_new = x_max_obj - x_min_obj
        elif x_min_new_img <= x_min_obj <= x_max_new_img <= x_max_obj:  # Inside right
            x_center_obj_new = int((x_max_new_img - x_min_obj) / 2 + x_min_obj - x_min_new_img)
            width_obj_new = x_max_new_img - x_min_obj
        elif x_max_new_img <= x_min_obj:  # Outside right
            x_center_obj_new = 0
            width_obj_new = 0
        elif x_min_obj <= x_min_new_img <= x_max_new_img <= x_max_obj:  # obj cover new img
            x_center_obj_new = int((x_max_new_img - x_min_new_img) / 2)
            width_obj_new = x_max_new_img - x_min_new_img

        if y_max_obj <= y_min_new_img:  # Outside top
            y_center_obj_new = 0
            height_obj_new = 0
        elif y_min_obj <= y_min_new_img <= y_max_obj <= y_max_new_img:  # Inside top
            y_center_obj_new = int((y_max_obj - y_min_new_img) / 2)
            height_obj_new = y_max_obj - y_min_new_img
        elif y_min_new_img <= y_min_obj <= y_max_obj <= y_max_new_img:  # Inside
            y_center_obj_new = int((y_max_obj - y_min_obj) / 2 + y_min_obj - y_min_new_img)
            height_obj_new = y_max_obj - y_min_obj
        elif y_min_new_img <= y_min_obj <= y_max_new_img <= y_max_obj:  # Inside bottom
            y_center_obj_new = int((y_max_new_img - y_min_obj) / 2 + y_min_obj - y_min_new_img)
            height_obj_new = y_max_new_img - y_min_obj
        elif y_max_new_img <= y_min_obj:  # Outside bottom
            y_center_obj_new = 0
            height_obj_new = 0
        elif y_min_obj <= y_min_new_img <= y_max_new_img <= y_max_obj:  # obj cover new img 1
            y_center_obj_new = int((y_max_new_img - y_min_new_img) / 2)
            height_obj_new = y_max_new_img - y_min_new_img
        # if new object is too small
        if (width_obj_new < 50 and height_obj_new < 50) or width_obj_new * height_obj_new < (w_obj * h_obj * 0.1):
            print('remove size is too small')
            with open(txt_file_new, 'a+') as file_empty:
                file_empty.write('')
            cv2.imwrite(filename_new, crop)
            continue

        # show label of new
        x_min_obj_new = int(x_center_obj_new - width_obj_new / 2)
        y_min_obj_new = int(y_center_obj_new - height_obj_new / 2)
        x_max_obj_new = int(x_center_obj_new + width_obj_new / 2)
        y_max_obj_new = int(y_center_obj_new + height_obj_new / 2)
        # cv2.rectangle(crop, (x_min_obj_new, y_min_obj_new), (x_max_obj_new, y_max_obj_new), (255, 0, 0), 1)
        # cv2.circle(crop, (x_center_obj_new, y_center_obj_new), 5, (0, 255, 0), 1)
        # cv2.imshow('label on new image', crop)
        # cv2.waitKey(0)

        # transfer size to rate
        x_center_obj_new /= 960
        y_center_obj_new /= 540
        width_obj_new /= 960
        height_obj_new /= 540
        cv2.imwrite(filename_new, crop)
        with open(txt_file_new, 'a+') as file:
            file.write('%i %f %f %f %f\n' % (id_class, x_center_obj_new, y_center_obj_new, width_obj_new, height_obj_new))


if __name__ == '__main__':
    folder_original = '/media/veec20/Data/duongdq/Yolo_mark/data/SeaShips_7000_raw/'
    directory = '/media/veec20/Data/duongdq/Yolo_mark/data/change_cor/'
    folder_target = '/media/veec20/Data/duongdq/Yolo_mark/data/change_cor/'
    directory_target = '/media/veec20/Data/duongdq/Yolo_mark/data/test_cut/'
    # change_coordination()
    draw_new_img(folder_target)
