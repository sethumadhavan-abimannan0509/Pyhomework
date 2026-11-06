        # Asks the user to enter the number
user_input = input("Enter a number: ")
numbers = []

        #if the user enters the empty, this condition will execute and stops the program and gives result.
while True:
    if user_input == "":
        print(f"smallest number is {min(numbers)}")
        print(f"largest number is {max(numbers)}")
        break
        # if the user enters the number, it updates the empty list with entered value as float until user leaves blank.
    else:
        numbers.append(float(user_input))
        user_input = input("Enter a number: ")
