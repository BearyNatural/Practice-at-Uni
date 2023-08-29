# Write a program that will take two inputs from user and print out the odd number

# try-except is being used to handle potential input errors, this is same if-else condition

# Function to check if a number is odd
def is_odd(n):
    return n % 2 != 0

try:
    # Request 2 separate inputs from user
    a = int(input("Enter 1st number: \n"))
    b = int(input("Enter 2nd number: \n"))

    # Check and print odd numbers
    if is_odd(a):
        print(f"{a} is an odd number.")
    else:
        print(f"{a} is not an odd number.")

    if is_odd(b):
        print(f"{b} is an odd number.")
    else:
        print(f"{b} is not an odd number.")

except ValueError:
    print("Please enter valid integers.")

# test:
# print(type(n))
# print()