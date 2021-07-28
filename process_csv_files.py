import pandas as pd
from csv_processor.csv_processor import create_file_list
from csv_processor.csv_processor import create_data_frame
import logging

logging.basicConfig(
level=logging.DEBUG, 
format='%(asctime)s | %(levelname)s | %(message)s')

"""
TO DO:

Create Test Data Programmatically
Verify Local Install Instructions

"""

# Create List of Files using default options
files = create_file_list()

# Merge Files into Data Frame
merged_data = create_data_frame(files)

# Pivot Data
pivoted_dataframe = merged_data.pivot_table(index="user_id", columns="path", values="length", aggfunc="sum")
logging.info("Data frame pivoted.")
logging.info(pivoted_dataframe.shape[0], pivoted_dataframe.shape[1])

# Save to CSV
pivoted_dataframe.to_csv("data/web_traffic_data.csv")