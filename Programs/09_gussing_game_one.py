"""
Question: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:
    1.Keep the game going until the user types “exit”
    2.Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random as r
import sys
num = str(r.randint(1,9))
print(f"Random number: {num}") # printing the random number to check if the program is working as it is intended to
c = 0
while(1):
    user = input()
    if user == 'exit':
        sys.exit()
    else:
        c+=1
        if user == num:
            print("Exactly right!")
            break
        elif user < num:
            print("Too low")
        elif user > num:
            print("Too high")
print(f"Number of guesses: {c}")
    
