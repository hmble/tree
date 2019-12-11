import os
import sys

class Tree:

    def __init__(self):
        self.dircount = 0
        self.filecount = 0

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


directory = "."
# FIXME :
# when arguments passed with / at end `os.path.basename(path)
# prints nothings as basename is an empty string e.g. home/dir/
#
# TODO : Options to follow symlinks or not
# Currently no method for symlinks

if len(sys.argv) > 1:
    directory = sys.argv[1]
    print(directory)
else:
    print(os.getcwd())

tree = Tree()
tree.walk(directory)

print("\ndirectories " + str(tree.dircount) + ", files " + str(tree.filecount))

