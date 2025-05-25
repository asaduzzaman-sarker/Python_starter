def guess_the_number():
    secret_number = 6  # The number to guess
    user_input = int(input("Enter a number between 1 and 9: "))

    if user_input < secret_number:
        print("Your guess is almost there.")
    elif user_input > secret_number:
        print("Your guess is higher.")
    else:
        print("Your Guess Is Correct!")
    print(user_input)