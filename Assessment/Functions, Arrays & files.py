#roll dice 

# Randomised import
import random

bunnies_rolling = []

while True:
    nu_dice_roll = int(input("How many times would you like to roll the dice?\n"))

    for roll in range(0, nu_dice_roll):
        dice_roll_choice = random.randint(1,6)
        print(f"You rolled: {dice_roll_choice}")
        bunnies_rolling.append(dice_roll_choice)
    new = input("Roll again? y or n\n").lower()
    if new != 'y':
        break


def Average(bunnies_got_rabies):
    return sum(bunnies_got_rabies) / len(bunnies_got_rabies)
average = Average(bunnies_rolling)
# print(f"Average rolls: {average}")

# sum
total = sum(bunnies_rolling)

# # average
# average = total / len(bunnies_got_rabies)

# final prints
print(f"Average rolls: {average}")
print(f"Total of rolls: {total}")
print(f"Stored dice rolls: {bunnies_rolling}")

