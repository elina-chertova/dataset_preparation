from pascal_voc_writer import Writer
import pandas as pd
import os

TEST_FOLDER = '/Users/elinachertova/Downloads/test/'
TRAIN_FOLDER = '/Users/elinachertova/Downloads/train/'

DOWNLOADS_PATH = '/Users/elinachertova/Downloads/'
TEST_PRETRAINED = 'test_pretrained.csv'
TRAIN_PRETRAINED = 'train_pretrained.csv'
TEST_XML_FOLDER = '/Users/elinachertova/Downloads/annotations_test/'
TRAIN_XML_FOLDER = '/Users/elinachertova/Downloads/annotations_train/'


if not os.path.isdir(TEST_XML_FOLDER):
    os.mkdir(TEST_XML_FOLDER)

if not os.path.isdir(TRAIN_XML_FOLDER):
    os.mkdir(TRAIN_XML_FOLDER)

df_test = pd.read_csv(DOWNLOADS_PATH + TEST_PRETRAINED)

df_train = pd.read_csv(DOWNLOADS_PATH + TRAIN_PRETRAINED)


def add_to_dict(dictionary: dict, dataframe: pd.DataFrame) -> dict:
    for i, row in dataframe.iterrows():
        if row['image_name'] in dictionary:
            dictionary[row['image_name']].append([row['image_path'], row['object'], row['image_width'],
                                                  row['image_height'], row['image_depth'], row['xmin'],
                                                  row['ymin'], row['xmax'], row['ymax'], row['image_name']])
        else:
            dictionary[row['image_name']] = [[row['image_path'], row['object'], row['image_width'],
                                              row['image_height'], row['image_depth'],
                                              row['xmin'], row['ymin'], row['xmax'], row['ymax'], row['image_name']]]
    return dictionary


def write_xmls(df: pd.DataFrame, folder_path: str) -> None:
    df_weapons = df[df['object'] == 'weapon']
    df_person = df[df['object'] == 'person'].sample(n=df_weapons.shape[0]).sort_index(axis=0)
    dict_ = dict()
    dict_ = add_to_dict(dict_, df_weapons)
    dict_ = add_to_dict(dict_, df_person)
    print(dict_)
    for key in dict_.keys():
        writer = Writer(dict_[key][0][0], dict_[key][0][2], dict_[key][0][3])
        for item in dict_[key]:
            writer.addObject(item[1], item[5], item[6], item[7], item[8])
        writer.save(folder_path + dict_[key][0][-1].split('.')[0] + '.xml')


write_xmls(df_test, TEST_XML_FOLDER)
write_xmls(df_train, TRAIN_XML_FOLDER)

# # Writer(path, width, height)
#
# writer = Writer(TEST_PATH_JPG, 800, 400)
#
# writer.addObject('cat', 100, 100, 200, 200)
# writer.addObject('dog', 200, 200, 400, 400)
# # ::save(path)
# writer.save(DOWNLOADS_PATH + 'img.xml')

# writer = Writer(image_path, w, h)
# writer.addObject(object_, x_1, y_1, x_2, y_2)
# writer.save(annotations_path + '{}.xml'.format(image_name.split('.')[0]))
