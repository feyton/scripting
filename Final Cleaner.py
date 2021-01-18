import os
import random
import re
import shutil
import stat

# Get the path to the file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DESTINATION_FOLDERS_BASE = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))


# Destination folders

DOCUMENTS_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Documents')
VIDEOS_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Videos')
PICTURES_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Pictures')
SOFTWARE_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Software')
AUDIO_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Audio')
DUPLICATE_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Duplicate')

# Destinations for specific files types
TVSERIES_DEST = os.path.join(VIDEOS_DEST, 'Series')
MOVIES_DEST = os.path.join(VIDEOS_DEST, 'Movies')
DOCUMENTARY_DEST = os.path.join(VIDEOS_DEST, 'Documentaries')
TUTORIAL_DEST = os.path.join(VIDEOS_DEST, 'Tutorials')
DESIGN_DEST = os.path.join(PICTURES_DEST, 'Design')
PLAYLIST_DEST = os.path.join(AUDIO_DEST, 'Playlist')
UN_CATEGORISED_DEST = os.path.join(DESTINATION_FOLDERS_BASE, 'Other')

# Making the destination directories
LIST_DIR = [DOCUMENTS_DEST, VIDEOS_DEST, PICTURES_DEST, SOFTWARE_DEST,
            TVSERIES_DEST, MOVIES_DEST, DOCUMENTARY_DEST, TUTORIAL_DEST, DESIGN_DEST, PLAYLIST_DEST, UN_CATEGORISED_DEST, DUPLICATE_DEST]

# Function to make missing directories.


def folder_check(list_of_folders):
    for i in list_of_folders:
        exist = os.path.isdir(i)
        if exist:
            pass
        else:
            os.makedirs(i)


def file_rename(files):
    file_to_rename = files
    name, ext = os.path.splitext(file_to_rename)
    number = random.randint(1, 10)
    new_name = f'{name}-{number}{ext}'
    return new_name

# This function will handle errors in rmtree using shutil


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def is_episode(name):
    match = re.match(r'.*(s[0-9]{2}e[0-9]{2})', name.lower())
    if match:
        return match.group(1)
    return None

print("""
Let us get to know each other, Am Fahrer Feyton Fabruce the author of this script.\nWhat About you?""")

user = input('What is your name? \n ><>>')

print(f"""
Dear {user.capitalize()},
This program will move files from this folder where the program is placed
and create specific directories for different file types. 
    If you want to proceed type in 1
    If you don't type in 2
Files in this folder '{BASE_DIR} will be moved to {DESTINATION_FOLDERS_BASE}
If a duplicate is found, it will be moved to Duplicate folder!!
Let's go>>>>>
""")
answer = input(
    f"{user.capitalize()}, If you want to procced, Type '1'\nIf otherwise type in 2:\n><>> ")


# List of extensions and their corresponding formats to be checked against
# I didn't use dictionary to avoid repetition of folders
audio = ['.aif', '.cda', '.mid', '.midi', '.mp3',
         '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.m3u']
documents = ['.txt', '.doc', '.docx', '.odt', '.pdf',
             '.rtf', '.tex', '.wks', '.wps', '.wpd', '.key', '.odp', '.pps',
             '.ppt', '.pptx', '.ods', '.xlr', '.xls', '.xlsx', '.csv']

design = ['.xd', '.psd', '.html', '.css']
videos = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
          '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.webm', '.srt']
compressed = ['.7z', '.arj', '.deb', '.pkg',
              '.rar', '.rpm', '.tar.gz', '.z', '.zip']

executables = ['.apk', '.bat', '.com', '.exe', '.jar', '.wsf', '.msi', '.py']

pictures = ['.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg',
            '.png', '.ps', '.svg', '.tif', '.tiff', '.CR2', '.JPG']
playlist = ['.zpl', '.xspf']
downloading = ['.crdownload', '.download', '.tmp']

# **********************


# Substrings to check against to identify different categories of the file
tutorials = ['tutorial', 'course', 'how to', 'python', 'build',
             'crash', 'course', 'html', 'css', 'django', 'beginner']

