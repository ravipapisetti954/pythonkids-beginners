import random

suits = ["clubs", "diamonds", "hearts", "spades"]

faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "jack", "queen", "king", "ace"]

keep_going = True

while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)

    your_face = random.choice(faces)
    your_suit = random.choice(suits)

    print("I have the ", my_face, "of ", my_suit)
    print("You have the ", your_face, "of ", your_suit)

    if faces.index(my_face) > faces.index(your_face):
        print("I WIN")
    elif faces.index(my_face) < faces.index(your_face):
        print("You WIN")
    else:
        print("It's a tie")

    answer = input("Hie[Enter] to keep going, any key to exit: ")
    keep_going = (answer == "") 
