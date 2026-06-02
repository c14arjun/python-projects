num=input("enter a number: ")

for i in range(1):
    for j in range(1):
        n=len(num)

        if n%2==0:
            print("Middle digits are:",num[n//2-1],"and",num[n//2])
        else:
            print("Middle digit is:",num[n//2])