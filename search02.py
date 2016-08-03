import time, zipfile, shutil
a = "db_install_" + time.strftime("%Y%m%d" "_" "%H%M")

print(a)

#f = open(a+".txt", "w")  # write path to file
#f.write(a)

myarchive = zipfile.ZipFile("archivename.zip", "w")
myarchive.write("C:\COPIE_DB", a +".txt", zipfile.ZIP_DEFLATED)