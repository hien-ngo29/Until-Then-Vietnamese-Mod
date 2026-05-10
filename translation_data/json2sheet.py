from openpyxl.styles import PatternFill
from pathlib import Path
import pandas, json

yellowFill = PatternFill (
    start_color="FFFF00",
    end_color="FFFF00",
    fill_type="solid"
)

def write_xlsx(jsons_dir: Path, output_dir: Path=Path("sheet")):
    excel_writer = pandas.ExcelWriter(output_dir / "UntilThen.xlsx", engine="openpyxl")

    workbook = excel_writer.book
    worksheet = workbook.create_sheet("UntilThen")

    worksheet["A1"] = "VĂN BẢN GỐC"
    worksheet["B1"] = "VĂN BẢN DỊCH"
    worksheet["C1"] = "CHẤT LƯỢNG"

    prev_dataframe = None
    sum_row = 0
    write_row = 0

    for i in range(0, len(all_filenames)):
        filename = all_filenames[i]
        dict_data = get_dict_data_from_json_file(filename)

        dataframe = pandas.DataFrame([dict_data]).T
        write_row = (write_row + len(prev_dataframe)) if (prev_dataframe is not None) else 0

        dataframe.to_excel(excel_writer, sheet_name="UntilThen", startrow=write_row+1, header=False)
        
        excel_writer.sheets["UntilThen"].column_dimensions["A"].width = 90
        excel_writer.sheets["UntilThen"].column_dimensions["B"].width = 90

        prev_dataframe = dataframe

    excel_writer.close()

all_filenames = []
file = open("test.txt", "w")

def get_all_json_filenames(jsons_dir: Path):
    for filepath in jsons_dir.iterdir():
        if filepath.is_file():
            all_filenames.append(filepath)
        else:
            get_all_json_filenames(filepath)

def get_dict_data_from_json_file(json_path: Path):
    file = open(str(json_path), "r")
    return json.load(file)

get_all_json_filenames(Path("json"))
write_xlsx(jsons_dir=Path("json"))
file.close()