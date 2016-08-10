__author__ = 'igor.pochitalkin'
import os, zipfile, math, time

arch_name = "db_install_" + time.strftime("%Y%m%d" "_" "%H%M")  #backup archive name
file = "WPHARMA.EXE"                                            #winpharma directory
copie = "BACKUPDB.BIN"                                          #backup directory

def find_dir(name, path):                                       #searching directory
    result = None                                               #directory
    timer = 0                                                   #directory choosing criteria(by usage time)
    for root, dirs, files in os.walk(path):
        if name in files:
            lastcall = math.trunc(os.path.getatime(root))       #last file usage time (unixtime)
            if timer < lastcall:
                timer = lastcall
                result = os.path.normpath(root)                 #path to directory containing file
                #print(lastcall, result)
    return  result

to_save = (find_dir(file, "C:/") + "\DB")                       #finding last used wpharma.exe file
#print(to_save)

saving_place = (find_dir(copie, "C:/"))                         #finding last used copie_db folder
#print(saving_place)

arch_fullpath = saving_place + "\\" + arch_name + ".zip"
#print(arch_fullpath)

arch = zipfile.ZipFile(arch_fullpath, "w")
for files in os.listdir(to_save):
    arch.write(os.path.join(to_save, files))
arch.close()