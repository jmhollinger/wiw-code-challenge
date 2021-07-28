# wiw-code-challenge
 Response to When I Work code challenge to retrieve a set of csv files, transform the data, and return a new single csv with the result.

##  Setup

1. Clone the Repo
2. Initialize the venv
3. Install dependencies from requirements.txt
4. Run python3 process_csv_files.py OR run process_csv

## Tests

This program uses pytest for unit testing using. To run tests simply run pytest from the root of the repo.

## Documentation

Pandas handles dataframe loading and manipulation.

The program contains two functions that are part of the csv_processor module:

### create_file_list(base_url="", identifier_list=[], file_extension="")

This function creates a list of file urls for future processing based on a base_url, a list of filename identifiers, and the file extension of all the files.

- base_url : This is the base_url for all files it defaults to.
- identifier_list : This is the name of each file at the base_url. This defaults to lower case letters a-z (26 items).
- file_extension : The extension of the files at the the base_url defaults to csv.


### create_data_frame(url_list=[])

This function takes a list of CSV urls that have the same column layout and returns a single dataframe with the data from all the successfully processed csv files. It will skip any files it is unable to process and will compare the column layout of each file to that of the first successfuly processed file to ensure no unexpected results occur in the final data frame.

- url_list : A list of csv file urls with same data structure.

