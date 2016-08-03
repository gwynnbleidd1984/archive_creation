__author__ = 'igor.pochitalkin'
import os, zipfile, math, time

arch_name = "db_install_" + time.strftime("%Y%m%d" "_" "%H%M")  #backup archive name
file = "WPHARMA.EXE"                                            #search for a winpharma directory
copie = "BACKUPDB.BIN"                                          #search for a backup directory

def find_dir(name, path):
    result = None                                               #directory
    timer = 0                                                   #directory choosing criteria(by usage time)
    for root, dirs, files in os.walk(path):
        if name in files:
            lastcall = math.trunc(os.path.getatime(root))       #last file usage time (unixtime)
            if timer < lastcall:
                timer = lastcall
                result = os.path.normpath(root)                 #path to directory containing file
    return  result

to_save = (find_dir(file, "C:/") + "\DB")
print(to_save)

saving_place = (find_dir(copie, "C:/"))
print(saving_place)

