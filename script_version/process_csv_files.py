import pandas as pd
import csv_processor as csv_processor

# Create List of Files
files = csv_processor.create_file_list()

# Merge Files into Data Frame
data = csv_processor.create_data_frame(files)

# Save CSV
csv_processor.pivot_and_export(data)


