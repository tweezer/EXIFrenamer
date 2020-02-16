# EXIFrenamer
I was searching for a tool to rename a lots of JPEG files on my Mac with Data from EXIF/IPTC Metadata. There have been a lots of tools, but no one was the solution I needed. So I took some time to write this small script in Python to do the job. It's my _first script_ I've done with Python. So there will be lots of optimization done with every new version of the script. I think it's the best way to learn a new lanuage. Solve a real "problem" with the code of a new language.

It has been written on a Mac (macOS 10.14), but I think it should work on other Unix, BSD and Linux too. I think this version does not work on Windows PCs. Keep in mind to install the cmdtool "exiftool", without my script wont work. On Mac you can easily install it with homebrew!



## Version 0.3 (2020-01-07)
This version of the script will do two checks before renaming the file. First it will check if there is any EXIF/IPTC data returned. If not, the script will skip the file. On the other side the script will check if a renamed file aready exists. If yes it will give it another name. Cause I'm not that happy with the code, I'll do some optimizations with the release 0.3.1.

## Version 0.2.1 (2020-01-05)
I was using os.scandir() in the wrong way. With the help over Mastodon (Social Network) I was able to fix it. Now the script is running. So I can focus on new features again!

## Version 0.2 (2020-01-05)
I've changed a lot in the script. First now it's fully written in Python 3 (min 3.6 needed!) and does not have any Python 2 Code anymore. Second thing is, I've made the script more variable. You can now pass the needed path as a parameter when calling the script. And I've added some output too, so you can see what the script is doing.

## Version 0.1 (2020-01-04)
very basic version of the script for a very special usecase. But I will add some more feature in future versions of the script
