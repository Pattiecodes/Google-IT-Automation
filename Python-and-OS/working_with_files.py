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

# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)


# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)

#PathLib
# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)


"""CSV FILES"""
# Reading CSV Files
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

#Generating your own CSV File
import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
    
#Reading and Writing CSV Files with dictionaries:
#the following command should be used in the terminal
cat software.csv 
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))
      
#Another Example of Reading and Writing CSV Files with dictionaries:
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


#the following command should be used in the terminal
cat by_department.csv  