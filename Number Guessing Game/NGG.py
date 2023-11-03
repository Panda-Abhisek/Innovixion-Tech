import random
import math

# Taking Inputs from user
min_range = int(input("Enter the minimum range: "))
max_range = int(input("Enter the maximum range: "))

# Generating random number between the range
random_number = random.randint(min_range, max_range)

# Calculating number of guesses
no_of_guesses = math.log(max_range - min_range + 1, 2)

# Showing user the number of guesses available to guess
print("\nMinimum number of attempts available: ", round(no_of_guesses))

# Guess the number
number = 0

while number < no_of_guesses:
    number += 1
    guess = int(input("\nEnter your guess: "))

    if random_number == guess:
        print("\nCongratulations! You guessed the number in ", number, " guesses")
        break
    elif random_number > guess:
        print("\nYou guessed a smaller number!")
    elif random_number < guess:
        print("\nYou guessed a larger number!")

if number >= no_of_guesses:
    print("\nYou failed to guess the number in ", number, " attempts")
    print("\nThe number was ", random_number)

# End of code