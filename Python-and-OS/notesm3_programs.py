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

#Escaping Characters
import re
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

import re
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

#Regular Expressions in Action
import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

# Capturing Groups
import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")

#Repetition Qualifiers Review
import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

import re
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

import re
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

import re
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

import re
print(re.findall(r"\w{5,10}", "I really like strawberries"))

import re
print(re.findall(r"\w{5,}", "I really like strawberries"))

import re
print(re.search(r"s\w{,20}", "I really like strawberries"))

#Extracting a PID using RegEx
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
print(result[1])
#Note that this print command results in an error as shown in the video. 

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

#Splitting and Replacing
import re
re.split(r"[.?!]", "One sentence. Another one? And the last one!")

import re
re.split(r"([.?!])", "One sentence. Another one? And the last one!")

import re
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

import re
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

