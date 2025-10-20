# multiplication_table.copy()

# Prompt user for a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

except ValueError:
    print("Please enter a valid integer.")
