#  Write a program that will take two inputs from user and print out the last digit of that number.

# try-except is being used to handle potential input errors, this is same if-else condition

# Function to get the last digit of a number
def last_digit(n):
    return abs(n) % 10  # Use abs to handle negative numbers

try:
    # Request 2 separate inputs from user
    a = int(input("Enter 1st number: \n"))
    b = int(input("Enter 2nd number: \n"))

    # Print the last digits of the numbers
    print(f"The last digit of {a} is: {last_digit(a)}")
    print(f"The last digit of {b} is: {last_digit(b)}")

except ValueError:
    print("Please enter valid integers.")

# test:
# print(type(n))
# print()