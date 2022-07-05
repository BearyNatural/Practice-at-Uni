#user input
name = input("What is the user's first name?\n").capitalize()
surname = input("What is user's surname?\n").capitalize()
studentid = input("What is user's studentID?\n").capitalize()
dob = input("What is the user's date of birth? use format yyyy\n").capitalize()
current_year = input("What is the current year? use format yyyy\n").capitalize()

#age of user calulation
age = int(current_year) - int(dob)

#test
print(name)
print(surname)
print(studentid)
print(dob)
print(current_year)
print(f"{name} {surname}, {age} years old")