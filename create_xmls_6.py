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
ALL_NEEDED_PATHS_TEST = 'all_needed_paths_test.csv'
ALL_NEEDED_PATHS_TRAIN = 'all_needed_paths_train.csv'


def add_to_dict(dictionary: dict, dataframe: pd.DataFrame) -> dict:
    for _, row in dataframe.iterrows():
        dictionary.setdefault(row['image_name'], []).append([row['image_path'], row['object'], row['image_width'],
                                                             row['image_height'], row['image_depth'],
                                                             row['xmin'], row['ymin'], row['xmax'], row['ymax'],
                                                             row['image_name']])

    return dictionary


def write_xmls(df: pd.DataFrame, folder_path: str, all_needed_path: str) -> None:
    df_weapons = df[df['object'] == 'weapon']
    lst_weapons = df_weapons['image_name'].tolist()
    needed_lst = set(lst_weapons)
    df_person = pd.DataFrame({'path': [], 'object': [], 'object_mark': [], 'image_name': [], 'image_path': [],
                              'image_width': [], 'image_height': [], 'image_depth': [],
                              'xmin': [], 'ymin': [], 'xmax': [], 'ymax': []})
    for i, row in df.iterrows():
        if row['image_name'] in needed_lst and row['object'] == 'person':
            df_person.loc[len(df_person)] = [row['path'], row['object'], row['object_mark'], row['image_name'],
                                             row['image_path'], row['image_width'], row['image_height'],
                                             row['image_depth'],
                                             row['xmin'], row['ymin'], row['xmax'], row['ymax']]

    dict_ = dict()
    dict_ = add_to_dict(dict_, df_weapons)
    dict_ = add_to_dict(dict_, df_person)
    for key in dict_.keys():
        writer = Writer(dict_[key][0][0], dict_[key][0][2], dict_[key][0][3])
        for item in dict_[key]:
            writer.addObject(item[1], item[5], item[6], item[7], item[8])
        writer.save(folder_path + dict_[key][0][-1].split('.')[0] + '.xml')
    lst = df_weapons['image_path'].tolist()
    needed_lst = list(set(lst))
    path_df = pd.DataFrame({'path': needed_lst})
    path_df.to_csv(DOWNLOADS_PATH + all_needed_path, index=False)


if __name__ == "__main__":

    if not os.path.isdir(TEST_XML_FOLDER):
        os.mkdir(TEST_XML_FOLDER)

    if not os.path.isdir(TRAIN_XML_FOLDER):
        os.mkdir(TRAIN_XML_FOLDER)

    df_test = pd.read_csv(DOWNLOADS_PATH + TEST_PRETRAINED)
    df_train = pd.read_csv(DOWNLOADS_PATH + TRAIN_PRETRAINED)

    write_xmls(df_test, TEST_XML_FOLDER, ALL_NEEDED_PATHS_TEST)
    write_xmls(df_train, TRAIN_XML_FOLDER, ALL_NEEDED_PATHS_TRAIN)
