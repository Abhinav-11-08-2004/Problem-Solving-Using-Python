"""
Question: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:-
->Rock beats scissors
->Scissors beats paper
->Paper beats rock
"""

player_1 = input("Player 1: ")
player_2 = input("Player 2: ")

if player_1==player_2:
    print("DRAW")
elif player_1=='rock':
    if player_2=='paper':
        print("Player 2 wins!")
    elif player_2=='scissors':
        print("Player 1 wins!")
elif player_1=='scissors':
    if player_2=='rock':
        print("Player 2 wins!")
    elif player_2=='paper':
        print("Player 1 wins!")
elif player_1=='paper':
    if player_2=='scissors':
        print("Player 2 wins!")
    elif player_2=='rock':
        print("Player 1 wins!")

