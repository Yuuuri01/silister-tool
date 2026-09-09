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
    