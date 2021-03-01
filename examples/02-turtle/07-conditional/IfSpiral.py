answer = input("Do you want to set a spiral? y/n: ")

if answer == 'y':
    print("Working ....")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(10):
        t.forward(x*2)
        t.left(89)

print("Okay, we'rse donet!")