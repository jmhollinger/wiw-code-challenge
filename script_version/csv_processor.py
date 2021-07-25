import pandas as pd
import string

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