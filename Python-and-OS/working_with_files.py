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