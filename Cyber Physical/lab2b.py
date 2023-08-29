# write a program that will take input from user and compare two numbers if they are smaller, bigger or equal

# try-except is being used to handle potential input errors, this is same if-else condition
try:
    # Request 2 separate inputs from user
    a = float(input("Enter 1st number: \n"))
    b = float(input("Enter 2nd number: \n"))

    # Compare the numbers and print the result
    if a > b:
        print(f"{a} is bigger than {b}.")
    elif a < b:
        print(f"{a} is smaller than {b}.")
    else:
        print(f"{a} is equal to {b}.")

except ValueError:
    print("Please enter valid numbers.")

# test:
# print(list)
# print()