tv_series = ['s01', 's02', 's03', 's04', 's05', 's06', 's07']
documentary = ['documentary', '15 ', 'artificial', 'last week']


# The real script
if answer == '1':
    # Create the folders, if they don'exist usining the function
    folder_check(LIST_DIR)
    # loop through the whole folder
    for root, folders, files in os.walk(BASE_DIR, topdown=False):
        for fil in files:
            is_folder = os.path.isdir(fil)
            file_name, file_ext = os.path.splitext(fil)
            f = os.path.join(root, fil)
            if not is_folder:
                try:
                    if file_ext in executables:
                        shutil.move(f, SOFTWARE_DEST)

                    elif file_ext in audio:
                        shutil.move(f, AUDIO_DEST)

                    elif file_ext in compressed:
                        size = os.stat(f).st_size
                        # checking the size of compressed folder
                        if int(size) in range(0, 100000000):
                            shutil.move(f, DOCUMENTS_DEST)
                        elif int(size) in range(100000000, 700000000):
                            shutil.move(
                                f, TUTORIAL_DEST)
                        else:
                            shutil.move(f, VIDEOS_DEST)

                    elif file_ext in documents:
                        shutil.move(f, DOCUMENTS_DEST)

                    elif file_ext in videos:
                        size = os.stat(f).st_size
                        Tv_series_check = any(sub in file_name.lower()
                                              for sub in tv_series)
                        Documentary_check = any(sub in file_name.lower()
                                                for sub in documentary)
                        Tutorial_check = any(sub in file_name.lower()
                                             for sub in tutorials)

                        if Tv_series_check:
                            shutil.move(
                                f, TVSERIES_DEST)
                        elif Documentary_check:
                            shutil.move(f, DOCUMENTARY_DEST)

                        elif Tutorial_check:
                            shutil.move(f, TUTORIAL_DEST)

                        elif int(size) in range(700000000, 9000000000):
                            shutil.move(f, MOVIES_DEST)

                        else:
                            shutil.move(f, VIDEOS_DEST)
                    elif file_ext in pictures:
                        shutil.move(f, PICTURES_DEST)

                    elif file_ext in playlist:
                        shutil.move(
                            f, PLAYLIST_DEST)
                    elif file_ext in design:
                        shutil.move(
                            f, DESIGN_DEST)
                    elif file_ext in downloading:
                        pass
                    else:
                        shutil.move(
                            f, UN_CATEGORISED_DEST)

                except Exception:
                    try:
                        shutil.move(f, DUPLICATE_DEST)

                    except Exception:
                        pass
            else:
                pass

    print('Do you wish to delete those empty folders too??\n If so, answer with yes. \n But make sure there is no files in those folders, or else\n You lose them')

    folder_delete = input(
        "If fou want directories deleted. Type in 'Yes'\n Else, type in any letter to continue: \n >> ")

    if folder_delete.lower() == 'yes':
        for a, b, c in os.walk(BASE_DIR, topdown=False):
            for fold in b:
                p = os.path.join(a, fold)
                try:
                    os.rmdir(p)
                except Exception:
                    print(
                        f'This folder {p} \ncannot be deleted because it contains files')
        dare = input(f"""
        {user.capitalize()}
        We Tried to delete empty folders.
        If you want to delete this folder{BASE_DIR},
        Check if no file and you want to delete.
        Type in 'Delete' to continue
        or type 'M', to leave them:
        >>>""")
        if dare.lower() == 'delete':
            try:
                # using onerror will call the function to handle the error and repeat the code
                shutil.rmtree(BASE_DIR, onerror=remove_readonly)
            except Exception:
                print(f'{user.capitalize()}, We apologize for the inconvenience!\n')
        else:
            print('Good one!!!')
    else:
        print(f'{user.capitalize()}, Your folders are left intact. \n \n Thank You!!!!')

    print(f"The process has finished. \nIf you are happy with the result consider sharing our program.")
    print(
        f'If you want to use this sript again you can find it in:\n {SOFTWARE_DEST}.\n')
    print(f'Good bye {user.capitalize()}')
else:
    print(
        f"Thank you for checking out my script!!. \n See you soon {user.capitalize()}")
