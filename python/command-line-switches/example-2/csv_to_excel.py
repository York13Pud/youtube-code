# --- Import required libraries / modules:
import argparse
import pandas as pd

from pathlib import Path


# --- 1. Setup the command line switch(es) for the program:
def directories() -> object:
    # --- Instantiate the argument parser:
    parser = argparse.ArgumentParser(prog = 'csv_to_excel',
                                    description = 'This program will convert csv files into Excel files.',
                                    add_help = True)

    # --- Add an argument for the first name:
    parser.add_argument("--source", "-s",
                        type = str, 
                        help = "Enter the directory containing the csv files.",
                        default = "/Users/neil/Documents/projects/youtube/youtube-code/python/command-line-switches/csv",
                        nargs = "?",
                        required = False)

    # --- Add an argument for the last name:
    parser.add_argument("--dest", "-d",
                        type = str, 
                        help = "Enter the directory to store the Excel files in.",
                        default = "/Users/neil/Documents/projects/youtube/youtube-code/python/command-line-switches/excel",
                        nargs = "?",
                        required = False)
    
    return parser.parse_args()


# --- 2. Check that the source and destination directories exist:
def check_dirs_exist(to_check: object) -> bool:
    for i in [to_check.source, to_check.dest]:
        if Path(i).exists() == False:
            raise Exception(f"The directory {i} does not exist. Please check it and try again.")
    
    return True


# --- 3. Go through the files in the folder and add only the files ending in csv to a list:
def get_source_csv_files(source_directory: str) -> list:
    directory = Path(source_directory)
    
    csv_files = list(directory.glob("*.csv"))
    
    if len(csv_files) == 0:
        raise Exception("No csv files were found in the source directory. Please check the directory and try again.")
    
    return csv_files


# --- 4. Process the list and convert each file to an excel file
def convert_csv_to_excel(csv_files: list, dest_dir: str) -> None:
    for i in csv_files:
        source = pd.read_csv(i)
        
        DEST_FILENAME = f"{dest_dir}/{i.stem}.xlsx"
        
        print(f"\033[0;37;40mConverting\033[4;36;40m {i}\033[0;37;40m to \033[4;32;40m{DEST_FILENAME}\033[0;37;40m")
        
        source.to_excel(DEST_FILENAME, 
                        sheet_name = "results",
                        index = False)


def main() -> None:
    """_summary_
    This is the main entry into the program.
    """
    
    # --- Get the directories that were passed by the user or use the defaults:
    results = directories()
    
    # --- Check that both the source and target directories exist:
    check_dirs_exist(to_check = results)
    
    # --- Get all the csv files in the source directory and
    csv_files = get_source_csv_files(source_directory = results.source)
    
    # --- Get the files in the source folder that have the csv extension:
    convert_csv_to_excel(csv_files = csv_files, dest_dir = results.dest)


# --- Run the main function:
if __name__ == "__main__":
    main()