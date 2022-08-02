# Q1 - prints integers from 1 to a number from user input
def q1_counting():
  count = 1

  inp = input('Enter a number to count to: ')
  
  if(inp.isdigit()):
    inputNumber = int(inp)
    
    while(count <= inputNumber):
      print(count)
      count += 1
    print('========================================')
    mainMenu()
  else:
    print('Please enter a valid number')
    q1_counting()

#Q2 Add two integers entered by the user
def q2_addNumbers():
  num1 = input("Enter first number to add: ")
  num2 = input("Enter second number to add: ")

  num1 = int(num1)
  num2 = int(num2)
  ans = num1 + num2

  print("Sum of the two numbers is", ans)

  print('==========================================')
  mainMenu()

#q3 Counts down from 10 to zero 
def q3_countDown():
  count = 10

  while(count >= 0):
    print(count)
    count -= 1

  print('BLAST OFF')
  print('==========================================')

# q4 get name from user.  If name is Fred/Fred Flintone/Flintstone, print YABBADABBADOOO!
def q4_checkFredFlintstone():
  name = input('Enter a name: ')

  if(name.upper() == 'FRED'):
    print("YABBADABBADOOO!")
  elif(name.upper() == 'FRED FLINTSTONE'):
    print("YABBADABBADOOO!")
  elif(name.upper() == 'FLINTSTONE'):
    print('You\'re not Fred!')

# q5 Asks user to enter names until "stop" is entered.  Stores names and print them in reversed
def q5_getNames():
  name = ''
  names = []

  while(name != 'stop'):
    name = input('Enter a name ("stop" to finish): ')
    names.append(name)
    # print(names)

  index = len(names) - 1
  while(index > -1):
    print(names[index])
    index -= 1

  print('==========================================')
  mainMenu()

# As q5_getNames().  Except this one doesn't store or print "stop"
def q6_getNamesNoStop():
  name = ''
  names = []

  while(name != 'stop'):
    name = input('Enter a name ("stop" to finish): ')
    names.append(name)

  names.remove('stop')

  index = len(names) - 1
  while(index > -1):
    
    print(names[index])
    index -= 1

  print('==========================================')
  mainMenu()

# Q7 Asks user for integers until "stop" is entered.  Prints the sum of all entered numbers at the end (should only do this once)
def q7_getSum():
  inp = ''
  total = 0

  while(inp != 'stop'):
    inp = input('Enter a number: ')
    
    if(inp.isdigit()):
      total += int(inp)
    elif(inp != 'stop'):
      print('A valid number or "stop" must be entered')

  print("Sum of entered numbers is: ", total)
  
  print('==========================================')
  mainMenu()

# As q7_getSum().  This one will store the numbers as well.  At the end will print total and then all numbers entered
def q8_getSumArray():
  inp = ''
  total = 0
  nums = []
  
  while(inp != 'stop'):
    inp = input('Enter a number: ')
    
    if(inp.isdigit()):
      total += int(inp)
      nums.append(int(inp))
    elif(inp != 'stop'):
      print('A valid number or "stop" must be entered')

  print("Sum of entered numbers is: ", total)

  # Must use the below while loop.  Cannot change to a for 
  print('Numbers entered were: ')
  index = 0
  while(index < len(nums)):
    print(nums[index])
    index += 1

  print('==========================================')
  mainMenu()

# returns the area of a rectangle given length and width. 
# Needs Debugging
def getRectangleArea(length, width):
  area = length * width
  return area

# gets a length and width from user.  Uses the getRectangleArea function to get the area.
def q9_useRectangleArea():
  length = int(input('Enter rectangle length: '))
  width = int(input('Enter rectangle width: '))
  # print(length * width)

  # print('The area of your rectangle is: ', length * width)
  print('The area of your rectangle is: ', getRectangleArea(length, width))

  print('==========================================')
  mainMenu()

# returns the power of a base number.  Eg. power 3, base 3, return 27.  power 2, base 4, return 16
# Needs Debugging - must use a loop to calculate the answer
def calcPower(power, base):
  ans = base 
  
  for count in range(power):
    ans *= power

  return ans

def q10_getPower():
  power = int(input('Enter power: '))
  base = int(input('Enter base: '))

  print(f"{base} to the power of {power} is {calcPower(power, base)}")
  print('==========================================')
  mainMenu()


# checks if num is a prime number.  Needs debugging 
def checkPrime(num):
  flag = False
  counter = 0
  
  if(num > 1):
      # check for factors
      while(counter < num):
          if (num % counter) == 1:
              # if factor is found, set flag to True
              flag = True
              # break out of loop
              break
  
  # check if flag is True
  if flag:
      return False
  else:
      return True

def q11_isPrime():
  number = int(input(('Enter a number: ')))
  result = checkPrime(number)
  
  if(result):
    print(f'{number} is a prime number')
  else:
    print(f'{number} is not a prime number')

  print('==========================================')
  mainMenu()


  # Main menu
def mainMenu():
  print('1 - q1_counting')
  print('2 - q2_addNumbers')
  print('3 - q3_countDown')
  print('4 - q4_checkFredFlintstone')
  print('5 - q5_getNames')
  print('6 - q6_getNamesNoStop')
  print('7 - q7_getSum')
  print('8 - q8_getSumArray')
  print('9 - q9_useRectangleArea')
  print('10 - q10_getPower')
  print('11 - q11_isPrime()')
  print('quit - exit program')

  selection = input('Enter an option: ')
  if(selection == '1'):
    q1_counting()
  elif(selection == '2'):
    q2_addNumbers()
  elif(selection == '3'):
    q3_countDown()
  elif(selection == '4'):
    q4_checkFredFlintstone()
  elif(selection == '5'):
    q5_getNames()
  elif(selection == '6'):
    q6_getNamesNoStop()
  elif(selection == '7'):
    q7_getSum()
  elif(selection == '8'):
    q8_getSumArray()
  elif(selection == '9'):
    q9_useRectangleArea()
  elif(selection == '10'):
    q10_getPower()
  elif(selection == '11'):
    q11_isPrime()
  elif(selection == 'quit'):
    print('Goodbye!')
    exit()
  else:
    mainMenu()

# start here
mainMenu()