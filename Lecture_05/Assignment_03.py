print("Welcome to the Airport Database")
airport = {}

while True:
    print("\ninput (1) for enter new airport details")
    print("input (2) to fetch existing airport details")
    print("input (3) to exit\n")
    user_number = int(input("Enter a number: "))
    if user_number == 1:
       user_input = input("Enter the ICAO code and airport name: ")
       code, name = user_input.split(",")
       airport[code.upper()] = name
       print("Airport saved!")
    elif user_number == 2:
       user_code = input("Enter the ICAO code of the airport: ").upper()
       if user_code in airport:
           print(airport[user_code])
       else:
           print("The ICAO code of the airport is incorrect.")
    elif user_number == 3:
       print("Goodbye!")
       break
    else:
        print("Please enter a valid number")
        continue

