# Write a program that will take an input from user and print out if the number is negative or positive

# try-except is being used to handle potential input errors, this is same if-else condition

try:
    # Request input from user
    number = float(input("Enter a number: \n"))

    # Check and print the result
    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is zero.")

except ValueError:
    print("Please enter a valid number.")

# test:
# print(type(n))
# print()