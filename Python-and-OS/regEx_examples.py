log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

index = log.index("[")
print(log[index+1:index+6])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Here the re module is used which lets us use the search function to find regular expressions inside strings. Then, a regular expression is defined as:
r"\[(\d+)\]"

"""This regular expression matches a string enclosed in square brackets 
followed by one or more digits. Then, it uses the re.search() function 
to search the string log for a match to the regular expression. The 
re.search() function returns a Match object if a match is found, or None 
if no match is found. the re.search() function returns a Match object 
because the string log contains a match to the regular expression. """