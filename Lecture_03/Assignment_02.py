         #Asks the user to enter the inches
inches = float(input("Enter a inches: "))

         # if the entered inches >=0, it converts inches into cm.
while inches >= 0:
    print(f"centimetre of the entered inches is: {inches*2.54}")
    inches = float(input("Enter a inches: "))

         # if the entered inches <0, it will stop the program.
    if inches < 0:
        print("you have entered a negative inches")