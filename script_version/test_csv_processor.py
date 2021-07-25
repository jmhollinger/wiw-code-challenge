import pytest
import csv_processor as csv_processor

# Test Default values
def test_create_file_list_1():
    print('Testing deafault values for create_file_list()')
    assert len(csv_processor.create_file_list()) == 26
    
# Test supplied values
def test_create_file_list_2():
    print('Testing supplied values for create_file_list()')
    assert len(csv_processor.create_file_list('https://google.com/',[1,2,3,4,5,6,7,8,9],"xls")) == 9