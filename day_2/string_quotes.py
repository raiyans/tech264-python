
bad_string = "I said 'Wow!'"

print(bad_string)

"""Explain: Why does this fail?
Find 3 ways to make this string assignment work
Condition: The Wow! must be surrounded in quotes when it prints to the screen
Explain: What is best practice when deciding what quotes to use around strings in Python?
 """

"""
Why does this fail?
The code fails because of unescaped quotes inside the string. The string 'I said 'Wow!'' uses single quotes (') both to define the string and around the word Wow!. This causes Python to incorrectly interpret the second single quote (just before Wow!) as the end of the string, resulting in a syntax error.

Three Ways to Fix This:
1. Using Double Quotes for the Outer String:
You can use double quotes (") for the outer string and keep the single quotes around Wow!.

code
bad_string = "I said 'Wow!'"
print(bad_string)  # Output: I said 'Wow!'

2. Using Escape Characters (\):
You can escape the single quotes inside the string using a backslash (\).

code 
bad_string = 'I said \'Wow!\''
print(bad_string)  # Output: I said 'Wow!'

3. Using Triple Quotes (''' or "three times)
"""