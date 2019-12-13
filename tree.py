import os
import sys
from collections import OrderedDict


class Tree:
    def __init__(self):
        self.dircount = 0
        self.filecount = 0
        self.dict_dir = []
        self.dict_file = []
        self.ignore = [".git", "AW_Dribble"]

    def walk(self, path, prefix=""):

        for entry in os.scandir(path):

            if entry.is_dir():
                self.dircount += 1
                print(prefix + "|-- " + entry.name)
                newstr = prefix + "|   "
                self.walk(entry.path, newstr)
            else:
                self.filecount += 1
                print(prefix + "|-- " + entry.name)

    def sorted_walk(self, path, prefix=""):

        dirlist = OrderedDict()
        filelist = []

        for entry in os.scandir(path):

            if entry.is_dir():
                self.dircount += 1
                dirlist[entry.name] = entry.path
            else:
                self.filecount += 1
                filelist.append(entry.name)

        fl = sorted(filelist)
        for file in fl:

            if file != fl[-1]:
                print(prefix + "|-- " + file)
            else:
                print(prefix + "`-- " + file)

        lt = (list(dirlist.keys()))
        for key in dirlist.keys():
            if (key in self.ignore):
                continue
            elif key != lt[-1]:
                print(prefix + "|-- " + key)
                newstr = prefix + "|   "
                self.sorted_walk(dirlist[key], newstr)
            else:
                print(prefix + "`-- " + key)
                newstr = prefix + "|   "
                self.sorted_walk(dirlist[key], newstr)


directory = "."
# FIXME :
# when arguments passed with / at end `os.path.basename(path)
# prints nothings as basename is an empty string e.g. home/dir/
#
# TODO : Options to follow symlinks or not
# Currently no method for symlinks
<<<<<<< HEAD

=======
>>>>>>> bc95c58b7de986daa63819ca01f2d7af9ea4b656

if len(sys.argv) > 1:
    directory = sys.argv[1]
    print(directory)
else:
    print(os.getcwd())

tree = Tree()
# tree.walk(directory)
tree.sorted_walk(directory)
#print("\ndirectories " + str(tree.dircount) + ", files " + str(tree.filecount))
