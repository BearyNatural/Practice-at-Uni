# write a program that will take input from user and compare two numbers if they are smaller, bigger or equal

# request 2 separate inputs from user
a = int(input("Enter a whole number: \n"))
b = int(input("Enter another whole number: \n"))
c = int(input("Enter a 3rd whole number: \n"))

# convert numbers back to string for output
d = str(a)
e = str(b)
f = str(c)

# 1st ensure that no 2 numbers are the same, then compare the 3 numbers to find the biggest
if a == b or b == c or a == c:
    print("I'm sorry but you seem to have given me the same number more than once, please try again")
elif a > b and a > c:
    print(d + " is biggest number")
elif b > a and b > c:
    print(e + " is biggest number")  
elif c > a and c > b:
    print(f + " is biggest number")    
else:
    print("There seems to be an error in the numbers you gave me")

# test:
# print(list)
# print()

