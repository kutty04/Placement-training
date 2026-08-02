def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


a = read_int("Enter first number: ")
# Read second number
b = read_int("Enter second number: ")

if a > b:
    print("First number is biggest")
elif b > a:
    print("Second number is biggest")
else:
    print("Both numbers are equal")
