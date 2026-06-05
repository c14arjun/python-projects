rows=int(input("Enter a number: "))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
        j=j+1
    print()
    i=i+1
        