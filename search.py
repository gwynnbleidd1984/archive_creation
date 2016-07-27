__author__ = 'igor.pochitalkin'
import os, sys, re, zipfile

path_exe = None  # wpharma.exe path
path_db = None  # DB directory path


def find_file(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root + "\DB"))
    # print (result)
    global path_exe
    path_exe = result
    return path_exe


def find_dir(name, path):
    result = []
    for root, dirs, files in os.walk(path, ):
        if name in dirs:
            result.append(os.path.join(root, name))
    # print (result)
    global path_db
    path_db = result
    return path_db

find_file("WPHARMA.EXE", "C:/")  # search for wpharma.exe file
f = open("executable.txt", "w")  # write path to file
for path in path_exe:
    # path = re.sub(r"\"", "/", path)
    f.write(path + '\n')
f.close()

find_dir("COPIE_DB", "C:/")  # search for DB directory
f = open("db_path.txt", "w")  # write path to file
for path in path_db:
    f.write(path + '\n')
f.close()
