#roll dice 

# Randomised import
import random

while True:
    nu_dice_roll = int(input("How many times would you like to roll the dice?\n"))

    for roll in range(0, nu_dice_roll):
        dice_roll_choice = random.randint(1,6)
        print(f"{dice_roll_choice} rolled dice")
    new = input("Roll again? y or n\n").lower()
    if new != 'y':
        break





#test
# print(type(nu_dice_roll))
# print(nu_dice_roll)
# print(dice_roll_choice)

# a=[]

# n=int(input("Enter number of elements:"))

# for j in range(n):

#     a.append(random.randint(1,20))

# print('Randomised list is: ',a)