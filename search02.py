__author__ = 'igor.pochitalkin'
import os, sys, re, zipfile

file = "WPHARMA.EXE"
copie = "BACKUPDB.BIN"

def find_file(name, path):
    result = []
    counter = 0
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.normpath(root))
            f = open(name+".txt", "w")  # write path to file
            for paths in result:
                f.write(paths+ '\n')

find_file(file, "C:/")
find_file(copie, "C:/")

