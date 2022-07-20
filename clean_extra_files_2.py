# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()


import pandas as pd
from collections import Counter


DOWNLOADS_PATH = '/Users/elinachertova/Downloads/'
TEST_DF = DOWNLOADS_PATH + 'test_df.csv'
TRAIN_DF = DOWNLOADS_PATH + 'train_df.csv'
TEST_DF_FINAL = 'test_df_final.csv'
TRAIN_DF_FINAL = 'train_df_final.csv'
TEST_DF_PREFINAL = 'test_df_prefinal.csv'
TRAIN_DF_PREFINAL = 'train_df_prefinal.csv'

k = 1


def prepare_dataframe(path: str, future_path_cleared: str, future_path_count: str, cnt: int) -> int:
    df = pd.read_csv(path)
    all_names_df = df['path_without_expansion'].tolist()
    counter_all_names_df = Counter(all_names_df)
    count_df = [counter_all_names_df[item] for item in all_names_df]
    mark = [1 if i == 'jpg' else 0 for i in df['expansion'].tolist()]
    df['mark'] = mark
    df['count'] = count_df
    df = df[df['count'] != 1]
    path_set = df.groupby('path_without_expansion')['path_without_expansion'].first().tolist()
    count_jpg = df.groupby('path_without_expansion')['mark'].sum()
    mupltiplier = df.groupby('path_without_expansion').count()['count']
    dict_ = {path_set[i]: (count_jpg.values[i], mupltiplier.values[i]) for i in range(len(path_set))}
    # словарь с values (наличие jpg для конкретной разметки, количество элементов для объекта (jpg + txts)
    n_times = [[i] * j for i, j in dict_.values()]
    final_list = [j for i in n_times for j in i]
    df['mark_to_delete'] = final_list
    final_names = []
    # cnt = 1
    for i in n_times:
        for _ in i:
            final_names.append(cnt)
        cnt += 1
    df['final_names'] = final_names
    df.to_csv(DOWNLOADS_PATH + future_path_count, index=False)
    df = df[df['mark_to_delete'] != 0]
    df.to_csv(DOWNLOADS_PATH + future_path_cleared, index=False)
    return cnt

cnt = prepare_dataframe(TEST_DF, TEST_DF_FINAL, TEST_DF_PREFINAL, k)
_ = prepare_dataframe(TRAIN_DF, TRAIN_DF_FINAL, TRAIN_DF_PREFINAL, cnt)


