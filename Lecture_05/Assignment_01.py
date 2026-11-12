

months = ("spring", "summer", "autumn", "winter")

user_input = int(input("Enter a number: "))

if user_input == 1 or user_input == 2 or user_input == 3:
    print(months[0])
elif user_input == 4 or user_input == 5 or user_input == 6:
    print(months[1])
elif user_input == 7 or user_input == 8 or user_input == 9:
    print(months[2])
elif user_input == 10 or user_input == 11 or user_input == 12:
    print(months[3])
else:
    print("invalid input, please enter a number between 1 and 12")