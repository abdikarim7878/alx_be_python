# pattern_drawing.py

# Ask user to input pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to print stars in a row
    for col in range(size):
        print("*", end="")
    print()  # New line after each row
    row += 1
