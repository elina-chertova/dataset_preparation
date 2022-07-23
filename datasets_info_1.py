import os
import pandas as pd

TRAIN_PATH = '/Users/elinachertova/Downloads/miem_train'
TEST_PATH = '/Users/elinachertova/Downloads/miem_test'
DOWNLOADS_PATH = '/Users/elinachertova/Downloads/'
TRAIN_FILES = os.listdir(TRAIN_PATH)
TEST_FILES = os.listdir(TEST_PATH)


def create_lists_txt_jpg(list_list_jpg: list, list_list_txt: list, files_from_directory: list, path: str) -> [list,
                                                                                                              list]:
    for file in files_from_directory:
        jpg_files = []
        txt_files = []
        if file != '.DS_Store':
            directory = os.listdir(path + '/' + file + '/obj_train_data')
            for name in directory:
                if name.endswith('jpg'):
                    jpg_files.append(file + '/obj_train_data/' + name)
                elif name.endswith('txt'):
                    txt_files.append(file + '/obj_train_data/' + name)

            list_list_jpg.append(jpg_files)
            list_list_txt.append(txt_files)

    return list_list_jpg, list_list_txt


def create_df(jpg: list, txt: list, path: str) -> pd.DataFrame:
    df = pd.DataFrame(
        {'directory': [], 'path': [], 'path_without_expansion': [], 'common_name': [],
         'name': [], 'expansion': [], 'size': []})
    new_list = jpg + txt
    print(new_list)
    for point in new_list:
        for i in point:
            directory = i.split('/')[0]
            name = i.split('.')[0]
            common_name = name.split('/')[-1].split('_')[0] + '_' + name.split('/')[-1].split('_')[1]

            df = df.append({'directory': directory, 'path': i,
                            'path_without_expansion': name.split('/')[0] + '/' + name.split('/')[1] + '/' + common_name,
                            'common_name': common_name, 'name': i.split('/')[-1], 'expansion': i.split('.')[-1],
                            'size': os.path.getsize(path + '/' + i)}, ignore_index=True)

    return df


if __name__ == "__main__":
    jpg_list = []
    txt_list = []
    jpg_test, txt_test = create_lists_txt_jpg(jpg_list, txt_list, TEST_FILES, TEST_PATH)
    jpg_train, txt_train = create_lists_txt_jpg(jpg_list, txt_list, TRAIN_FILES, TRAIN_PATH)

    data_test = create_df(jpg_test, txt_test, TEST_PATH)
    sorted_df_test = data_test.sort_values(by=['directory', 'name', 'common_name'])

    data_train = create_df(jpg_train, txt_train, TRAIN_PATH)
    sorted_df_train = data_train.sort_values(by=['directory', 'name', 'common_name'])

    sorted_df_test.to_csv(DOWNLOADS_PATH + 'test_df.csv', index=False)
    sorted_df_train.to_csv(DOWNLOADS_PATH + 'train_df.csv', index=False)
