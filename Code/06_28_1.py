#todays lesson
from datetime import datetime
from datetime import date
# get current date
now = datetime.now()
current_year = date.today().year
# print(current_year)

# a person class
class Person:
    def __init__(self, name, age): #is a reserved function
        # print("hey! I'm in the __init__")
        self.name = name
        self.age = age
#this type of class is used to create an Object
    def calcYOB(self):
        return current_year - self.age


p1 = Person("Jane", 21)
p2 = Person("Mary", 51)

print(p1.name)
print(p2.age)
print(f"Year of birth: {p2.calcYOB()}")

print(p2)

