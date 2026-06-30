import random
choices=("rock","paper","scissors")
user_choice=input("enter your choice rock paper or scissors: ")
computer_choice=random.choice(choices)
print(f"computer selected {computer_choice}")
print(f"User selected {user_choice}")
if computer_choice==user_choice:
    print("its a tie")
elif computer_choice=="rock" and user_choice=="paper":
    print("you won")
elif computer_choice=="rock" and user_choice=="scissors":
    print("you lost")
elif computer_choice=="paper" and user_choice=="rock":
    print("you lost")
elif computer_choice=="paper" and user_choice=="scissors":
    print("you won")
elif computer_choice=="scissors" and user_choice=="paper":
    print("you lost")
elif computer_choice=="scissors" and user_choice=="rock":
    print("you won")
else:
    print("Invalid choice")
