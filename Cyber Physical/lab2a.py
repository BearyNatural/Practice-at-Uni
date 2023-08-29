# write a program that will take input from user and print out the smaller number using separate inputs and the if condition

# request 2 separate inputs from user
a = float(input("Enter 1st number: \n"))
b = float(input("Enter 2nd number: \n"))

# convert numbers back to string for output
c = str(a)
d = str(b)

# compare the 2 numbers
if a > b:
    print(d + " is smaller than " + c)
else:
    print(c + " is smaller than " + d)

# test:
# print(type(c))
# print()

