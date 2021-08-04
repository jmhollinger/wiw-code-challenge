import pytest
import pandas as pd
from csv_processor import csv_processor as csv_processor


# Set up test data in repo based on username and repo name.
def create_test_data():
    file_a = open("test_data/a.csv", "wt")

    contents_a = """drop,uid,path,minutes
1,1,/,3
0,2,/a,3
1,2,/a,3
0,4,/b,3
1,5,/c,3"""
    file_a.write(contents_a)

    file_c = open("test_data/c.csv", "wt")
    contents_c= """drop,uid,path,minutes
1,1,/,3
0,2,/a,3
1,2,/a,3
0,4,/b,3
1,5,/c,3"""
    file_c.write(contents_c)

    file_d = open("test_data/d.csv", "wt")
    contents_d = """col1,col2,col3,col4
1,2,3,4
1,2,3,4
1,2,3,4
1,2,3,4
1,2,3,4"""
    file_d.write(contents_d)

# Create test CSV files
create_test_data()

# Test create_file_list with default values
def test_create_file_list_default():
    assert len(csv_processor.create_file_list()) == 26
    
# Test create_file_list with supplied values
def test_create_file_list_supplied():
    assert len(csv_processor.create_file_list('https://google.com/',[1,2,3,4,5,6,7,8,9],"xls")) == 9

# Test create_data_frame with all 404 errors
def test_create_data_frame_all_404():
    files = csv_processor.create_file_list('test_data/',[1,2,3,4,5,6,7,8,9],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[0] == 0

# Test create_data_frame with mix of 404 errors and inconsistent data
def test_create_data_frame_mix_1():
    files = csv_processor.create_file_list("test_data/",["a","b","c","d"],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[0] == 10

# Test create_data_frame with mix of 404 errors and inconsistent data
def test_create_data_frame_mix_2():
    files = csv_processor.create_file_list("test_data/",["a","b","c","d"],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[1] == 4

# Test create_data_frame with all successful files
def test_create_data_frame_all_success_1():
    files = csv_processor.create_file_list("test_data/",["a","c"],"csv")
    df = csv_processor.create_data_frame(files)
    assert df.shape[1] == 4

# Test create_data_frame with all successful files
def test_create_data_frame_all_success_2():
    files = csv_processor.create_file_list("test_data/",["a","c"],"csv")
    df = csv_processor.create_data_frame(files)
    assert df.shape[0] == 10

# Test if pivot_table returns correct rows and columns.
def test_pivot_1():
    files = csv_processor.create_file_list("test_data/",["a","b","c","d"],"csv")
    data = csv_processor.create_data_frame(files)
    pivoted_dataframe = data.pivot_table(index="uid", columns="path", values="minutes", aggfunc="sum")
    assert pivoted_dataframe.shape[0] == 4

# Test if pivot_table returns correct rows and columns.
def test_pivot_2():
    files = csv_processor.create_file_list("test_data/",["a","b","c","d"],"csv")
    data = csv_processor.create_data_frame(files)
    pivoted_dataframe = data.pivot_table(index="uid", columns="path", values="minutes", aggfunc="sum")
    assert pivoted_dataframe.shape[1] == 4

# Test if pivot_table returns correct value.
def test_pivot_3():
    files = csv_processor.create_file_list("test_data/",["a","b","c","d"],"csv")
    data = csv_processor.create_data_frame(files)
    pivoted_dataframe = data.pivot_table(index="uid", columns="path", values="minutes", aggfunc="sum")
    assert pivoted_dataframe.at[2,'/a'] == 12