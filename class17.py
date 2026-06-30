import random
computer_choice=random.randint(1,10)
while True:
    guess=int(input("enter your guess: "))
    if guess==computer_choice:
        print("you guessed it and the computer choice was",computer_choice)
        break
    elif computer_choice>guess:
        print("guess is higher")
    elif computer_choice<guess:
        print("guess is lower") 
    else:
        print("error")