from pathlib import Path


TEST_JPG_FOLDER = '/Users/elinachertova/Downloads/jpg_test/'
TRAIN_JPG_FOLDER = '/Users/elinachertova/Downloads/jpg_train/'

TEST_XML_FOLDER = '/Users/elinachertova/Downloads/annotations_test/'
TRAIN_XML_FOLDER = '/Users/elinachertova/Downloads/annotations_train/'


test_jpg = sorted(Path(TEST_JPG_FOLDER).glob('*.jpg'))

test_xml = sorted(Path(TEST_XML_FOLDER).glob('*.xml'))

train_jpg = sorted(Path(TRAIN_JPG_FOLDER).glob('*.jpg'))

train_xml = sorted(Path(TRAIN_XML_FOLDER).glob('*.xml'))


print('test_jpg == test_xml', len(test_xml) == len(test_jpg), len(test_xml), len(test_jpg))
print('train_jpg == train_xml', len(train_xml) == len(train_jpg), len(train_xml), len(train_jpg))
