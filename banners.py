from colors import colors
import subprocess


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
        print(f"{colors.GREEN}figlet: Installed successfully!{colors.RESET}")
        print(f"{colors.RED}###################################{colors.RESET}\n")
    except:
        print(f"{colors.RED}already installed or 'figlet' not found!{colors.RESET}")

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
