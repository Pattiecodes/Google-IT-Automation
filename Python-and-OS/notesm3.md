Relevant Files for Module 3:
- notesm3_programs.py


--- Notes Start Here ---
Regular Expressions:
Regular expressions (or RegEx) are a way to describe a pattern of characters.
![RegEx](<Screenshot (580).png>)

Grep Function
![grep function in terminal](<Screenshot (593).png>)
![grep function in terminal - results](<Screenshot (594).png>)
- grep is a case-sensitive search command. Hence, we use the -i flag to make it case-insensitive.
![-i in grep](<Screenshot (597).png>)
-- Reserved Characters in grep
- dot (.) - can be used as an alternative to a character
![dot character](<Screenshot (599).png>)
- caret (^) - can be used to find characters/words in front of a line
![caret character](<Screenshot (602).png>)
- dollar sign ($) - can be used to find characters/words at the end of a line.
![dollar sign](<Screenshot (603).png>)

Regular Expressions Uses:
![RegEx_uses](<Screenshot (633).png>)
- Always use raw strings for regular expressions:
![RawString in RegEx](<Screenshot (632).png>)

Escape Characters:
 Escape Characters are used to escape special characters.
 Examples:
 \w - matches any word character
 \W - matches any non-word character
 \d - matches any digit
 \D - matches any non-digit
 \s - matches any whitespace character
 \S - matches any non-whitespace character
 \b - matches the beginning or end of a word
 \B - matches any character that is not the beginning or end of a word
 \A - matches the beginning of a string
 \Z - matches the end of a string
 \n - matches a newline character
 (regex101.com)

Capturing Groups
![Capturing Groups](<Screenshot (721).png>)