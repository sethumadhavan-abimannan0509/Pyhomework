cities = []
      #This program asks the user to input city name.
while len(cities) < 5:
    user_input = input("Please enter a city name: ")
      #Here it validates the correct input as a city name and stores it in the list called cities.
    if user_input.isalpha():
        cities.append(user_input)
    else:
        print("Invalid input! Please enter letters only.")
      #It prints the stored city name one by one
for city in cities:
    print(city)