fish_length = float(input("What is your zander length in centimetres? "))

if fish_length >= 42:
    print("You can keep this fish.")
else:
    short = 42 - fish_length
    print(f"Your fish is should be in the minimum length of 42 centimetres. But, your's is short of {short} centimetres.")
    print("Sorry, You cannot keep this fish.")