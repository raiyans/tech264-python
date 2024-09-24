# When is None Commonly Used?
# Default return value: Functions that do not explicitly return anything return None.
# Placeholders: Used as a placeholder for variables that will be assigned later.
# Optional arguments: It is often used in function arguments to denote that a value is optional.

x = None
print(bool(x))  # Output: False

# Check if x is None
if x is None:
    print("x is None")  # This will print "x is None"
else:
    print("x is not None")