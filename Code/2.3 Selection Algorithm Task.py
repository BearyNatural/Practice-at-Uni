#program receives 2 numbers, if the numbers add up to geater 
# than 10, output "sum of numbers is greater than 10".  If 
# the numbers add up to less than 10, output "Sum of numbers 
# is less than 10.  What happens if the numbers add up to 10?"

#user input requested
userinput1 = input("Choose a number between 0 and 9:\n")
userinput2 = input("Choose a 2nd number between 0 and 9:\n")

#conversion to interger
userinput1 = int(userinput1)
userinput2 = int(userinput2)

#calculation of numbers
total = userinput1 + userinput2

#if conditions
if total > 10:
    print("Sum of numbers is greater than 10")
elif total < 10:
    print("Sum of numbers is less than 10")
else:
    print("Sum of numbers is equal to 10")

#test
print(userinput1)
print(userinput2)
print(total)