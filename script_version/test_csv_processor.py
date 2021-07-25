import pytest
import csv_processor as csv_processor

# Test create_file_list with default values
def test_create_file_list_1():
    assert len(csv_processor.create_file_list()) == 26
    
# Test create_file_list with supplied values
def test_create_file_list_2():
    assert len(csv_processor.create_file_list('https://google.com/',[1,2,3,4,5,6,7,8,9],"xls")) == 9