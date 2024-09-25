# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

menu = {"starters": {"calamari": 3, "calamari salad":4, "sliced calamari":3},
        "mains": {"steak": 10, "burger": 11, "ice": 9},
        "dessert": {"cheesecake": 5, "brownie": 5, "ice cream": 5}
        }

total_bill = 0
# level 1
customer_order_list =[]
# Greet the user
name = input("hello whats your name sir")

# Print a list of starters
print(menu["starters"].keys())
# Take an input for the user for their starter
customer_order_list.append(input("what starter would you like?").lower())
total_bill = total_bill + menu["starters"][customer_order_list[0]]
# Print a list of mains
print(menu["mains"].keys())
# Take an input for the user for their main course
customer_order_list.append(input("what main would you like?").lower())
total_bill = total_bill + menu["mains"][customer_order_list[1]]
# Print a list of desserts
dessert = ["Cheesecake", "Brownie", "Ice Cream"]
print(menu["dessert"].keys())
# Take an input for the user for their dessert
customer_order_list.append(input("what dessert would you like?").lower())
total_bill += menu["dessert"][customer_order_list[2]]
# Print all of the user's choices
print(f"You have ordered: {customer_order_list}")
print(f"Your total is: {total_bill}")
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'


# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
