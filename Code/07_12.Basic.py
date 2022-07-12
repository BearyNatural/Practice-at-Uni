# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.



# variable = 12
# str(variable)
# # list = [1, 2]
# variable.reverse()
# print(list)
largestpalindrome = 0
multiple = 0

for number in range(100, 1000):

    for numbers in range(100, 1000):
        multiple = number * numbers

        foot = str(multiple)
        n = len(foot)
        s1 = foot[:n//2]
        s2 = foot[n//2:]
        s22 = s2[::-1]
        if s1 == s22:
            # test
            # feet = foot
            if largestpalindrome < multiple:
                largestpalindrome = multiple
            # print(feet)

print(largestpalindrome)


        # test
        # print(foot)
        






# Find the largest palindrome made from the product of two 3-digit numbers.

