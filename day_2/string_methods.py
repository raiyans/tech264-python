# TODO:Trim spaces off the beginning and end of a string


str_with_extra_spaces = "   extra spaces at the start and end   "

# Write comment to explain what this does
#  prints out len of string characters
print(len(str_with_extra_spaces))

# Write comment to explain what this does

print(len(str_with_extra_spaces.strip()))

"""
Next, use this new starting code for the next set of subtasks. Write code to do what the comments ask for.
"""

example_text = "here's some text with some words of text"

# count how many times the substring 'text' occurs within example_text & print it to the screen
print(example_text.count("text"))

# convert example_text to lowercase & print it to the screen
print(example_text.lower())

# convert example_text to uppercase & print it to the screen
print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
print(example_text.replace("with",","))