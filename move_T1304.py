#!python
import os
import shutil
from datetime import datetime, timedelta
import pathlib
import uuid

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


class cleanup_directory:

    def move_files(self):
        files = os.listdir(self.source_directory)
        for filename in files:
            self.file_path = os.path.join(self.source_directory, filename)
            self.file_ext = pathlib.Path(filename).suffix
            self.filename = filename
            if self.file_ext in self.list_ext:
                destination_path = os.path.join(self.dest_directory, self.filename)
                file_name, file_ext = os.path.splitext(self.filename)
                file_version = 0
                while os.path.exists(destination_path):
                    new_file_name = file_name + f"_v{file_version}" + file_ext
                    destination_path = os.path.join(self.dest_directory, new_file_name)
                    file_version = file_version + 1
                shutil.move(self.file_path, destination_path)
                print(f"Moved '{self.filename}' to '{self.dest_directory}'")

    def move_old_files(self):
        # Calculate the date threshold (1 year ago)
        one_year_ago = datetime.now() - timedelta(days=365)

        # Create the archive directory if it doesn't exist
        if not os.path.exists(self.archive_directory):
            os.makedirs(self.archive_directory)

            for root, _, files in os.walk(self.source_directory):
                for filename in files:
                    file_path = os.path.join(root, filename)
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
        FileType_completer = WordCompleter(
            [
                "Images",
                "PDFs",
                "Archives",
                "Apps",
                "Fonts",
                "Videos",
                "Office",
            ],
            ignore_case=True,
        )

        user_name = os.getlogin()
        text = prompt(
            "File Type: ", completer=FileType_completer, complete_while_typing=True
        )
        print("You said: %s" % text)
        match text:
            case "Images":
                self.dest_directory = f"C:/Users/{user_name}/Pictures"
                self.list_ext = [
                    ".png",
                    ".jpg",
                    ".jpeg",
                    ".svg",
                    ".ico",
                    ".webp",
                    ".drawio",
                    ".gif",
                    ".excalidraw",
                    ".eps",
                    ".avif",
                    ".excalidrawlib",
                ]
            case "PDFs":
                self.dest_directory = f"C:/Users/{user_name}/Downloads/PDFs"
                self.list_ext = [
                    ".pdf",
                    ".epub",
                    ".md",
                    ".txt",
                    ".bib",
                    ".tex",
                    ".ris",
                    ".html",
                ]
            case "Archives":
                self.dest_directory = f"C:/Users/{user_name}/Downloads/Archives"
                self.list_ext = [
                    ".zip",
                    ".tar",
                    ".tar.gz",
                    ".gz",
                    ".7z",
                    ".rar",
                    ".tgz",
                ]
            case "Apps":
                self.dest_directory = f"C:/Users/{user_name}/Downloads/Apps"
                self.list_ext = [".exe", ".bat", ".msi"]
            case "Fonts":
                self.dest_directory = f"C:/Users/{user_name}/Downloads/Fonts"
                self.list_ext = [".ttf"]
            case "Videos":
                self.dest_directory = f"C:/Users/{user_name}/Videos"
                self.list_ext = [".mp4"]
            case "Office":
                self.dest_directory = f"C:/Users/{user_name}/Downloads/Office"
                self.list_ext = [
                    ".docx",
                    ".pptx",
                    ".doc",
                    ".ppt",
                    ".xlsx",
                    ".xls",
                    ".odt",
                    ".odg",
                ]


if __name__ == "__main__":
    cdo = cleanup_directory()
    user_name = os.getlogin()
    cdo.source_directory = f"C:/Users/{user_name}/Downloads"
    # cdo.archive_directory = f"C:/Users/{user_name}/Downloads/Archives"
    while True:
        cdo.get_dest_dir()
        cdo.move_files()
        varin_exit_char = input("Press C to exit : ")
        if ( varin_exit_char == "c" or varin_exit_char == "C" ) :
            break;

