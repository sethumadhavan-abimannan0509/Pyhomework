import random

def diceroll():
    return random.randrange(1,7)

counter = 0

while True:
    number = diceroll()
    counter += 1
    if number != 6:
        print(f"{counter} time of dice roll is {number}")
    else:
        print(f"Result is {number}")
        print("you have reached the final result")
        break