import random
           #It generates random numbers
numbers = random.randint(1,10)
attempts = 0
           #This while condition matches the user input with random computer generated numbers and gives output accordingly.
while True:
    user_input = int(input("Enter a number between 1 and 10: "))
    attempts += 1

    if user_input > 10:
        print("you have entered a number greater than 10. please enter a number between 1 and 10")
    elif user_input < 1:
        print("you have entered a number less than 1. please enter a number between 1 and 10")
    elif user_input > numbers:
        print("Too high")
    elif user_input < numbers:
        print("Too low")
    else:
        print("correct")
        print(f"you have guessed the number on {attempts} attempts")
        break