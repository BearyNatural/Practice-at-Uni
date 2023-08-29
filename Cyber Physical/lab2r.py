# Consider the following list
numbers = [3, 9, 2, 11, 17, 16, 21, 8, 36, 1, 5, 2] 

# Print all the odd number in the list using a for loop

# Iterate over each number in the list
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        print(num)