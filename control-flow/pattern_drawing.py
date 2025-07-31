# pattern_drawing.py

# Ask the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line
            row += 1

except ValueError:
    print("Invalid input. Please enter a valid integer.")
