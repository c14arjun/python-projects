medical_cause=input("do u have any medical_cause, yes or no: ")
attendance=int(input("enter your attendance: "))
if medical_cause=="yes":
    print("You are allowed to write the exam")
else:
    if attendance >= 75:
        print("You are allowed to write the exam")
    else:
        print("Sorry you are not eligible: ")