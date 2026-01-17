import os 
import shutil as sl


# -- A programm to sort files into a directory specific for there file extension --

# Global variables
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DOCUMENTS_PATH = os.path.join(os.path.expanduser("~"), "Documents")
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

# possible Choices 1: Downloads , 2: Documents, 3: Desktop
p_choices = {"1": DOWNLOAD_PATH, "2": DOCUMENTS_PATH, "3": DESKTOP_PATH}

# -----------------------------------------------

# -- FUNCTIONS -- 

def console_folder_choice()-> None:
    print("1: Downloads\n2: Documents\n3. Desktop\n")

# controlling user input for entering index for the desired folder
def user_input_folder()-> str:
    try: 
        console_folder_choice()
        while True:
            try: 
                user_in = input("Enter index\n")
                if 1 <= int(user_in) <= 3:
                    break
                print("Please enter valid index\n")
            except:
                print("Please enter valid index\n")
        
    except Exception as e :
        print(e)
    return p_choices[user_in]

# user input for file extensions
def user_input_file_extension()-> str:
    try:
        file_ext = input("Enter a extension without the dot, example for .pdf you enter pdf\n")
    except Exception as e :
        print(e)
    return file_ext

# function to  get the list of all the current files within the download section 
def list_files(users_chosen_path= DOWNLOAD_PATH) -> list[str]:
    try:
        all_files = os.listdir(users_chosen_path)
    except PermissionError as e:
        print(e)
    except OSError as e :
        print(e)
    return all_files


# function to create a folder based on the file extension
def create_folder(users_choice_move_path, file_ext="PDF") -> None:
    try:
        os.makedirs(os.path.join(users_choice_move_path, file_ext.upper()),exist_ok=True)
        print("Folder created...")
    except PermissionError as e:
        print(e)
    except OSError as e:
        print(e)
    return os.path.join(users_choice_move_path, file_ext.upper())

# function to move files to there folder based on extension
def move_files(all_files: list[str], users_choice_target_path, users_choice_move_path, file_ext) -> None :
    if  os.path.exists(users_choice_move_path):
        try:
            for files in all_files:
                if files.lower().endswith("." + file_ext.lower()):
                    try:
                        sl.move(os.path.join(users_choice_target_path,files),users_choice_move_path)
                    except sl.Error as e:
                        print(e)
        except Exception as e:
            print(e)

# -----------------------------------------------

# -- MAIN OPERATION --
if __name__ == "__main__":
    # -- User input --
    print("Which folder to sort ?\n")
    user_sorting_folder = user_input_folder()
    print("Which folder to move in ?\n")
    user_target_folder = user_input_folder()
    print("Which files should be sorted/moved ?\n")
    user_sorting_file_extension = user_input_file_extension()
    
    # -- The Actual moving/sorting --
    files = list_files(user_sorting_folder)
    path_to_move_files = create_folder(user_target_folder,user_sorting_file_extension)
    move_files(files, user_sorting_folder, path_to_move_files, user_sorting_file_extension)