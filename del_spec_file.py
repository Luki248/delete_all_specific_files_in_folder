#!/usr/bin/env python3

# del_spec_file.py

import os


def del_spec_file(path, filename):
    """deletes specific files recursively
        Args:
            path (str): folder to work with
            filename (str): file(s) to delete
        Returns:
            integer: the number of deleted file(s)
    """
    count_del_files = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                full_path = os.path.join(path, entry.name)
                count_del_files += del_spec_file(full_path, filename)
            elif entry.is_file():
                if entry.name == filename:
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

    filename = input("Filename to delete (with extension): ")

    ret = del_spec_file(path, filename)
    print("Deleted " + str(ret) + " file(s)")
