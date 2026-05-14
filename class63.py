print("marks obtained in 5 differnet subjects: ")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot/5)

validRange = range(0,101)

if avg not in validRange:
    print("Invalid Input!")

elif avg in range (91,101):
    print("your grade is a1")
elif avg in range (81,91):
    print("your grade is a2")
elif avg in range (71,81):
    print("your grade is b1")
elif avg in range (61,71):
    print("your grade is b2")
elif avg in range (51,61):
    print("your grade is c1")
elif avg in range (41,51):
    print("your grade is c2")
elif avg in range (33,41):
    print("your grade is d1")
elif avg in range (21,33):
    print("your grade is e1")
elif avg in range (0,21):
    print("your grade is e2")