#!python
import os
import shutil
from datetime import datetime, timedelta
import pathlib

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

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

user_name = os.getlogin( ) 

def main():
    text = prompt(
        "File Type: ", completer = FileType_completer, complete_while_typing=True
    )
    print("You said: %s" % text)
    match text:
        case "Images":
            dest_directory = f"C:/Users/{user_name}/Pictures"
            list_ext = ['.png','.jpg','.jpeg','.svg','.ico','.webp','.drawio','.gif','.excalidraw','.eps','.avif','.excalidrawlib']
        case "PDFs":
            dest_directory = f"C:/Users/{user_name}/Downloads/PDFs"
            list_ext = ['.pdf','.epub','.md','.txt','.bib','.tex','.ris','.html']
        case "Archives":
            dest_directory = f"C:/Users/{user_name}/Downloads/Archives"
            list_ext = ['.zip','.tar','.tar.gz','.gz','.7z','.rar','.tgz']
        case "Apps":
            dest_directory = f"C:/Users/{user_name}/Downloads/Apps"
            list_ext = ['.exe','.bat','.msi']
        case "Fonts":
            dest_directory = f"C:/Users/{user_name}/Downloads/Fonts"
            list_ext = ['.ttf']
        case "Videos":
            dest_directory = f"C:/Users/{user_name}/Videos"
            list_ext = ['.mp4']
        case "Office":
            dest_directory = f"C:/Users/{user_name}/Downloads/Office"
            list_ext = ['.docx','.pptx','.doc','.ppt','.xlsx','.xls','.odt','.odg']

    return dest_directory,list_ext





class cleanup_directory:
    

    def move_files(self,file_type):
        files = os.listdir(self.source_directory)
        for filename in files:
            self.file_path = os.path.join(self.source_directory, filename)
            self.file_ext = pathlib.Path(filename).suffix 
            self.filename = filename

            # Move the .md files to the documents
            if file_type == 'image' :
                self.move_images()
            else:
                self.move_file(file_type)

    def move_old_files(self):
        # Calculate the date threshold (1 year ago)
        one_year_ago = datetime.now() - timedelta(days=365)

        # Create the archive directory if it doesn't exist
        if not os.path.exists(self.archive_directory):
            os.makedirs(self.archive_directory)

            for root, _, files in os.walk(self.source_directory):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    modification_date = datetime.fromtimestamp(os.path.getmtime(file_path))

                    # Move the file to the archive directory
                    if modification_date < one_year_ago:
                        destination_path = os.path.join(self.archive_directory, filename)
                        shutil.move(file_path, destination_path)
                        print(f"Moved '{filename}' to '{self.archive_directory}'")


    def move_images(self):
        # Move the .md files to the documents
        if self.file_ext == '.jpg' or self.file_ext == '.png' or self.file_ext == '.jpeg':
            destination_path = os.path.join(self.picture_directory, self.filename)
            shutil.move(self.file_path, destination_path)
            print(f"Moved '{self.filename}' to '{self.picture_directory}'")

    def move_file(self, list_ext):
        if self.file_ext in list_ext:
            destination_path = os.path.join(self.dest_directory, self.filename)
            shutil.move(self.file_path, destination_path)
            print(f"Moved '{self.filename}' to '{self.dest_directory}'")


            

if __name__ == "__main__":
    cdo = cleanup_directory()
    user_name = os.getlogin( ) 
    cdo.source_directory = f"C:/Users/{user_name}/Downloads"
    cdo.dest_directory, list_ext = main()
    cdo.archive_directory = f"C:/Users/{user_name}/Downloads/Archives"
    cdo.picture_directory = f"C:/Users/{user_name}/Pictures"
    cdo.move_files(list_ext)
