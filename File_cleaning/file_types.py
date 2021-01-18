import os

# from series_cleaner import is_serie

audio = ['.aif', '.cda', '.mid', '.midi', '.mp3',
         '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.m3u']
documents = ['.txt', '.doc', '.docx', '.odt', '.pdf',
             '.rtf', '.tex', '.wks', '.wps', '.wpd', '.key', '.odp', '.pps',
             '.ppt', '.pptx', '.ods', '.xlr', '.xls', '.xlsx', '.csv']

design = ['.xd', '.psd', '.html', '.css', '.otf', '.fnt', '.ttf']
videos = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
          '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.webm', '.srt']
compressed = ['.7z', '.arj', '.deb', '.pkg',
              '.rar', '.rpm', '.tar.gz', '.z', '.zip']

executables = ['.apk', '.bat', '.com', '.exe',
               '.jar', '.wsf', '.msi', '.py', '.bat', '.iso', '.bin']

pictures = ['.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg',
            '.png', '.ps', '.svg', '.tif', '.tiff', '.cr2', '.JPG']
playlist = ['.zpl', '.xspf']
downloading = ['.crdownload', '.download', '.tmp']

# **********************


# Substrings to check against to identify different categories of the file
tutorials = ['tutorial', 'course', 'how to', 'python', 'build',
             'crash', 'course', 'html', 'css', 'django', 'beginner']

tv_series = ['s01', 's02', 's03', 's04', 's05', 's06', 's07']
documentary = ['documentary', '15 ', 'artificial', 'last week']


def get_file_type(fil, size):
    name, ext1 = os.path.splitext(fil)
    name = str(name)
    ext = str(ext1)
    if ext.lower() in executables:
        return ["Soft", "Soft"]

    elif ext.lower() in audio:
        return ["Music", "Music"]

    elif ext.lower() in compressed:
        # checking the size of compressed folder
        if int(size) in range(0, 100000000):
            return ["Documents", "Compresed"]
        else:
            return ["Compressed", "Compressed"]

    elif ext.lower() in documents:
        return ["Documents", "Documents"]

    elif ext.lower() in videos:
        Tv_series_check = any(sub in name.lower()
                              for sub in tv_series)
        Documentary_check = any(sub in name.lower()
                                for sub in documentary)
        Tutorial_check = any(sub in name.lower()
                             for sub in tutorials)

        if Tv_series_check:
            return ["Videos", "TV SERIES"]
        elif Documentary_check:
            return ["Videos", "DOCS"]

        elif Tutorial_check:
            return ["Videos", "Tutorials"]

        elif int(size) in range(700000000, 9000000000):
            return ["Videos", "MOVIES"]

        else:
            return ["Videos", "Videos"]
    elif ext.lower() in pictures:
        return ["Pictures", "Pictures"]

    elif ext.lower() in playlist:
        return ["Music", "Playlist"]
    elif ext.lower() in design:
        return ["Pictures", "Design"]
    elif ext.lower() in downloading:
        return ["Downloads", "Downloads"]
    else:
        return ["Others", "Others"]
