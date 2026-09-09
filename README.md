# 🌳 -SILISTER TOOL-

> A stylized, professional, and modular command-line file exploration and classification utility inspired by the standard `tree` command, enhanced with custom color themes, ASCII art banners, and native system integration.

---

## 🚀 Features

- **Recursive Directory Mapping:** Visually explores and maps out sub-directories and files seamlessly.
- **Native File Classification:** Interacts with system utilities (`file`) to detect and display accurate file types and states (e.g., Python scripts, C source files, empty files).
- **Dynamic ANSI Color Themes:** Implements a clean class-based color management system to prevent color bleeding and style terminal output elegantly.
- **ASCII Art Branding:** Integrated `figlet` branding with custom alternating color effects.
- **Interactive Help Manual:** Built-in manual with clear usage guidelines and zero visual clutter.

---

## 🛠️ Prerequisites & Dependencies

The tool relies on Python's standard libraries, but it requires the `figlet` utility for the ASCII art banner animation. 

If `figlet` is missing on your system, you can install it manually based on your distribution:

```bash
# Debian / Ubuntu / Kali Linux
sudo apt install figlet

# macOS (Homebrew)
brew install figlet
```

---

## 📦 Installation & Global Setup

To download, configure, and make the tool executable from **anywhere** in your terminal, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/youri-01/silister-tool.git
cd silister-tool
```

### 2. Make the Script Executable (`chmod +x`)
Add execution permissions to your main script and ensure it has a proper python shebang (`#!/usr/bin/env python3`) at the very top of `SilisTree.py`:
```bash
chmod +x SilisTree.py
```

### 3. Run Globally from Any Directory (Optional)
To run `silister` from anywhere without typing the full path, you can create a symbolic link in `/usr/local/bin`:
```bash
sudo ln -s $(pwd)/SilisTree.py /usr/local/bin/silister
```

Now you can use it globally like a native Linux command:
```bash
silister <folder_name>
# Or for the help manual:
silister help
```

---

## 💻 Usage (Local)

If you didn't set up the global symlink, run it directly via Python:

```bash
python3 SilisTree.py <folder_name>
```

### Example:
```bash
python3 SilisTree.py Module3
```

### Help Manual:
```bash
python3 SilisTree.py help
```

---

## 📂 Project Structure

```text
├── SilisTree.py       # Main entry point and directory traversal logic
├── banners.py         # ASCII art rendering and dynamic color animation
├── colors.py          # ANSI escape code classes and theme management
└── README.md          # Documentation
```

---

## 👤 Author

- **youri-01**

---

## 🛡️ Support & Feedback

If you encounter any unexpected behavior, bugs, or have feature requests, please open an issue on the [GitHub Issues page](https://github.com/youri-01/silister-tool/issues).
