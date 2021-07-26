import pandas as pd
import csv_processor as csv_processor

# Create List of Files
files = csv_processor.create_file_list()

# Merge Files into Data Frame
merged_data = csv_processor.create_data_frame(files)

# Pivot Data
pivoted_dataframe = merged_data.pivot_table(index="user_id", columns="path", values="length", aggfunc="sum")

# Save to CSV
pivoted_dataframe.to_csv("data/web_traffic_data.csv")