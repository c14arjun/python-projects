count = int(input("How many numbers do you want to convert? "))

for i in range(count):
    num = float(input("Enter a decimal number (0-1): "))

    binary = "0."

    while num > 0 and len(binary) < 18:  
        num *=2

        if num >= 1:
            binary += "1"
            num -= 1
        else:
            binary += "0"

    print("Binary:", binary)