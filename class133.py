def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
num=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
choose=int(input("Enter your choice: "))
if choose==1:
    print(add(num,num2))
if choose==2:
    print(sub(num,num2))
if choose==3:
    print(mul(num,num2))
if choose==4:
    print(div(num,num2))
