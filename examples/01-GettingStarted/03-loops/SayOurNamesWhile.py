# SayYourNames.py

# Ask the user for their name
name = input("what is your name? ")

# Keep printing names until we want to quit

while name != "":
    #Print their name 100 times
    for x in range(100):
        print(name, end =  " ")

    print()

    name = input("Type another name, or just hit enter to quit:")

print("Game completed..")
