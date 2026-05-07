import sys, os

def show_help():
    print("Handy script that helps convert json/xlsx files back into the inkb files.")
    print()
    print("Usage: " + os.path.basename(__file__), "<COMMAND> [OPTION]...")
    print()
    print("Command: ")
    print("    compile        Do compile from files. output goes to `./compiled`. See options to learn more.")
    print("    sync           Overwrite the file from directory `sheet` to `jsonstrings` by default. See options if you want to do opposite.")
    print()
    print("Option: ")
    print("    --fromjson     Compile all files from `jsonstrings` directory.")
    print("    --fromsheet    Compile all files from `sheet` directory.")
    print("    --sheet2json   Overwrite all files from `jsonstrings` directory with xlsx file from `sheet` directory. (default option with command <sync>)")
    print("    --json2sheet   Overwrite xlsx file from `sheet` directory with with json files from `jsonstrings` directory.")
    print("    -y --agree     Overwrite files without asking for confirmation.")

if (args_number <= 1):
    show_help()
