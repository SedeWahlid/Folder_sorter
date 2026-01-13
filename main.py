import os 
import shutil as sl


# -- A programm to sort files into a directory specific for there file extension --

# Global variables
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DOCUMENT_PATH = os.path.join(os.path.expanduser("~"),"Documents","PDF")
# -- FUNCTIONS -- 

# function to  get the list of all the current files within the download section 
def list_files() -> list[str]:
    try:
        all_files = os.listdir(DOWNLOAD_PATH)
    except PermissionError as e:
        print(e)
    except OSError as e :
        print(e)
    return all_files


# function to create a folder based on the file extension (For now only pdf files)
def create_folder() -> None:
    try:
        os.makedirs(DOCUMENT_PATH,exist_ok=True)
        print("Folder created...")
    except PermissionError as e:
        print(e)
    except OSError as e:
        print(e)

# function to move files to there folder based on extension (for now only pdf files)
def move_files(all_files: list[str]) -> None :
    if  os.path.exists(DOCUMENT_PATH):
        try:
            for files in all_files:
                if files.lower().endswith(".pdf"):
                    try:
                        sl.move(os.path.join(DOWNLOAD_PATH,files),DOCUMENT_PATH)
                    except sl.Error as e:
                        print(e)
        except Exception as e:
            print(e)

# -- MAIN OPERATION --
if __name__ == "__main__":
    files = list_files()
    create_folder()
    move_files(files)