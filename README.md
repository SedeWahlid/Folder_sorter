# 🗂️ Auto File Sorter & Organizer

> A lightweight, interactive Command Line Interface (CLI) tool built in Python to instantly declutter your computer. It automatically sorts and moves files from a source directory to a target directory based on their file extensions, keeping your workspace clean and organized.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-4D4D4D?style=for-the-badge\&logo=gnometerminal\&logoColor=white)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20macOS%20%7C%20Linux-0078D6?style=for-the-badge\&logo=windows\&logoColor=white)

---


## ✨ Features

* 📂 **Pre-configured Paths**: Instantly access your `Downloads`, `Documents`, or `Desktop` folders.
* 🎯 **Extension-Based Sorting**: Target specific file types (e.g., `pdf`, `jpg`, `docx`).
* 📁 **Auto-Folder Creation**: Automatically generates a neatly named folder (e.g., "PDF") in your target directory.
* 🛡️ **Error Handling**: Built-in protections against permission errors and invalid user inputs.
* ⚡ **Zero Dependencies**: Runs entirely on Python's standard library (`os`, `shutil`). No `pip install` required except for the tests then you need to install pytest!

---

## 🖼️ Preview

> Clean, interactive terminal prompts guide you through the process.

```text
Which folder to sort ?
1: Downloads
2: Documents
3. Desktop
> 1

Which folder to move in ?
> 2

Which files should be sorted/moved ?
Enter a extension without the dot, example for .pdf you enter pdf
> pdf

Folder created...
[Files successfully moved!]
```

---

## 🛠️ Tech Stack

* 🐍 **Python** (Core Logic)
* 💻 **OS Module** (Path resolution & directory creation)
* 🚚 **Shutil Module** (High-level file operations & moving)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/SedeWahlid/Folder_sorter.git
cd Folder_sorter
```

*(Note: Because this script uses only Python's built-in standard libraries, there is no `requirements.txt` file to install!)*

---

## ▶️ Usage

Run the Python script directly in your terminal:

```bash
python main.py
```

Then follow the on-screen prompts:

1. Enter the number (`1`, `2`, or `3`) for the folder you want to clean up.
2. Enter the number for the destination folder where the files should go.
3. Type the file extension you want to move (e.g., `png`, `txt`, `mp4`).
4. Check your destination folder to see your newly organized files! 🎉

---

## 🧠 How It Works

* The script uses `os.path.expanduser("~")` to dynamically find your computer's Home directory, making it cross-platform compatible (works on Mac, Windows, and Linux).
* It scans the chosen source directory using `os.listdir()`.
* It creates a new, uppercase folder in the target directory using `os.makedirs(..., exist_ok=True)`.
* It iterates through the files, checking if they end with the specified extension (case-insensitive).
* Matching files are physically relocated using `shutil.move()`.

---

## 📁 Project Structure

```
📦 auto_file_sorter
 ┣ 📜 main.py
 ┣ 📜 README.md
 ┗ 📜 LICENSE
```

---

## ⚠️ Notes

* 🛑 **Files are MOVED, not copied**: This script physically relocates the files from the source to the destination. They will no longer be in the original folder.
* **Case-Insensitive**: If you type `pdf`, the script will successfully catch both `.pdf` and `.PDF` files.
* **No Dots Needed**: When prompted for the extension, type `jpg`, not `.jpg`.

---

## 📄 License

This project is licensed under the APACHE 2.0 License.

---
