import os
import re
import shutil
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

from art import tprint

from file_types import get_file_type
from folder_cleaner import (dare_cleaner, delete_empty_folders,
                            handle_existing_files, list_files_in_folder)
from name_cleaner import clean_names_in_folder
from series_cleaner import clean_series_in_folder

# FUNCTIONS


def get_or_create_folder(folder):
    """checking if a folder exits to avoid moving files
    into empty folders

    Args:
        folder (directory): os.path.isdir file path
    """
    if not os.path.isdir(folder):
        os.makedirs(folder)
    pass


def get_destination():
    root = tk.Tk()
    root.withdraw()
    print("Please select the destination")
    print("The folder have to be empty to avoid collision.")
    DESTINATION = filedialog.askdirectory(
        title="Select the destination folder")
    return DESTINATION


def check_if_folder_is_empty(path):
    if not os.path.exists(path):
        raise PermissionError("Folder don't exist")
    os.chdir(path)
    directory = os.listdir()
    if len(directory) == 0:
        return True
    return False


def resolve_destination(fold, dest):
    file_type = fold[0]
    destination = fold[-1]
    if file_type == destination:
        path = os.path.join(dest, destination)
    else:
        path = os.path.join(dest, "%s/%s" % (file_type, destination))
    get_or_create_folder(path)
    return path

# // FUNCTIONS


tprint("File Organizer")
root = tk.Tk()
root.withdraw()

print("Please select the folder to clean!!")
start = 1
while True:
    start += 1
    BASE_DIR = filedialog.askdirectory(
        title="Please choose the base directory", mustexist=True)
    if BASE_DIR != "" and os.path.exists(BASE_DIR):
        if not check_if_folder_is_empty(BASE_DIR):
            break

    if start > 3:
        print("You failed to select folder to clean")
        tprint("Bye", font="small")
        break

if BASE_DIR == "":
    time.sleep(3)
    exit()

print("The files in this directory '%s' will be organized" % BASE_DIR)
time.sleep(1)


def validate_destination():
    base = Path(BASE_DIR)
    ds = str(Path(DESTINATION))
    ex = ds.startswith(str(base))
    return ex


dstart = 1
while True:
    dstart += 1
    DESTINATION = get_destination()
    if validate_destination():
        print("Select a folder outside our base directory")
        if dstart > 3:
            tprint("You failed to specify the destination", font="small")
            tprint("Bye")
            DESTINATION = ""
            break
        continue
    elif DESTINATION == "":
        continue
    elif check_if_folder_is_empty(DESTINATION):
        print("Those files will be moved to: %s" % DESTINATION)
        break

    else:
        tprint("Non empty folder selected", font="small")
        time.sleep(1)
        join = input(
            "Use the current destination and join files?\n 'Y' Yes or 'N' No.\n*** ")
        if join.lower() == 'y':
            print('Your files will be moved to %s' % DESTINATION)
            print('Folders will be merged')
            break

        dest = os.path.join(DESTINATION, "FILES")
        get_or_create_folder(dest)
        DESTINATION = dest
        print('Your files will be moved to %s' % DESTINATION)
        break

if DESTINATION == "":
    time.sleep(3)
    exit()

DUPLICATES_DEST = os.path.join(DESTINATION, "Duplicates")

for root, folders, files in os.walk(BASE_DIR, topdown=False):
    for fil in files:
        if os.path.isdir(fil):
            pass
        f = os.path.join(root, fil)
        destination = resolve_destination(get_file_type(
            fil, size=os.stat(f).st_size), DESTINATION)
        try:
            shutil.move(f, destination)
        except shutil.Error:
            try:
                get_or_create_folder(DUPLICATES_DEST)
                new_name = handle_existing_files(f)
                shutil.move(os.path.join(root, new_name), DUPLICATES_DEST)
            except Exception:
                pass

tprint("Files has been moved", font="small")
time.sleep(2)
tv_series_dir = os.path.join(DESTINATION, "Videos")
folders_to_clean = [os.path.join(
    DESTINATION, "MUSIC"), os.path.join(DESTINATION, "Videos")]
clean = input(
    "To clean all videos, and audio. Please type in 1, \nelse type any character: ")
if clean == '1':

    if os.path.exists(tv_series_dir):
        if not check_if_folder_is_empty(tv_series_dir):
            clean_series_in_folder(
                tv_series_dir, os.path.join(DESTINATION, "TV SERIES"))
    for f in folders_to_clean:
        if os.path.exists(f):
            clean_names_in_folder(f)
    print("Files cleaning have been completed")

    tprint("Clean up time", font="small")

    delete_empty_folders(BASE_DIR)
    time.sleep(2)
    print("################\n")
    print("The following files are still in the folder")
    list_files_in_folder(BASE_DIR)
    print("#################")

    delete = input("Confirm deletion of files: 'Y' Yes or 'N' No\n****")
    if delete.lower() == "y":
        dare_cleaner(BASE_DIR, force=True)
    else:
        tprint("Thank you", font="medium")
        time.sleep(3)
        exit()
else:
    tprint("Thank You")
    time.sleep(3)
    exit()
