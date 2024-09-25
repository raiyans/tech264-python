# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1
customer_order_list =[]
# Greet the user
name = input("hello whats your name sir")

# Print a list of starters
starters = ["Calamari", "Calamari Salad", "Sliced Calamari"]
print(starters)
# Take an input for the user for their starter
customer_order_list.append(input("what starter would you like?"))
# Print a list of mains
mains = ["Steak", "Burger", "Ice"]
# Take an input for the user for their main course
customer_order_list.append(input("what main would you like?"))
# Print a list of desserts
dessert = ["Cheesecake", "Brownie", "Ice Cream"]

# Take an input for the user for their dessert
customer_order_list.append(input("what dessert would you like?"))
# Print all of the user's choices
print(f"You have ordered: {customer_order_list}")
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'


# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
