#Reading Data Interactively
cat hello.py
#!/usr/bin/env python3

name = input("Please enter your name: ")
print("Hello, " + name)

./hello.py 
Please enter your name: Roger
#Output will be Hello, Roger

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")

./seconds.py 
Welcome to this time converter
Enter the number of hours: 1
Enter the number of minutes: 2
Enter the number of seconds: 3

Do you want to do another conversion? [y to continue] y
Enter the number of hours: 3
Enter the number of minutes: 2
Enter the number of seconds: 1

Do you want to do another conversion? [y to continue] n

#Standard Streams
#Standard streams are the three main streams of data that a program can use to interact with the outside world (user).
cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z

#another ex:
cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z