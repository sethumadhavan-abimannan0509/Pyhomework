    #Here we asks for user input
user_input = input("please enter a number: ")
number = []
    #It comes to while condition and and satisfies the condition
while True:
    if user_input == "":
        number.sort(reverse=True)
        break
    else:
        number.append(int(user_input))
        user_input = input("please enter a number: ")
    #Here we got the user inputs and it will print first 5 num in descending order
print("the 5 greatest numbers are: ")
for i in range(min(5, len(number))):
    print(number[i], end=" ")