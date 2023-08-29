# Build a calculator that will take two user input and ask user if they want the program to perform addition, subtraction, multiplication, or division. Based on the user’s choice print the results in the console

# try-except is being used to handle potential input errors, this is same if-else condition

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

try:
    # Request two numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display menu and request operation choice from user
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("\nEnter choice (1/2/3/4): ")

    # Based on user choice, perform operation and display result
    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter valid numbers.")

# test:
# print(type(n))
# print()