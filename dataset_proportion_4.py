import pandas as pd

DOWNLOADS_PATH = '/Users/elinachertova/Downloads/'
TEST_PRETRAINED = 'test_pretrained.csv'
TRAIN_PRETRAINED = 'train_pretrained.csv'

df = pd.read_csv(DOWNLOADS_PATH + TEST_PRETRAINED)
print('test "person"', df[df['object'] == 'person'].shape[0])
print('test "weapon"', df[df['object'] == 'weapon'].shape[0])
print('test summary', df.shape, '\n')

df = pd.read_csv(DOWNLOADS_PATH + TRAIN_PRETRAINED)
print('train "person"', df[df['object'] == 'person'].shape[0])
print('train "weapon"', df[df['object'] == 'weapon'].shape[0])
print('train summary', df.shape)
