"""Practice control flow
Practice completing user stories"""



"""Task

Level 1

Challenge yourself to get Level 1 done in 15 min
Comments in the code are to help you meet user requirements, but you may need to write code in the order you think is necessary
```"""

# User story 1

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# Define/assign number to a variable called magic_number
# Ask user for input
# Check if this input matches magic_number
# Let the user know if the response was correct or not
# Allow the user 5 guesses
"""import random

max_tries=5
guesses = 0
random_num = random.randrange(1, 10)
while guesses< max_tries:
    magic_number = int(input("guess a number"))
    if magic_number == random_num:
        print("You are right!")
        break
    else:
        guesses += 1
        print(f"WRONG! You have {max_tries - guesses} guesses remaining loser!")"""



"""
```





Level 2

Challenge yourself to get from Level 1 to Level 2 in 10 min

```

# User story 2

# As a user, I want to be able to guess a number and know if I need to go higher or lower.


# User story 3

# As a user, I don't want my guesses wasted if I enter something accidently as my guess which are not digits.



# User story 4

# As a user, after each guess, I would like to know how many guesses I have left.

```
"""
import random

max_tries=5
guesses = 0
random_num = random.randrange(1, 10)
while guesses< max_tries:
    magic_number_is_digits = False
    while not magic_number_is_digits:
        magic_number = input("guess a number")
        magic_number_is_digits = magic_number.isdigit()
        if magic_number_is_digits: magic_number = int(magic_number)

    if magic_number == random_num:
        print("You are right!")
        break
    else:
        guesses += 1
        print(f"WRONG! You have {max_tries - guesses} guesses remaining loser!")
        if magic_number < random_num : print("gotta count higher than that number idiot")
        elif magic_number > random_num : print("it's a smaller number like you")
        print(random_num)
    if guesses == max_tries:
        print(f"You couldn't even guess {random_num}, pathetic")
"""



Level 3

Challenge yourself to get from Level 2 to Level 3 in 10 min

```

# User story 5

# As a user, I would like the magic to be randomly generated each time I play so it is more fun.



# User story 6

# As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries.

```

Hint:

Use the Python library random to generate a random number rather than assigning one


"""