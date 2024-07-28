from src.move_file import cleanup_directory
import unittest
from pathlib import Path
import os

class Testcleanup_directory(unittest.TestCase):
    def setUp(self):
        cdo = cleanup_directory()
        self.user_name = os.getlogin()
        cdo.source_directory = f"C:/Users/{self.user_name}/Downloads"
        cdo.archive_directory = f"C:/Users/{self.user_name}/Downloads/Archives"
        with open(f"C:/Users/{self.user_name}/Downloads/testfile123.txt", 'w') as fp:
            pass
        while True:
            cdo.get_dest_dir()
            cdo.move_files()
            val = input("Enter source directory continue or C to exit: ")
            if val == "c" or val == "C":
                break
            else:
                cdo.source_directory = val


    def test_move_files(self):
        self.assertFalse(os.path.exists(Path(f"C:/Users/{self.user_name}/Downloads/testfile123.txt")), "File did not move" )
        

# Run the tests
if __name__ == '__main__':
    unittest.main()