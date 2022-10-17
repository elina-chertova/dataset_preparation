import os
import pandas as pd

DOWNLOADS_PATH = '/Downloads/'
TEST_DF_FINAL = DOWNLOADS_PATH + 'test_df_final.csv'
TRAIN_DF_FINAL = DOWNLOADS_PATH + 'train_df_final.csv'
TEST_FOLDER = 'test_new/'
TRAIN_FOLDER = 'train_new/'
TRAIN_PATH = 'train/'
TEST_PATH = 'test/'

if not os.path.isdir(TEST_FOLDER):
    os.mkdir(TEST_FOLDER)

if not os.path.isdir(TRAIN_FOLDER):
    os.mkdir(TRAIN_FOLDER)


def move_files_to_common_folders(df_final: str, path: str, future_folder: str) -> None:

    df = pd.read_csv(df_final)
    list_files_to_move = df['path'].to_list()
    future_names = df['final_names'].to_list()
    for i, file in enumerate(list_files_to_move):
        var = file.split('/')[-1]
        end = '_iss.txt' if var.endswith('_iss.txt') else '.' + var.split('.')[-1]
        os.rename(path + file, future_folder + str(future_names[i]) + end)


if __name__ == "__main__":
    move_files_to_common_folders(TEST_DF_FINAL, TEST_PATH, TEST_FOLDER)
    move_files_to_common_folders(TRAIN_DF_FINAL, TRAIN_PATH, TRAIN_FOLDER)
