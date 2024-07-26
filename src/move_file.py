import json
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path


class cleanup_directory:

    def move_files(self):
        files = os.listdir(self.source_directory)
        for filename in files:
            self.file_path = Path(self.source_directory) / filename
            self.file_ext = Path(filename).suffix
            self.filename = filename
            if self.file_ext in self.dest_dir_path:
                self.dest_directory = self.dest_dir_path[self.file_ext]
            else:
                continue
            if self.file_ext in self.list_ext:
                destination_path = Path(self.dest_directory) / self.filename
                file_name, file_ext = Path(self.filename).stem, Path(self.filename).suffix
                file_version = 0
                while Path(destination_path).is_file():
                    new_file_name = file_name + f"_v{file_version}" + file_ext
                    destination_path = Path(self.dest_directory) / new_file_name
                    file_version = file_version + 1
                shutil.move(self.file_path, destination_path)
                print(f"Moved '{self.filename}' to '{self.dest_directory}'")

    def move_old_files(self):
        # Calculate the date threshold (1 year ago)
        one_year_ago = datetime.now() - timedelta(days=365)

        # Create the archive directory if it doesn't exist
        if not Path(self.archive_directory).is_dir():
            os.makedirs(self.archive_directory)

            for root, _, files in os.walk(self.source_directory):
                for filename in files:
                    file_path = Path(root) / filename
                    modification_date = datetime.fromtimestamp(
                        os.path.getmtime(file_path)
                    )

                    # Move the file to the archive directory
                    if modification_date < one_year_ago:
                        destination_path = os.path.join(
                            self.archive_directory, filename
                        )
                        shutil.move(file_path, destination_path)
                        print(f"Moved '{filename}' to '{self.archive_directory}'")

    def get_dest_dir(self):
        user_name = os.getlogin()
        with open(Path(__file__).parent / "list.json",'r') as f:
            l = json.load(f)
        d ={}
        for key,values in l.items():
            p = values.format(user_name=user_name)
            d[key]=p
        self.dest_dir_path = d
        self.list_ext = d.keys()
  

    
         


if __name__ == "__main__":
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

