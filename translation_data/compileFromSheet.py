# Usage python3 compileFromSheet.py
# Compile written data in sheet file to compiled directory. This would be your most used script.

import compileFromJson, sheet2json
from pathlib import Path

sheet2json.load_dataframe_from_sheet()
sheet2json.write_json_files_in_recursive_dir(Path("json"))

compileFromJson.compile("json", "compiled")
if (not compileFromJson.isSuccess):
    exit()