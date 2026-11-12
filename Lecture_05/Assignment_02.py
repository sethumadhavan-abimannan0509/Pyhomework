user_input = input("Enter a name: ")
name = set()

while user_input != "":
    if user_input not in name:
        name.add(user_input)
        print("new name")
        user_input = input("Enter a name: ")
    else:
        print("existing name")
        user_input = input("Enter a name: ")
for i in name:
    print(i)
