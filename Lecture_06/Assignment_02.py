def conversion(gallons):
    number = gallons * 3.785
    return number

print("Welcome to American Gallon to Litre converter")

while True:
    user_input = float(input("Enter your gallons: "))
    if user_input < 0:
        print("You have entered a negative number")
        break
    else:
        converted = conversion(user_input)
        print(f"your gallons in litres is {converted}")