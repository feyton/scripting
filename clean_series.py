import os
import re
import sys
from os import makedirs

ORIGIN = "C:/Users/Feyton Inc/Desktop/"
DEST = "C:/Users/Feyton Inc/Videos/"


def clean_string(string):
    string = str(string)
    string = string.replace(".", ' ').strip()
    if '_' in string:
        string = string.replace("_", " ").strip()
    match = re.match(r'.*([1-3][0-9]{3})', string)
    if match:
        year = match.group(1)
        string = string.split(year)[0].strip()
    if "  " in string:
        string = string.replace("  ", "")
    return string.title()


def is_serie(name):
    match = re.match(r'.*(s[0-9]{2}e[0-9]{2})', name.lower())
    if match:
        return match.group(1)
    return None


def get_season_and_episode(serie):
    return [serie[0:3], serie[3:]]


def get_serie_name(file_name):
    s = is_serie(file_name)
    name = file_name.lower().split(s)[0]
    name = clean_string(name)
    sea = get_season_and_episode(s)[0]
    return "%s/%s" % (name, sea.upper())


def get_or_create_folders(name):
    folder = os.path.join(DEST, name)
    exist = os.path.isdir(folder)
    if exist:
        pass
    else:
        makedirs(folder)


def episode_destination(episode):
    name = get_serie_name(episode)
    destination = os.path.join(DEST, name)
    return "%s/" % destination


def get_new_episode_name(old_name):
    s = is_serie(old_name)
    name = old_name.lower().split(s)[0]
    name = clean_string(name)
    sea = get_season_and_episode(s)
    new_name = "%s %s%s" % (name, sea[0].upper(), sea[1].upper())
    dest = episode_destination(old_name)
    return "%s%s" % (dest, new_name)


def rename_episode(episode, new_name):
    name = "%s%s" % (episode, new_name)
    print(name)


def clean_other_season(name):
    if 'season' in name.lower():
        new_name = name.replace('season', 'S')
        num = re.match(r'.*')


print("####################################")
print("\nThe series in this folder \nwill be moved to their respective folders\n")
print("####################################")

process = input("\nTo proceed press enter '1' else type in other character\n")
if not process == "1":
    print("Sad to see you go...")
    sys.exit()
for root, folders, files in os.walk(ORIGIN):
    for fold in folders:
        os.chdir(os.path.join(root, fold))
        folder = os.listdir()
        for file in folder:
            name, ext = os.path.splitext(file)
            if ext != '':
                serie = is_serie(name)
                if serie:
                    episode = get_season_and_episode(serie)
                    serie_name = get_serie_name(name)
                    get_or_create_folders(serie_name)
                    new_name = "%s%s" % (get_new_episode_name(name), ext)
                    # dest = episode_destination(name)
                    try:
                        os.rename(file, new_name)
                    except FileExistsError:
                        pass
                else:
                    pass
            else:
                pass

print("Done....")
print("Thank you for using this tool!!")
