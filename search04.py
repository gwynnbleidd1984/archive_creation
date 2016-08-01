__author__ = 'igor.pochitalkin'

import os, sys, zipfile, math

file = "WPHARMA.EXE"
copie = "BACKUPDB.BIN"


def find_file(name, path):
    result = []
    timer = 0
    for root, dirs, files in os.walk(path):
        if name in files:
            if os.path.getatime(root):
                lastcall = math.trunc(os.path.getatime(root))
                if lastcall > timer:
                    timer = lastcall
            print(timer)

                    #print(os.path.normpath(root), lastcall)

            """result.append(os.path.normpath(root))
            f = open(name+".txt", "w")  # write path to file
            for paths in result:
                f.write(paths+ '\n')"""


find_file(file, "C:/")
# find_file(copie, "C:/")