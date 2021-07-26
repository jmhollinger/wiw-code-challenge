#from script_version.csv_processor import create_data_frame, create_file_list
import pytest
import csv_processor as csv_processor

# Test create_file_list with default values
def test_create_file_list_default():
    assert len(csv_processor.create_file_list()) == 26
    
# Test create_file_list with supplied values
def test_create_file_list_supplied():
    assert len(csv_processor.create_file_list('https://google.com/',[1,2,3,4,5,6,7,8,9],"xls")) == 9

# Test create_data_frame with all 404 errors
def test_create_data_frame_all_404():
    files = csv_processor.create_file_list('https://test.com/',[1,2,3,4,5,6,7,8,9],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[0] == 0
    assert df.shape[1] == 0

# Test create_data_frame with mix of 404 errors and inconsistent data
def test_create_data_frame_mix():
    files = csv_processor.create_file_list('https://google.com/',[1,2,3,4,5,6,7,8,9],"xls")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[0] == 0
    assert df.shape[1] == 0

# Test create_data_frame with all successful files
def test_create_data_frame_all_success():
    files = csv_processor.create_file_list()
    df = csv_processor.create_data_frame(files)
    assert df.shape[0] == 39052
    assert df.shape[1] == 5
