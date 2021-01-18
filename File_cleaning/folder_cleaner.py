import os
import random
import shutil
import stat


def check_if_folder_is_empty(path):
    os.chdir(path)
    directory = os.listdir()
    if len(directory) == 0:
        return True
    return False


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def delete_empty_folders(directory):
    for root, folders, files in os.walk(directory, topdown=False):
        for fold in folders:
            p = os.path.join(root, fold)
            if os.path.isdir(p):
                print(p)
                try:
                    os.rmdir(p)
                except OSError:
                    pass


def list_files_in_folder(directory):
    x = 1
    for root, folders, files in os.walk(directory, topdown=False):
        for fil in files:
            p = os.path.join(root, fil)
            if not os.path.isdir(p):
                x += 1
                print("%s. %s" % (x, p))


def dare_cleaner(directory, force=False):
    if not force:
        try:
            shutil.rmtree(directory)
        except Exception:
            pass
    else:
        try:
            shutil.rmtree(directory, onerror=remove_readonly)
        except Exception:
            pass


def handle_existing_files(fil):
    name, ext = os.path.splitext(fil)
    new_name = "%s-%s%s" % (name, random.randint(2, 100), ext)
    try:
        os.rename(fil, new_name)
        return new_name
    except FileExistsError:
        return None
