# Write a program that will take two inputs from user and print out the average number

# try-except is being used to handle potential input errors, this is same if-else condition
def average(num1, num2):
    return (num1 + num2) / 2

try:
    # request 2 separate inputs from user
    a = float(input("Enter 1st number: \n"))
    b = float(input("Enter 2nd number: \n"))

    # find and print the average number
    print(f"The average of {a} and {b} is: {average(a, b), 2}")

except ValueError:
    print("Please enter valid numbers.")

# test:
# print(type(num1))
# print()
