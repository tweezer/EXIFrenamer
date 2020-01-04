#!/usr/bin/python
import os, sys, subprocess
path = "/path/you/need/"
files = os.listdir(path)
for filename in files:
   print filename.find(".jpg")
   if ".jpg" in filename:
      fullfilename = path + filename
      exifreturn = subprocess.check_output("exiftool -Description " + fullfilename, shell=True)
      exifarray = exifreturn.split(":")
      newfilename = exifarray[1].strip() + ".jpg"
      os.rename(fullfilename,path + newfilename)
      print newfilename
