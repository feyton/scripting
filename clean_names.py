import os
import re

MOVIES_DEST = "D:/MOVIES/"
DOCUMENTARY_DEST = "D:/DOCS/"
TUTORIALS_DEST = "C:/Users/Feyton Inc/Documents/Crack It/"
VIDEOS_DEST = "D:/VIDEOS/"
MUSIC_DEST = "C:/Users/Feyton Inc/Music/"
folders_to_clean = [MOVIES_DEST, DOCUMENTARY_DEST,
                    TUTORIALS_DEST, MUSIC_DEST, VIDEOS_DEST]


def clean_string(string):
    string = str(string)
    string = string.replace(".", ' ').strip()
    if '_' in string:
        string = string.replace("_", " ").strip()
    if "  " in string:
        string = string.replace("  ", "").strip()
    match = re.match(r'.*([1-3][0-9]{3})', string)
    if match:
        year = match.group(1)
        string = string.split(year)[0].strip()

    return string.title()


for folder in folders_to_clean:

    for root, folders, files in os.walk(folder, topdown=False):
        for fold in folders:
            os.chdir(os.path.join(root, fold))
            fol = os.listdir()
            for fil in fol:
                file_name, file_ext = os.path.splitext(fil)
                if file_ext != '':
                    # print(file_name)
                    cleaned_name = clean_string(file_name)
                    new_name = "%s%s" % (cleaned_name, file_ext)
                    try:
                        os.rename(fil, new_name)
                    except FileExistsError:
                        pass

        os.chdir(root)
        folder = os.listdir()
        for fil in folder:
            file_name, file_ext = os.path.splitext(fil)
            if file_ext != '':
                cleaned_name = clean_string(file_name)
                new_name = "%s%s" % (cleaned_name, file_ext)
                try:
                    os.rename(fil, new_name)
                except FileExistsError:
                    pass
