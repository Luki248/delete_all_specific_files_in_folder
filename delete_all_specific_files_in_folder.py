#!/usr/bin/env python3

# delete_all_specific_files_in_folder.py

import os
import argparse

import del_spec_file

VERSION = "1.0"

arg_parser = argparse.ArgumentParser(prog="delete_all_specific_files_in_folder",
                                     description="Delete specific Files in a Folder and returns the number of the deleted items.")
arg_parser.version = VERSION

arg_parser.add_argument("Path",
                        metavar="path",
                        type=str,
                        help="the path to work with")

arg_parser.add_argument("Filename",
                        metavar="filename",
                        type=str,
                        help="the name of the File to be deleted")

arg_parser.add_argument("-v",
                        "--version",
                        action="version",
                        help="show the version of the program")

args = arg_parser.parse_args()

folderpath = args.Path
filename = args.Filename

if not os.path.isdir(folderpath):
    print("The path specified does not exist!")
    exit()

ret = del_spec_file.del_spec_file(folderpath, filename)
print("Deleted " + str(ret) + " folder(s)")
