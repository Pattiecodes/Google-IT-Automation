Files included in this module:
- reading_and_writing_files.py
- working_with_files.py

Module Notes for Module 2

- The OS is structured with a tree structure, called "directories" or folders. These contain directories,
and files that are used in the computer.
- The root directory is the top of the tree, and is called the "root directory". And the path back to the home
is called the "absolute path".
![absolute path](<pngs/Screenshot (442).png>)

-- File Descriptor --
- A file descriptor is a unique number that is assigned to a file.
![File Descriptor](<pngs/Screenshot (453).png>)
- uses readline/read method to read the file.
![readline method](<pngs/Screenshot (454).png>)
![read method](<pngs/Screenshot (456).png>)

- Always close files when you open them:
![open-close method](<pngs/Screenshot (457).png>)
- With block syntax, automatically closes the file.
![with method in opening file](<pngs/Screenshot (458).png>)

- Word of Caution:
-- Readline and read are useful methods, but reading them into a variable might be dangerous if the file is large.

-- Modes --
- Modes are similar to a file permission.
- r = read - The default mode
- w = write
- a = append
- r+ = read and write
- w+ = append and write
![Write mode](<pngs/Screenshot (469).png>)

-- Reading and Writing on Files with Python --
Relative File path
- ![Relative File Path](<pngs/Screenshot (497).png>)
- Usually preferred by programmers for its flexibility.
- ![File Paths](<pngs/Screenshot (501).png>)

File Paths are different from each OS:
![Windows vs Mac/Linux File Paths](<pngs/Screenshot (503).png>)
- Often times, you need to have a double back-slash in using backslashes,
as backslashes is a special character in Python.
![Double Backslasj](<pngs/Screenshot (509).png>)

CWD Commands for File Paths:
![usual CWD Command](<Screenshot (512).png>)
![CWD for External Commands](<pngs/Screenshot (513).png>)

- Oftentimes, in automation. You'll have to write on text file, and
the outputs be saved somewhere. An example of using relative file path:
![RElative File Path Saved](<pngs/Screenshot (514).png>)
![Relative File Path Example](<pngs/Screenshot (515).png>)

NOTE IN FILE PATHS:
![Important in File Paths](<pngs/Screenshot (516).png>)
![Reminder for File Paths](<pngs/Screenshot (518).png>)
Things to keep in mind  
One thing to be aware of is that Python treats text and binary files differently. Because Python is cross-platform, it tries to automatically handle different ASCII line endings. If you’re processing a binary file, make sure to open it in binary mode so Python doesn’t try to “fix” newlines in a binary file.

A best practice is to always close() a file when you’re done reading or writing to it. Even though Python usually closes them for you, it’s a good signal to other people reading your code that you’re done with that file. Make sure to catch any potential errors from filesystem calls, such as permission denied, file not found, and so on. Generally, you wrap them in try/except to handle those errors.


Working with CSV files
Parsing:
![Parsing](<pngs/Screenshot (532).png>)


Module Note:
Module 2 - Qwiklabs Asessment: Handling Files is not yet accomplished.