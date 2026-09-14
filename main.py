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
def user_input_folder() -> str:
    console_folder_choice()
    while True:
        user_in = input("Enter index\n")
        if user_in in p_choices:
            return p_choices[user_in]
        print("Please enter valid index\n")

# user input for file extensions
def user_input_file_extension() -> str:
    return input("Enter a extension without the dot, example for .pdf you enter pdf\n")

# function to  get the list of all the current files within the download section 
def list_files(users_chosen_path=DOWNLOAD_PATH) -> list[str]:
    try:
        return os.listdir(users_chosen_path)
    except (PermissionError, OSError) as e:
        print(e)
        return []


# function to create a folder based on the file extension
def create_folder(users_choice_move_path, file_ext="PDF") -> str:
    target = os.path.join(users_choice_move_path, file_ext.upper())
    try:
        os.makedirs(target, exist_ok=True)
        print("Folder created...")
    except (PermissionError, OSError) as e:
        print(e)
    return target

# function to move files to there folder based on extension
def move_files(all_files, users_choice_target_path, users_choice_move_path, file_ext) -> None:
    if not os.path.exists(users_choice_move_path):
        print(f"Target path does not exist: {users_choice_move_path}")
        return
    for file in all_files:
        if file.lower().endswith("." + file_ext.lower()):
            try:
                sl.move(
                    os.path.join(users_choice_target_path, file),
                    users_choice_move_path,
                )
            except (sl.Error, OSError) as e:
                print(e)

# -----------------------------------------------

# -- MAIN OPERATION --
def main() -> None:
    print("Which folder to sort ?\n")
    user_sorting_folder = user_input_folder()
    print("Which folder to move in ?\n")
    user_target_folder = user_input_folder()
    print("Which files should be sorted/moved ?\n")
    user_sorting_file_extension = user_input_file_extension()
    
    # -- The Actual moving/sorting --
    files = list_files(user_sorting_folder)
    path_to_move_files = create_folder(user_target_folder, user_sorting_file_extension)
    move_files(files, user_sorting_folder, path_to_move_files, user_sorting_file_extension)

if __name__ == "__main__":
    main()