# Write a program that will take two inputs from user and print out the even number

# try-except is being used to handle potential input errors, this is same if-else condition

# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

try:
    # Request 2 separate inputs from user
    a = int(input("Enter 1st number: \n"))
    b = int(input("Enter 2nd number: \n"))

    # Check and print even numbers
    if is_even(a):
        print(f"{a} is an even number.")
    else:
        print(f"{a} is not an even number.")

    if is_even(b):
        print(f"{b} is an even number.")
    else:
        print(f"{b} is not an even number.")

except ValueError:
    print("Please enter valid integers.")

# test:
# print(type(n))
# print()