# Pythom program my_first_calculator.py

# This function adds two numbers
def add(x,y):
    return x + y

#This function subtracts two numbers
def subtract(x,y):
    return x - y

#This function multiplies two numbers 
def multiply(x,y):
    return x * y

#This funtion divides two numbers
def divide(x,y):
    return x / y


print("Welcome to this calculator! Please choose an operation ")
print(a. Addition)
print(b. Subtract)
print(c. Multiplication)
print(d. Division)

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four operations
    if choice in ('a', 'b', 'c', 'd'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if choice == 'a':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 'b':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 'c':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 'd':
        print(num1, "/", num2, "=", divide(num1, num2))

    # check if user wants another calculation
    #break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Invalid Input")

print("Thanks for using this calculator, goodbye :)")
