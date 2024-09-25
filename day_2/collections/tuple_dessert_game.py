"""Before finishing the game below, answer these questions:

1.How are tuples similar to lists?
2.Are tuples immutable and what does this mean?
3.What other data types are immutable?
4.What is a good use case for tuples?
5.What does the following piece of code do? """

"""
1.Both store multiple values, can contain different data types, and support indexing and iteration.

2.Yes, tuples are immutable. This means once created, their values cannot be changed, added to, or removed.

3.Strings, integers, floats, booleans, and frozen sets.

4.Storing unchangeable data like days of the week, returning multiple values from a function, or using them as dictionary keys.
"""

essentials = ("bread", "eggs", "milk")

print(essentials)

print(essentials.count("bread"))

# makes a tuple and the prints it out and then prints how many times bread occurs in the tuple

"""Practice using tuples
Add your code where it says 'YOUR CODE GOES HERE'
"""




# "Stranded on a Desert Island" game

# Rationale: Practice tuples

# Type of exercise: Finish the code

print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ")

essential_item2 = input("What is an essential item you would take? ")

essential_item3 = input("What is an essential item you would take? ")

# save the items as a tuple

essentials_tuple = (essential_item1,essential_item2,essential_item3)  # YOUR CODE GOES HERE INSTEAD OF 'None'

# print the tuple

print("Here are your items as a tuple:", essentials_tuple)

print("")

print("I lied. You can take one more item.")

essential_item4 = input("What is one more essential item you would take? ")

# try to add the 4th item to the tuple

# if you can't add the 4th item, work out how to save the 4th item to the tuple

essentials_tuple = essentials_tuple + (essential_item4,)
print(essentials_tuple)


print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)


