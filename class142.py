def cube(a):
    return a**3
def division(a):
    if a%3==0:
        return cube(a)
    else:
        print("not divisible")
num=int(input("Enter a number: "))
print(division(num))