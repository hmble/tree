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

if len(sys.argv) > 1:
    directory = sys.argv[1]
    print(directory)
else:
    print(os.getcwd())

tree = Tree()
tree.walk(directory)

print("\ndirectories " + str(tree.dircount) + ", files " + str(tree.filecount))

