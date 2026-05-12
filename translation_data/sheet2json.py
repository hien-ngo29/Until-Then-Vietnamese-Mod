# Usage: python3 sheet2json.py

# Helper script to convert xlsx file in sheet directory back into json files
# Converted files are put in json directory

import pandas, json, time
from pathlib import Path

dataframe = None
start_index_counter = 0

def load_dataframe_from_sheet():
    global dataframe
    
    sheet_path = Path("./sheet")
    sheet_files = [f for f in sheet_path.iterdir() if f.is_file()]

    dataframe = pandas.read_excel(sheet_files[0])

def get_dict_data_from_json_file(json_path: Path):
    file = open(str(json_path), "r")
    data = json.load(file)
    file.close()
    return data

def write_dict_data_to_json_file(json_path: Path, dict_data: dict):
    file = open(str(json_path), "w")
    json.dump(dict_data, file, ensure_ascii=False, indent=4)
    file.close()

def write_json_files_in_recursive_dir(dir: Path):
    global start_index_counter
    
    for path in dir.iterdir():
        if (path.is_file()):
            json_dict_data = get_dict_data_from_json_file(path)
            json_dict_data = get_ranged_dict_data_from_data_frame(start_index_counter, start_index_counter + len(json_dict_data))
            start_index_counter += len(json_dict_data)
            write_dict_data_to_json_file(path, json_dict_data)
        else:
            write_json_files_in_recursive_dir(path)

def get_ranged_dict_data_from_data_frame(start, end):
    dict_result = {}
    
    for i in range(start, end):
        row = dataframe.iloc[i]
        dict_result[row["VĂN BẢN GỐC"]] = row["VĂN BẢN DỊCH"]
    
    return dict_result

load_dataframe_from_sheet()
write_json_files_in_recursive_dir(Path("json"))