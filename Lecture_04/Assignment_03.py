                      #Here the program asks the user for input as a integer.
number = int(input("Enter a number: "))
                      #Here it validates the condition if and else condition and satisfies accordingly.
if number <= 1:
    print("It's not a prime number")

else:
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number")
            break
    else:             #After running for loop it not satisfies with above condition and it will through this output.
        print("It is a prime number")