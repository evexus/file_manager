from pathlib import Path
import os
import shutil

# Extend it to delete in Specified folder
# Recycle Bin

# Specify the path to your Downloads folder
# downloads_folder = str(Path.home() / "Downloads")
downloads_folder = os.path.expanduser('~/Downloads')

# Function to delete files and folders recursively
# os.walk - Generates File names in a directory tree
def delete_contents(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path)
                print(f"Deleted folder: {dir_path}")
            except Exception as e:
                print(f"Error deleting folder {dir_path}: {e}")

# Code under that will only run when the script is run directly
# NOT when it's called as an import
# When importing all the code run besides this area
if __name__ == "__main__":
    try:
        delete_contents(downloads_folder)
        print("Downloads folder contents deleted successfully.")
    except Exception as e:
        print(f"Error deleting Downloads folder contents: {e}")