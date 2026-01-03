"""
Question: Given this solution to Exercise 9, modify it to have one level of user feedback: if the user does not enter a number between 1 and 9, tell them. Don’t count this guess against the user when counting the number of guesses they used.
"""

import random as r
random_number  = r.randint(1,9)
guess_count = 0
while True:
    try:
        user_input = int(input("Enter a number: "))
        if 1 <= user_input <= 9:
            guess_count += 1
            if user_input == random_number:
                print(f"{user_input} is the correct number.\nYou guessed the correct number in {guess_count} guesses.")
                break
            elif user_input > random_number:
                print("Too High!")
            else:
                print("Too Low!")
        else:
            print("You must enter a number between 1 and 9")
    except ValueError:
        print("You must enter a number")
        continue
