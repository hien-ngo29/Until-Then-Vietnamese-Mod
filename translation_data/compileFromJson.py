# Usage: python3 compileFromJson.py
# This script compiles json files in json directory to .inkb files in compiled directory

import os, json
from pathlib import Path

isSuccess = True

def get_alternative_vanilla_path_from_json_path(json_path: Path):
    vanilla_path = Path(str(json_path).replace("json/", "vanilla/").replace(".strings.json", ".inkb"))
    return vanilla_path

def move_compiled_file_from_vanilla_dir(bin_path: Path):
    compiled_path = Path(str(bin_path).replace("vanilla/", "compiled/").replace(".modified.bin", ".inkb"))
    compiled_path.parent.mkdir(parents=True, exist_ok=True)
    Path.move(bin_path, compiled_path)

def compile(json_dir: str, compiled_dir: str):
    files = [p.name for p in Path(json_dir).iterdir() if p.is_file()]

    dirs = [p.name for p in Path(json_dir).iterdir() if p.is_dir()]

    for fil in files:
        filepath = json_dir + "/" + fil
        
        if Path(fil).suffix == ".json":
            print("Compiling file " + fil)

            vanilla_path = get_alternative_vanilla_path_from_json_path(Path(filepath))

            if (os.name == "posix"):
                os.system("./inkcpp_bineditor --replace=" + str(filepath) + " " + str(vanilla_path))
            elif (os.name == "nt"):
                os.system("./inkcpp_bineditor.exe --replace=" + str(filepath) + " " + str(vanilla_path))

            bin_path = Path(str(vanilla_path).replace(".inkb", ".modified.bin"))
            move_compiled_file_from_vanilla_dir(bin_path)

    for di in dirs:
        compile(json_dir + "/" + di, compiled_dir)

def verify(dirToVerify: str, dirExpected: str):
    global isSuccess

    verifyFiles = [p.name.replace(".strings.json", "") for p in Path(dirToVerify).iterdir() if p.is_file()]
    expectedFiles = [p.name.replace(".inkb", "") for p in Path(dirExpected).iterdir() if p.is_file()]

    dirs = [p.name for p in Path(dirExpected).iterdir() if p.is_dir()]

    uniqueFiles = sorted(set(verifyFiles) ^ set(expectedFiles))
    if (uniqueFiles != []):
        for uniqueFile in uniqueFiles:
            isSuccess = False
            print("Failed to decompile " + dirExpected + "/" + uniqueFile + ".inkb");

    for di in dirs:
        path1 = dirToVerify + "/" + di
        path2 = dirExpected + "/" + di
        if Path(path1).name == Path(path2).name:
            verify(path1, path2)

if __name__ == "__main__": 
    compile("json", "compiled")
    print("------")

    # verify("json", "compiled")
    if (isSuccess):
        print("All files decompiled successfully!")

