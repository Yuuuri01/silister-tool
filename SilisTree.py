#!/usr/bin/env python3 


import os
import sys
import subprocess
from colors import colors
from banners import banners
    
def type_file(file_name) -> str:

    out = subprocess.run(
        ["file", file_name],
        capture_output=True,
        text=True
        )

    result = out.stdout.strip()
    return result.split(",")[0]

def process_path_type(type: str) ->str:
    return type.split(":")[1]

def main() -> None:
    if len(sys.argv) != 2:
        print(colors.warning_theme("try: help sub to see manuel"))
        return
    elif sys.argv[1] == "help":
        banners.banner()
        print("sub is a command line utility built to help you explore directories")
        print("and classify files with ease. it works similarly to the standard tree")
        print("command while providing detailed descriptions for every file it finds.")
        print()
        print("usage")
        print("    ./SilisTree folder_name")
        print("    python3 SilisTree.py folder_name")
        print()
        print("how it works")
        print("    the tool validates your input path to ensure it is a valid directory")
        print("    before scanning. it then maps out all your sub-directories and files")
        print("    while interacting with native system commands to detect exact file types.")
        print()
        print("support and feedback")
        print("    if you encounter any unexpected behavior or have questions, please")
        print("    open an issue on <github>: https://github.com/youri-01/silister-tool/issues")
        return
    
    elif len(sys.argv) == 2:
        banners.banner()
        folder_name = sys.argv[1]
        path = os.path.join(os.getcwd(), folder_name)
        try:
            print(f"{colors.GRAY}-------------------------------------------------{colors.RESET}")
            with os.scandir(path) as enties:
                for name in enties:
                    if name.is_dir():
                        path_v2 = os.path.join(os.getcwd(), name)
                        with os.scandir(path_v2) as en:
                            print(f"| {colors.folder_theme(name.name)}")
                            for i in en:
                                if i.is_file():
                                    print(f"|----|>{colors.file_theme(i.name)}({process_path_type(type_file(i)).strip()})")
                    elif name.is_file():
                        print(f"|{colors.folder_theme(" MAIN_DIR")}")       
                        print(f"|----|>{colors.file_theme(name.name)} ({process_path_type(type_file(name)).strip()})")
                    else:
                        print("| UNKWOWN")
                        print(f"{colors.file_theme(name.name)} ({process_path_type(type_file(name))})")
                print(f"{colors.GRAY}-------------------------------------------------{colors.RESET}")
        except OSError as e:
            print(f"{e}")
            print("Usage: python3 sSilisTree <directory_path>")
            print("Try 'python3 SilisTree help' for more information.")

if __name__ == "__main__":
    main()