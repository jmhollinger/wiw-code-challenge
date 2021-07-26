import pytest
import pandas as pd
import csv_processor as csv_processor

# Set up test data in repo based on username and repo name.
github_username = "jmhollinger"
github_repo_name = "wiw-code-challenge"

# Test create_file_list with default values
def test_create_file_list_default():
    assert len(csv_processor.create_file_list()) == 26
    
# Test create_file_list with supplied values
def test_create_file_list_supplied():
    assert len(csv_processor.create_file_list('https://google.com/',[1,2,3,4,5,6,7,8,9],"xls")) == 9

# Test create_data_frame with all 404 errors
def test_create_data_frame_all_404():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',[1,2,3,4,5,6,7,8,9],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[0] == 0

# Test create_data_frame with mix of 404 errors and inconsistent data
def test_create_data_frame_mix_1():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","b","c","d"],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[0] == 10

# Test create_data_frame with mix of 404 errors and inconsistent data
def test_create_data_frame_mix_2():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","b","c","d"],"csv")
    df = csv_processor.create_data_frame(files)
    print(df.shape)
    assert df.shape[1] == 4

# Test create_data_frame with all successful files
def test_create_data_frame_all_success_1():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","c"],"csv")
    df = csv_processor.create_data_frame(files)
    assert df.shape[1] == 4

# Test create_data_frame with all successful files
def test_create_data_frame_all_success_2():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","c"],"csv")
    df = csv_processor.create_data_frame(files)
    assert df.shape[0] == 10

# Test if pivot_table returns correct rows and columns.
def test_pivot_1():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","b","c","d"],"csv")
    data = csv_processor.create_data_frame(files)
    pivoted_dataframe = data.pivot_table(index="uid", columns="path", values="minutes", aggfunc="sum")
    assert pivoted_dataframe.shape[0] == 4

# Test if pivot_table returns correct rows and columns.
def test_pivot_2():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","b","c","d"],"csv")
    data = csv_processor.create_data_frame(files)
    pivoted_dataframe = data.pivot_table(index="uid", columns="path", values="minutes", aggfunc="sum")
    assert pivoted_dataframe.shape[1] == 4

# Test if pivot_table returns correct value.
def test_pivot_3():
    files = csv_processor.create_file_list(f'https://raw.githubusercontent.com/{github_username}/{github_repo_name}/script-csv-processor/script_version/test_data/',["a","b","c","d"],"csv")
    data = csv_processor.create_data_frame(files)
    pivoted_dataframe = data.pivot_table(index="uid", columns="path", values="minutes", aggfunc="sum")
    assert pivoted_dataframe.at[2,'/a'] == 12

