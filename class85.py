print("select your ride: ")
print("1.bike")
print("2.car")
choice_of_ride=int(input("enter your choice, 1 or 2: "))
if choice_of_ride==1:
    print("you have selected bike")
    print("select your bike: ")
    print("a.Activa")
    print("b.Motorcycle")
    choice_of_bike=input("enter your choice a or b: ")
    if choice_of_bike=="a":
        print("you have selected Activa")
    else:
        print("you have selected a Motorcycle")
else:
    print("you have selected car")
    print("select your car: ")
    print("a.SUV")
    print("b.Sedan")
    choice_of_car=input("enter your choice a or b: ")
    if choice_of_car=="a":
        print("you have selected SUV")
    else:
        print("you have selected a Sedan")

