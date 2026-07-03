try:
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))
    choice=input("Enter your choice +,-,*,/:")
    def add(a, b):
        return a+b
    def div(a, b):
        return a/b
    def mul(a, b):
        return a*b
    def sub(a, b):
        return a-b
    if choice=="+":
        print("addition of a and b is",add(num,num1))
    elif choice=="*":
        print("multiplication of a and b is",mul(num,num1))
    elif choice=="/":
        print("division of a and b is",div(num,num1))
    else:
        print("subtraction of a and b is",sub(num,num1))
except ValueError:
        print("Enter an actual number")
except ZeroDivisionError:
        print("Enter an actual number")