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