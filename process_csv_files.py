import pandas as pd
import csv_processor
import logging

logging.basicConfig(
level=logging.DEBUG, 
format='%(asctime)s | %(levelname)s | %(message)s')

# Create List of Files using default options
files = csv_processor.create_file_list()

# Merge Files into Data Frame
merged_data = csv_processor.create_data_frame(files)

# Pivot Data
pivoted_dataframe = merged_data.pivot_table(index="user_id", columns="path", values="length", aggfunc="sum")
logging.info(f"Data frame pivoted. {pivoted_dataframe.shape[0]} rows and {pivoted_dataframe.shape[1]} columns")

# Save to CSV
pivoted_dataframe.to_csv("data/web_traffic_data.csv")
logging.info(f"File saved to data/web_traffic.csv")
