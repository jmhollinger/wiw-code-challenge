import pandas as pd
import string
import logging

logging.basicConfig(
level=logging.DEBUG, 
format='%(asctime)s | %(levelname)s | %(message)s')


def create_file_list(base_url="https://public.wiwdata.com/engineering-challenge/data/", identifier_list=list(string.ascii_lowercase), file_extension="csv"):
    """
    This function creates a list of file urls for future processing based on a base_url, a list of filename identifiers, and the file extension of all the files.

    base_url : This is the base_url for all files it defaults to.
    identifier_list : This is the name of each file at the base_url. This defaults to lower case letters a-z (26 items).
    file_extension : The extension of the files at the the base_url defaults to csv.

    """

    # Used my map function to concat file path elements
    def create_url(identifier):
        return f'{base_url}{identifier}.{file_extension}'

    url_list = map(create_url, identifier_list)

    return list(url_list)


def create_data_frame(url_list):
    """
    This function takes a list of CSV urls that have the same column layout and returns a single dataframe

    url_list : A list of csv file urls with same data structure.

    """

    # Expected number of files
    num_of_files = len(url_list)
    logging.info(f"Attempting to process {num_of_files} files")

    # Get column layout of first file.
    initial_file = pd.read_csv(url_list[0])
    column_layout = list(initial_file.columns)

    # List of hold all the data frame for concatenation.
    data_frame_list = []
    
    # Loop through URLS to read data
    for url in url_list:
        # Try to create dataframe, on error set an empty one.
        try:
            data_frame = pd.read_csv(url)
        except:
            logging.warning(f"Could not create dataframe from file at {url}")
            data_frame = pd.DataFrame()
            pass

        if data_frame.empty != True:
            # Check the column layout against the first file for consistency
            data_frame_columns = list(data_frame.columns)
            
            if data_frame_columns == column_layout:
                data_frame_list.append(data_frame)
            else:
                logging.warning(f"File {url} has an inconsistent layout.")

    merged_data_frame = pd.concat(data_frame_list)

    logging.info(f"Successfully processed {len(data_frame_list)} files")

    return merged_data_frame