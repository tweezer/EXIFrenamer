#!/usr/bin/python
import os, sys, subprocess, pathlib
filecounter = 1
if len(sys.argv) > 1:
   path = sys.argv[1]
   filebuffer = []
   for files in os.scandir(path):
       if files.is_file() and files.name.endswith('.jpg'):
          filebuffer.append(files.name)
   for filename in filebuffer:
       fullfilename = path + filename
       exifreturn = subprocess.run(["exiftool","-Description",fullfilename],capture_output=True,text=True).stdout
       exifarray = exifreturn.split(":")
       newfilename = exifarray[1].strip() + ".jpg"
       newfilecheck = pathlib.Path(path + newfilename)
       if len(newfilename) >= 5:
           if newfilecheck.is_file():
               os.rename(fullfilename, path + "copy_" + str(filecounter) + “_” + newfilename)
               print("Renaming File #" + str(filecounter) + ": " + filename + " -> copy_" + str(filecounter) + "_" + newfilename)
           else:
               os.rename(fullfilename,path + newfilename)
               print("Renaming File #" + str(filecounter) + ": " + filename + " -> " + newfilename)
       else:
          print ("File #" + str(filecounter) + " " + filename + ": has empty EXIF/IPTC Data - skipping")
       filecounter += 1
else:
    path("Path is missing! Please start the script this way: iptcrenamer.py /path/to/your/files/")
    exit()
