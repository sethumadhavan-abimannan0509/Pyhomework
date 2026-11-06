
import random
    #Getting input from the user for how many times
dice = int(input("how many dice to roll? "))
total = 0
    #it rolls the dice according to the user input
for i in range(dice):
    roll = random.randint(1, 6)
    total += roll
    #Finally you will get the sum of the rolled dice
print(f"you rolled a {total}")

