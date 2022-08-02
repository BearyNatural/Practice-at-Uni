# import libraries for random and mean functions
import random
import statistics
rollArray = []

# function to get total of rolled numbers
def getTotal(array):
  total = 0
  for num in array:
    total += num

  return total

# function to get average of the rolled numbers
def getAvg(array):
  x = statistics.mean(array)
  return x

# First loop that controls prompting user input for number of rolls
ii = 0

while ii < 1:
  num = int(input('How many dice would you like to roll? '))
  i = 1

    
  # second loop to roll dice based on user's input
  while i <= num:

    i += 1
    roll = random.randint(1,6)
    print(roll)
    rollArray.append(roll)


  # Prompt user to roll again. If input is 'y' then exit program
  ii += 1
  if input("Roll again?(y/n) ") == 'y':
    print("\n")
    ii = 0  
  else:
    # Print the array, its total and mean values
    print("Rolls list = " ,rollArray)
    print("Total = ", getTotal(rollArray))
    print("Avg = ", getAvg(rollArray))
    print('End')