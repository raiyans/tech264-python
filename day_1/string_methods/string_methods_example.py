hi = "Hello World!"

# Check if 'hi' is made up of letters only
print(hi.isalpha())  # Output: False (because there are spaces and punctuation)

# Check if 'hi' is made up only of lowercase letters
print(hi.islower())  # Output: False (because there are uppercase letters)

# Check if 'hi' is made up only of uppercase letters
print(hi.isupper())  # Output: False (because not all letters are uppercase)

# Check if 'hi' ends with an exclamation mark
print(hi.endswith("!"))  # Output: True

# Check if 'hi' starts with a capital "H"
print(hi.startswith("H"))  # Output: True
