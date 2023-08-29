# ask for 2 numbers separated by a ','
user_input = input("Enter 2 numbers separated by a ',':\n")

# separate the 2 numbers into 2 variables
numbers_list = user_input.split(",")

# change string to integer
a = int(numbers_list[0])
b = int(numbers_list[1])

# which is the bigger of the variable integers
c = max(a, b)

# change back to string to output the sum of the 2 inputs
d = str(c)

# test: 
# print("Variables given: " + user_input)
# print(numbers_list)
# print(numbers_list[0])
# print(numbers_list[1])
# print(a)
# print(b)
print(c)
print("The biggest of the 2 numbers given is: " + d)
# print()