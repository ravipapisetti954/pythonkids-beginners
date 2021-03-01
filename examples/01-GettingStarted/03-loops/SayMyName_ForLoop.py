# SayMyName_ForLoops.py - print user name repeatatively
 
# Ask the user for their name
name = input("What is your name? ")

# Print their name n times
n = eval(input("How many number of times name to be printed?"))

for x in range(n):
    # Print their name followed by a space, not a new line
    print(name, end = " ")
