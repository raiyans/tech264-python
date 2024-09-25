"""
Slicing strings in Python is a way to extract a portion (substring) of a string using a specific range of indices.
It allows you to access and manipulate parts of a string by specifying a start, stop, and an optional step value.

The general syntax for slicing is:
    string[start:stop:step]
"""

Hw = "Hello world!"

print(Hw)

# Find out how many characters Hw has
print("length = ", len(Hw))


# Get the character in the first position in Hw
print("first char = ", Hw[1])

# Get the last character
print("last char = ", Hw[-1])

# Get the 2nd last character
print("last char = ", Hw[-2])

# Write a comment to EXPLAIN what does this do
# This starts with the 2nd index value in the string array and till the end
print(Hw[2:])

# Write a comment to EXPLAIN what does this do
# Starts with the 3rd last char and completes rest of string till end
print(Hw[-3:])

# Write a comment to EXPLAIN what does this do
# ends string starts from 0 index and ends at 5th index
print(Hw[:5])

# Starts from the second, stops at the fifth (doesn't include it)
