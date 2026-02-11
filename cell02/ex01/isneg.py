user_input = input("Enter a number: ")
number = int(user_input)

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")