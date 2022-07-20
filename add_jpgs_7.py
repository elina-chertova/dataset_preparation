import os
import pandas as pd

DOWNLOADS_PATH = '/Users/elinachertova/Downloads/'
TEST_FOLDER = DOWNLOADS_PATH + 'test/'
TRAIN_FOLDER = DOWNLOADS_PATH + 'train/'
TEST_JPG_FOLDER = DOWNLOADS_PATH + 'jpg_test/'
TRAIN_JPG_FOLDER = DOWNLOADS_PATH + 'jpg_train/'
ALL_NEEDED_PATHS_TEST = 'all_needed_paths_test.csv'
ALL_NEEDED_PATHS_TRAIN = 'all_needed_paths_train.csv'


def move_jpg(dataframe: pd.DataFrame, future_folder: str) -> None:
    paths = dataframe['path'].tolist()
    for i in range(len(paths)):
        os.rename(paths[i], future_folder + paths[i].split('/')[-1])


if __name__ == "__main__":

    if not os.path.isdir(TEST_JPG_FOLDER):
        os.mkdir(TEST_JPG_FOLDER)
    if not os.path.isdir(TRAIN_JPG_FOLDER):
        os.mkdir(TRAIN_JPG_FOLDER)

    df_test = pd.read_csv(DOWNLOADS_PATH + ALL_NEEDED_PATHS_TEST)
    df_train = pd.read_csv(DOWNLOADS_PATH + ALL_NEEDED_PATHS_TRAIN)

    move_jpg(df_test, TEST_JPG_FOLDER)
    move_jpg(df_train, TRAIN_JPG_FOLDER)
