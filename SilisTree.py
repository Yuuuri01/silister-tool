#!/usr/bin/env python3 


import os
import sys
import subprocess

class colors:
    # ANSI Color Codes
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Colors
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"   
    CYAN = "\033[96m"
    GRAY = "\033[90m"
    RED = "\033[91m"

    @classmethod
    def folder_theme(cls, text: str) ->str:
        return f"{cls.BLUE}{cls.BOLD}{text}{cls.RESET}"
    @classmethod
    def file_theme(cls, text: str) ->str:
        return f"{cls.YELLOW}{cls.BOLD}{text}{cls.RESET}"
    @classmethod
    def warning_theme(cls, text) ->str:
        return f"{cls.RED}{cls.BOLD}{text}{cls.RESET}"
    
class banners:

    @staticmethod
    def print_banner(msg: str) ->None:
        color_msg = ""
        strat = 1
        end = 0
        for i in range(len(msg)):
            if strat:
                color_msg += colors.warning_theme(msg[i])
                end = 1
                strat = 0
            elif end:
                color_msg += colors.folder_theme(msg[i])
                end = 0
                strat = 1
        print(color_msg)

    @staticmethod
    def banner() ->None:
        try:
            ins: str = subprocess.run(
                ["figlet", "-f", "slant", "SILISTER TOOL"],
                capture_output=True,
                text=True,
                check=True
            )
            banners.print_banner(ins.stdout)
        except:
            print(colors.warning_theme("ERROR: figlet not found!"))
            answer: str = input(f"{colors.GREEN}did you want to download it(y/n): {colors.RESET}").strip()
            if answer == 'y' or answer == 'Y':
                try:
                    install("figlet")
                    ins = subprocess.run(
                        ["figlet", "-f", "slant", "SILISTER TOOL"],
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    banners.print_banner(ins.stdout)
                except:
                    print(f"{colors.warning_theme("ERROR: Cannot install tool!")}\n")
            else:
                print(f"\n\n{colors.GRAY}############################{colors.RESET}")
                print(f"{colors.GREEN}WELCOME  TO  SILISTER  TOOL{colors.RESET}")
                print(f"{colors.GRAY}############################\n{colors.RESET}")

def install(name_tool):
    try:
        print(f"{colors.CYAN}loading...{colors.RESET}")
        out = subprocess.run(
            ["sudo", "apt", "install", "-y", name_tool],
            capture_output=True,
            text=True,
            check=True
        )
        print("###################################")
        print(out.stdout)
        print(f"{colors.RED}###################################{colors.RESET}")
        print(f"{colors.GREEN}TOOL: Installed successfully!{colors.RESET}")
        print(f"{colors.RED}###################################{colors.RESET}\n")
    except:
        print(f"{colors.RED}all ready installed or tool not found!{colors.RESET}")

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
        print(colors.warning_theme("type: help sub to see manuel"))
        return
    elif sys.argv[1] == "help":
        banners.banner()
        print("sub is a command line utility built to help you explore directories")
        print("and classify files with ease. it works similarly to the standard tree")
        print("command while providing detailed descriptions for every file it finds.")
        print()
        print("usage")
        print("    sub folder_name")
        print("    python3 check_sub.py folder_name")
        print()
        print("how it works")
        print("    the tool validates your input path to ensure it is a valid directory")
        print("    before scanning. it then maps out all your sub-directories and files")
        print("    while interacting with native system commands to detect exact file types.")
        print()
        print("support and feedback")
        print("    if you encounter any unexpected behavior or have questions, please")
        print("    feel free to reach out to us via email at world_tools@proton.YOURI")
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
            print("Usage: python3 sub_map <directory_path>")
            print("Try 'python3 sub_map help' for more information.")

if __name__ == "__main__":
    main()