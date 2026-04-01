import os
import shutil
from DATA.categories import file_categories


def detect_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension


def detect_category(filename):
    extension = detect_extension(filename)

    for category, extensions in file_categories.items():
        if extension in extensions:
            return category

    return "others"

def scan_folder(folders):
    file_s = []
    for files in os.listdir(folders):  # this loop through all files in that folder
        location = os.path.join(folders, files)  # this give path of that folder ex download/file.png
        if os.path.isfile(location):  # this includes only file, ignore folder
            file_s.append(files)

    return file_s

def organize_folder(folder_path):  # function that organizes files inside a folder given by the user

    files = scan_folder(folder_path)

    for file in files:

        extension = detect_extension(file)
        category = detect_category(extension)

        category_path = os.path.join(folder_path, category)
        # build the path of the category folder
        # example: "Downloads" + "images" -> "Downloads/images"

        if not os.path.exists(category_path):
            # check if the category folder already exists

            os.makedirs(category_path)
            # if the folder does not exist, create it

        source = os.path.join(folder_path, file)
        # build the full path of the file's current location
        # example: "Downloads/photo.jpg"

        destination = os.path.join(category_path, file)
        # build the destination path where the file should go
        # example: "Downloads/images/photo.jpg"

        shutil.move(source, destination)
        # move the file from its original location to the new category folder





