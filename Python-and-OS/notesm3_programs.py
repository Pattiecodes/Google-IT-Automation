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

#Simple Matching in Python
import re
result = re.search(r"aza", "plaza")
print(result)

import re
result = re.search(r"aza", "bazaar")
print(result)

import re
result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))


#WildCards and Character Classes
import re
print(re.search(r"[Pp]ython", "Python"))

import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

#Repetition Qualifiers
import re
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

import re
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

import re
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))