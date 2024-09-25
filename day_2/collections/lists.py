"""
You are now moving onto ‘collections’.
Suggestion: Make a new folder inside the root project folder (or python learning folder) called ‘collections’ to store your work.

Write a Python script to:

Create a list called 'shopping_list' with the following items:
eggs
bread
bananas
biscuits
milk
Print the list to the screen
Print the data type of 'shopping_list'
Print the first item in the list
Print the last item in the list
Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'
"""

shopping_list=["eggs","bread","bananas","biscuits","milk"]

print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
shopping_list[1] = "rice"
print(shopping_list)
shopping_list.append("carrots")
print(shopping_list)

additional_list =["toffee","coffee"]
shopping_list.extend(additional_list)
print(shopping_list)
shopping_list.remove("bananas")
print(shopping_list)
shopping_list.pop()
print(shopping_list)
