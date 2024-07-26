from src.move_file import cleanup_directory
import os
cdo = cleanup_directory()
user_name = os.getlogin()
cdo.source_directory = f"C:/Users/{user_name}/Downloads"
cdo.archive_directory = f"C:/Users/{user_name}/Downloads/Archives"
while True:
    cdo.get_dest_dir()
    cdo.move_files()
    val = input("Enter source directory continue or C to exit: ")
    if val == "c" or val == "C":
        break
    else:
        cdo.source_directory = val