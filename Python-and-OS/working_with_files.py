# Removes novel.txt
import os
os.remove("novel.txt")
os.remove("novel.txt")

#Throws an error as this file does not exist.
os.rename("first_draft.txt", "finished_masterpiece.txt")

#Renaming a file. 
os.path.exists("finished_masterpiece.txt")
os.path.exists("userlist.txt")