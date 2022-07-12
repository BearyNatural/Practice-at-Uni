largest_palindrome = 0



for n1 in range(100, 1000):

    for n2 in range(100, 1000):

        multiple = n1 * n2

        string_number = str(multiple)

        if string_number == string_number[::-1] and multiple > largest_palindrome:  

            largest_palindrome = multiple

print(largest_palindrome)