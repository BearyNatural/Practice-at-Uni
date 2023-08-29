# Consider the following list
numbers = [3, 9, 2, 11, 17, 16, 21, 8, 36, 1, 5, 2] 

# Sum of odd number in the list using a for loop

# Initialize a variable to store the sum of even numbers
sum_odd = 0

# Iterate over each number in the list
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        sum_odd += num

print(f"Sum of all even numbers in the list: {sum_odd}")

# test:
# print(sum(numbers))