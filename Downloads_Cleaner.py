import os
import random
import shutil
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

TVSERIES_DEST = "C:/Users/Feyton Inc/Videos/"
PLAYLIST_DEST = "C:/Users/Feyton Inc/Music/Playlists/"
SOFTWARE_DEST = "D:/SOFTWARE/"
AUDIO_DEST = "C:/Users/Feyton Inc/Music/"
DOCUMENT_DEST = "C:/Users/Feyton Inc/Documents/"
MOVIES_DEST = "D:/MOVIES/"
DOCUMENTARY_DEST = "D:/DOCS/"
PICTURES_DEST = "C:/Users/Feyton Inc/Pictures/"
TUTORIALS_DEST = "C:/Users/Feyton Inc/Documents/Crack It/"
OTHERS = "C:/Users/Feyton Inc/Documents/Others/"
VIDEOS_DEST = "D:/VIDEOS/"
DESIGN_DEST = "C:/Users/Feyton Inc/Documents/Design"


def Filename_change(file_to_rename, destination=None):
    name, ext = os.path.splitext(file_to_rename)
    num = random.randint(1, 10)
    new_name = f'{name}-{num}{ext}'
    fil = os.rename(file_to_rename, new_name)
    if destination is not None:
        shutil.move(fil, destination)

    else:
        return fil


def folders_check(list_of_folders):
    for i in list_of_folders:
        exist = os.path.isdir(i)
        if exist:
            pass
        else:
            os.makedirs(i)


def get_or_create_folder(name):
    exist = os.path.is_dir(name)
    if exist:
        pass
    else:
        os.makedirs(name)


def episode_season(name):
    l = ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 's09']
    p = ''
    for i in l:
        if i in name.lower():
            p = i
            break
        else:
            pass
    return p


def episode_folder(f):
    name, ext = os.path.splitext(f)
    season = episode_season(name)
    if season != '':
        nam = name.split(season)[0]
        fol = '%s/%s/' % (nam.replace('.', ' '), season)
    else:
        fol = name.split('.')[0]
        fol.strip()

    folder = os.path.join(TVSERIES_DEST, fol)
    get_or_create_folder(folder)
    return folder


class MyCleaner(FileSystemEventHandler):
    def on_modified(self, event):
        for folder in folders_to_track:
            os.chdir(folder)
            folder_new = os.listdir()

            for f in folder_new:
                file_name, file_ext = os.path.splitext(f)
                if file_ext != '':
                    try:
                        if file_ext in executables:
                            try:
                                shutil.move(f, SOFTWARE_DEST)
                            except FileExistsError:
                                Filename_change(f)

                        elif file_ext in audio:
                            shutil.move(f, AUDIO_DEST)

                        elif file_ext in compressed:
                            size = os.stat(f).st_size
                            # checking the size of compressed folder
                            if int(size) in range(0, 100000000):
                                shutil.move(f, DOCUMENT_DEST)
                            elif int(size) in range(100000000, 700000000):
                                shutil.move(
                                    f, TUTORIALS_DEST)
                            else:
                                shutil.move(f, TVSERIES_DEST)

                        elif file_ext in documents:
                            try:
                                shutil.move(f, DOCUMENT_DEST)
                            except FileExistsError:
                                Filename_change(f)

                        elif file_ext in videos:
                            file_name = file_name.lower()
                            is_episode = any(sub in file_name.lower()
                                             for sub in tv_series)
                            if is_episode:
                                shutil.move(
                                    f, TVSERIES_DEST)

                            is_tutorial = any(
                                sub in file_name for sub in tutorials)
                            if is_tutorial:
                                shutil.move(
                                    f, TUTORIALS_DEST)
                            else:
                                size = os.stat(f).st_size
                                if int(size) in range(700000000, 9000000000):
                                    try:
                                        shutil.move(f, MOVIES_DEST)
                                    except FileExistsError:
                                        Filename_change(
                                            f, destination=MOVIES_DEST)
                                elif int(size) in range(100000000, 700000000):
                                    shutil.move(
                                        f, TVSERIES_DEST)
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
                                f, OTHERS)
                    except FileExistsError:
                        Filename_change(f, destination=OTHERS)
                    except shutil.Error:
                        pass
                    except Exception:
                        pass
                else:
                    try:
                        shutil.move(f, DOCUMENT_DEST)
                    except shutil.Error:
                        pass


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

executables = ['.apk', '.bat', '.com', '.exe', '.jar', '.wsf', '.msi']

pictures = ['.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg',
            '.png', '.ps', '.svg', '.tif', '.tiff', '.CR2']

tutorials = ['tutorial', 'course', 'how to', 'python', 'build',
             'crash', 'course', 'html', 'css', 'django', 'beginner']

tv_series = ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08']

documentary = ['documentary']

playlist = ['.zpl', '.xspf']

downloading = ['.crdownload', '.download', '.tmp']

folders_to_track = ["C:/Users/Feyton Inc/Downloads"]

event_handler = MyCleaner()
observer = Observer()
observer.schedule(event_handler, folders_to_track[0], recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()


