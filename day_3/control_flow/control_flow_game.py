"""Rationale:Consolidate control flow topic
The options
Battle Game
Dice roll game
Interactive quiz game
All the games should use the CLI (not anything like the pygame library).


Battle game
Make a 2 player battle game using Python.
Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.
If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.
The two Pokemon/fighters/characters need to fight.
A winner must be declared via some sort of calculation.
Bonus: Want to play again?

Note: No Pygame or Turtle allowed. CLI only.

Interactive quiz
Create and interactive quiz game using Python.
The subject can be what you want. Why not try to give the user an outcome at the end, like their personality type, what avenger they would be, what position on a football team would best suit them, etc?
Start by asking if they are ready to play the quiz, if they are start the game.
Ask question one, work out if the answer given is correct and if so add to a score variable.
Keep asking questions. As many as you like.
When the quiz ends, give them their score back, if you can give them back something more interesting than a score, that would be awesome!
Bonus: Want to play again?

Dice game
Make a dice game:
Let's make a game that rolls a dice and picks a winner.
Start the game with a welcome message and ask if the user is ready to play.
Get the user's name and start a loop (While loop recommended)
Use the random library and a method from that library to roll, a number 1-6
Store the number in a variable
Do the same for the computer
Compare the two numbers, whose was bigger? Tell the user! and end the game
Now add functionality to the game. Let the User and the CPU roll until one gets to 30. The one that gets there first is the winner!
Bonus: Want to play again?
"""

import random

max_points=30
human_random_roll, comp_random_roll = random.randrange(1, 6), random.randrange(1, 6)
human_random_score, comp_random_score = 0, 0
not_ready=True

print(human_random_roll, comp_random_roll)
while not_ready:
    if input("type yes if you are ready?")=="yes":
        not_ready =False
name = input("what's your name?")
print(f"first to 30 wins")
print(human_random_score, comp_random_score)
while human_random_score or comp_random_score <= 30:
    input("Press enter to roll")
    if human_random_roll > comp_random_roll:
        print("You are win this time!")
    if human_random_roll < comp_random_roll:
        print("You lost!")
    if human_random_roll == comp_random_roll:
        print(f"its a draw")
    human_random_score += human_random_roll
    comp_random_score += comp_random_roll
    print(human_random_score, comp_random_score)
    if human_random_score >= 30:
        print("you won the game")
        break
    if comp_random_score >= 30:
        print("you lost the game")
        break
    human_random_roll, comp_random_roll = random.randrange(1, 6), random.randrange(1, 6)