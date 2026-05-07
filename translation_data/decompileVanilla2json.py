# This script decompiles inkb files from vanilla directory and overwrites all data into json directory
# Your changes in json directory would lost
# This binary is required: Put it next to this script (https://github.com/nikitalita/inkcpp/releases)

# TODO: it works well. But need refactoring
# P.S: currently there's no point of refactoring this script as it is just a helper script and already serves well what it should do. But i would happy if someone did

import os
from pathlib import Path

isSuccess = True

def decompile(vanillaDir: str, outputDir: str):
    files = [p.name for p in Path(vanillaDir).iterdir() if p.is_file()]

    dirs = [p.name for p in Path(vanillaDir).iterdir() if p.is_dir()]

    for fil in files:
        if Path(fil).suffix == ".inkb":
            print("Decompiling file " + fil)
            filepath = vanillaDir + "/" + fil

            if (os.name == "posix"):
                os.system("./inkcpp_bineditor --dump " + filepath)
            elif (os.name == "nt"):
                os.system("./inkcpp_bineditor.exe --dump " + filepath)

            fileToMove = Path(filepath.replace(".inkb", ".strings.json"))
            fileDestination = Path(outputDir + "/" + "/".join(vanillaDir.split("/")[1:]) + "/" + fileToMove.name)
            Path.move(fileToMove, fileDestination)
            print()

    for di in dirs:
        decompile(vanillaDir + "/" + di, outputDir)

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

decompile("vanilla", "json")
print("------")

verify("json", "vanilla")
if (isSuccess):
    print("All files decompiled successfully!")

