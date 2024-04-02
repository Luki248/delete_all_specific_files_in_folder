#!/usr/bin/env python3

# del_spec_filetype.py

import os


def del_spec_filetype(path, filetype):
    """deletes specific filetypes recursively
        Args:
            path (str): folder to work with
            filetype (str): filetype to delete (mp3)
        Returns:
            integer: the number of deleted file(s)
    """
    count_del_files = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                full_path = os.path.join(path, entry.name)
                count_del_files += del_spec_filetype(full_path, filetype)
            elif entry.is_file():
                extension = entry.name.split(".")[-1]
                if extension == filetype:
                    try:
                        os.remove(entry.path)
                    except:
                        print("Could not delete \"" + entry.path + "\"")
                    else:
                        count_del_files += 1
                        print("Deleted \"" + entry.path + "\"")
    return count_del_files


if __name__ == "__main__":
    path = input("Path to work with: ")

    if not os.path.isdir(path):
        print("The path specified does not exist!")
        exit()

    filetype = input("Filetype (Extension) to delete (without dot): ")

    if len(filetype) == 0:
        print("Give a correct Extension!")
        exit()

    ret = del_spec_filetype(path, filetype)
    print("Deleted " + str(ret) + " file(s)")
