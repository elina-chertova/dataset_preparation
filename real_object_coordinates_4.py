import cv2
import os
import pandas as pd
import re

TEST_FOLDER = '/test_new/'
TRAIN_FOLDER = '/train_new/'
TEST_XML_FOLDER = '/annotations_test/'
TRAIN_XML_FOLDER = '/annotations_train/'

DOWNLOADS_PATH = '/Downloads/'
TEST_PRETRAINED = 'test_pretrained.csv'
TRAIN_PRETRAINED = 'train_pretrained.csv'


def generate_true_coordinates(folder: str, dataset_name: str) -> None:
    df = pd.DataFrame({'path': [], 'object': [], 'object_mark': [], 'image_name': [], 'image_path': [],
                       'image_width': [], 'image_height': [], 'image_depth': [],
                       'xmin': [], 'ymin': [], 'xmax': [], 'ymax': []})

    list_txt = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(".txt")]
    list_txt.sort(key=lambda file_: int(re.sub('\D', '', file_)))
    print(list_txt)
    k = 0

    for txt in list_txt:
        img = cv2.imread(txt[:-8] + '.jpg') if txt.endswith('_iss.txt') else cv2.imread(txt[:-4] + '.jpg')
        h, w, d = img.shape
        with open(txt, 'r') as f:
            temp = f.read().split()
        image_path = txt[:-8] + '.jpg' if txt.endswith('_iss.txt') else txt[:-4] + '.jpg'
        image_name = txt.split('/')[-1][:-8] + '.jpg' if txt.endswith('_iss.txt') else txt.split('/')[-1][:-4] + '.jpg'

        for i in range(0, len(temp), 5):
            x_, y_, w_, h_ = eval(temp[i + 1]), eval(temp[i + 2]), eval(temp[i + 3]), eval(temp[i + 4])
            x1 = w * x_ - 0.5 * w * w_
            x2 = w * x_ + 0.5 * w * w_
            y1 = h * y_ - 0.5 * h * h_
            y2 = h * y_ + 0.5 * h * h_
            x_1, y_1, x_2, y_2 = int(x1), int(y1), int(x2), int(y2)
            object_, mark = ('person', 1) if txt.endswith('_iss.txt') else ('weapon', 0)

            df.loc[k] = [txt, object_, mark, image_name, image_path, w, h, d, x_1, y_1, x_2, y_2]
            k += 1

    df.to_csv(DOWNLOADS_PATH + dataset_name, index=False)


if __name__ == "__main__":
    generate_true_coordinates(TEST_FOLDER, TEST_PRETRAINED)
    generate_true_coordinates(TRAIN_FOLDER, TRAIN_PRETRAINED)
