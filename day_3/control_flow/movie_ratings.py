"""Task: Print movie rating meanings
Practice using one if statement that uses else if and else

The task
You are starting a new Python topic: "Control Flow". Organise your project appropriately for this topic.
For example, in the root of your PyCharm project (or in your python learning folder),
create a new folder named "control_flow". Store the code for this task there.
The if statement you make will below will print the meaning of the movie rating specified at the beginning of the code.
You should only need to replace the lines in CAPITALS with your own code. """

# possible film ratings are "universal", "pg", "12", "12a", "15", "18"

film_rating = "12a"

# use an if statement to check for "universal" rating

if film_rating == "universal":
    print("All age groups can watch this film")

# Check if the film rating is "pg"
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")

# Check if the film rating is "12" or "12a"
elif film_rating == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

# Check if the film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")

# Check if the film rating is "18"
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")

# Else statement for incorrect ratings
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18.")

