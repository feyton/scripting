import os
import re


def clean_string(string):
    string = str(string.replace(".", ' ').strip())
    if 'watch' in string.lower():
        string = string.lower().replace('watch', '').title()
    if '_' in string:
        string = string.replace("_", " ").strip()
    match = re.match(r'.*([1-3][0-9]{3})', string)
    if match:
        year = match.group(1)
        string = string.split(year)[0].strip()

    return string.title()


origin = "C:/Users/Feyton Inc/Desktop/"

substrings = ['season', 'episode', 'saison']


def clean_no_season(name):
    string = str(clean_string(name))
    match1 = re.match('.*ep([0-9]{1})', string.lower())
    match2 = re.match(r'.*(saison [0-9]{1})', string.lower())

    if match1 and not match2:
        episode = str(match1.group(1))
        episode_name = "S01E%s" % episode.upper()
        new_name = string.lower().replace(
            episode, episode_name).replace('episode ', '').strip()

        return new_name.title()

    elif match1 and match2:
        season = match2.group(1)
        episode = match1.group(1)
        new_name = string.lower().replace(season, "S0%s" % season.strip()).replace(
            'saison ', '').replace(episode, "E0%s" % episode.strip()).strip().replace('ep', '')
        return new_name.title()


videos = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
          '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.webm', '.srt']

for root, folders, files in os.walk(origin, topdown=False):
    for fold in folders:
        os.chdir(os.path.join(root, fold))
        folder = os.listdir()
        for fil in folder:
            name, ext = os.path.splitext(fil)
            if ext in videos:

                s_name = clean_no_season(name)
                if s_name:
                    new_name = "%s%s" % (s_name, ext)
                    print(new_name)
                    os.rename(fil, new_name)
