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