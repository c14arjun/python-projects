secret=13
print("you have 5 attempts to guess the number")
i=1
while i<=5:
    guess=int(input("Enter a number from 1-50: "))
    i=i+1
    if guess==secret:
        print("you won")
        i=i+4
    elif i==2:
        print("wrong,❤️❤️❤️❤️ left")
        if guess<13:
            print("guess is too low")
        else:
            print("guess is too high")
    elif i==3:
        print("wrong,❤️❤️️❤️ left")
        if guess<13:
            print("guess is too low")
        else:
            print("guess is too high")
    elif i==4:
        print("wrong,❤️❤️ left")
        if guess<13:
            print("guess is too low")
        else:
            print("guess is too high")
    elif i==5:
        print("wrong,❤️ left")
        if guess<13:
            print("guess is too low")
        else:
            print("guess is too high")
    else:
        print("game over")