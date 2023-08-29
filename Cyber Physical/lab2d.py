# Write a program that will take two inputs from user and print out the sum of that two number.

# try-except is being used to handle potential input errors, this is same if-else condition
def sum(num1, num2):
    return (num1 + num2)

try:
    # request 2 separate inputs from user
    a = int(input("Enter 1st number: \n"))
    b = int(input("Enter 2nd number: \n"))

    # find and print the sum number
    print(f"The average of {a} and {b} is: {sum(a, b)}")

except ValueError:
    print("Please enter valid numbers.")

# test:
# print(type(num1))
# print()
