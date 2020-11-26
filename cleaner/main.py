import csv
import os

origin = "C:/Users/Feyton Inc/Desktop/"

videos = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
          '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.webm']


movies_origin = "D:/Movies/"
videos_origin = "D:/Videos/"
tvseries_origin = "C:/Users/Feyton Inc/Videos/"
audio_origin = "C:/Users/Feyton Inc/Music/"
documentary_origin = "D:/DOCS/"
tutorials_origin = "C:/Users/Feyton Inc/Documents/Crack It/"


all_folders = [movies_origin, videos_origin, tvseries_origin,
               audio_origin, documentary_origin, tutorials_origin]


def with_movie_py(file, as_time=False):
    import datetime

    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(file)
    duration = clip.duration
    if as_time:
        video_time = str(datetime.timedelta(seconds=int(duration)))
        return video_time
    return duration


# for root, folders, f in os.walk(origin, topdown=False):
#     for fold in folders:
#         os.chdir(os.path.join(root, fold))
#         folder = os.listdir()
#         for file in folder:
#             name, ext = os.path.splitext(file)
#             if not os.path.isdir(file):
#                 info = os.stat(file)
#                 mode = info.st_mode
#                 size = info.st_size
#                 ino = info.st_ino
#                 # print(name)
#                 filename = os.path.join(root, fold, file)
#                 directory = os.path.dirname(os.path.abspath(file))
#                 if ext in videos:
#                     duration = with_movie_py(file, as_time=True)
#                 else:
#                     print('None')


def is_videos(file):
    name, ext = os.path.splitext(file)
    if ext in videos:
        return True
    return False


def collect_info():

    with open("files_info.csv", 'wb', newline='') as file:
        fields = ['name', 'extension', 'size', 'folder', 'length']
        writter = csv.DictWriter(file, fieldnames=fields)
        writter.writeheader()

        for f in all_folders:
            for root, folders, f in os.walk(f, topdown=False):
                for fold in folders:
                    os.chdir(os.path.join(root, fold))
                    folder = os.listdir()
                    for file in folder:
                        if not os.path.isdir(file):
                            info = os.stat(file)
                            mode = info.st_mode
                            size = info.st_size
                            ino = info.st_ino
                            name, ext = os.path.splitext(file)
                            directory = os.path.dirname(os.path.abspath(file))
                            directory = directory.split("\\")[-1]
                            if ext in videos:
                                duration = with_movie_py(file, as_time=True)
                            else:
                                duration = 0

                            writter.writerow(
                                {'name': name, 'extension': ext, 'size': size, 'folder': directory, 'length': duration})

    print("Done")


collect_info()
