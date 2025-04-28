# NumberGuess is a number logic game specified with 5 different levels.

import random

def guess_the_number():
    # Print game introduction
    print("Welcome to NumberAll!")
    print("Choose a difficulty level:")
    print("1. Facile Mode (1-10)")
    print("2. Easy (1-50)")
    print("3. Medium (1-100)")
    print("4. Hard (1-200)")
    print("5. Turbo Mode (1-1000)")
    print("Choose ONE at a time")
    # Difficulty level is decided by the user
    while True:
        try:
            difficulty = int(input("Enter the number for your chosen difficulty (1/2/3/4/5): "))
            if difficulty == 1:
                number_range = 10
                break
            elif difficulty == 2:
                number_range = 50
                break
            elif difficulty == 3:
                number_range = 100
                break
            elif difficulty == 4:
                number_range = 200
                break
            elif difficulty == 5:
                number_range = 1000
                break
            else:
                print("Please choose a valid difficulty (1/2/3/4/5).")
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3/4/5).")

    # Randomly select a number based on the chosen difficulty
    number_to_guess = random.randint(1, number_range)
    attempts = 0
    guess = None

    print(f"Great! I have chosen a number between 1 and {number_range}. Try to guess it!")

    # Start the game loop
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
