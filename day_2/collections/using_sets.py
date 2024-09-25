"""
Objective

Practice creating sets, adding and removing elements, and understanding the properties of sets.

The task

Explain 2 main ways that sets are different to lists and tuples
Create a set named 'fruits' containing "apple", "banana", and "cherry".
Print the set 'fruits'
Add "orange" to the fruits set using one of the set's methods.
Print the set 'fruits' - check it's added
Remove "banana" from the fruits set using one of the set's methods.
Print the set 'fruits' - check it's removed
Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
Print the final fruits set.
Print the 2nd item in the set. If there is any problem doing this, explain.
"""

"""
Sets Are Unordered:
Sets do not maintain element order, while lists and tuples are ordered and have indexes.

Example:
my_set = {3, 1, 2}  # Output: {1, 2, 3} (order not guaranteed)
Sets Do Not Allow Duplicates:
Sets remove duplicates automatically, while lists and tuples allow duplicates.

Example:
my_set = {1, 2, 2, 3}  # Output: {1, 2, 3} (no duplicates)
"""

fruits ={"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
# Cant add duplicates
# Sets are Unordered cant print an indexable value