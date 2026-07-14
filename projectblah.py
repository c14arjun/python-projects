lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
square_values = []
odd_squares = []
even_squares = []

for num in range(lower, upper + 1):
    square = num ** 2
    square_values.append(square)

    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print("Square values:", square_values)
print("Odd square values:", odd_squares)
print("Even square values:", even_squares)