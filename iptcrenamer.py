#!/usr/bin/python
import os, sys, subprocess
filecounter = 1
if len(sys.argv) > 1:
   path = sys.argv[1]
   files = os.scandir(path)
   for filename in files:
       if filename.is_file():
           if ".jpg" in filename.name:
             fullfilename = path + filename.name
             exifreturn = subprocess.run(["exiftool","-Description",fullfilename],capture_output=True,text=True).stdout
             exifarray = exifreturn.split(":")
             newfilename = exifarray[1].strip() + ".jpg"
             os.rename(fullfilename,path + newfilename)
             print("Renaming File #" + str(filecounter) + ": " + filename.name + " -> " + newfilename)
             filecounter += 1
else:
    path("Path is missing! Please start the script this way: iptcrenamer.py /path/to/your/files/")
    exit()
