# Removes novel.txt
import os
os.remove("novel.txt")

#Removing it again will throw an error. As file does not exist.
os.remove("novel.txt")

#Renaming a file. 
os.rename("first_draft.txt", "finished_masterpiece.txt")

#Checks if file exists
os.path.exists("finished_masterpiece.txt")
os.path.exists("userlist.txt") 

"""Directories"""

print(os.getcwd())
#This code snippet returns the current working directory.

os.mkdir("new_dir")
#The os.mkdir("new_dir") function creates a new directory called new_dir

os.chdir("new_dir")
os.getcwd()
#This code snippet changes the current working directory to new_dir. 
#The second line prints the current working directory.

os.mkdir("newer_dir")
os.rmdir("newer_dir")
#This code snippet creates a new directory called newer_dir. 
#The second line deletes the newer_dir directory.

import os
os.listdir("website")
#This code snippet returns a list of all the files and 
#sub-directories in the website directory.

dir = "website"
for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
     else:
        print("{} is a file".format(fullname))

