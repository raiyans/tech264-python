"""
Use your code from the "Task: Get name, age and DOB details from a user".
Mix the name, age and DOB into one list user_details_list
Print the user's name, age and DOB from the list
Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
Ask the user for their height in cm and save it to the variable height
Save height as a float in the list, and print the height from the list.
"""

print("uh-oh you lost my memory who are you again?...")

person_list = [input("whats your name?")]
print(f"oh my yeah my name is {person_list[0]}")
person_list.append(input("whats your age?"))
print(type(person_list[1]))
if isinstance(person_list[1], str):
    person_list[1] = int(person_list[1])
print(type(person_list[1]))
print(f"Uh I'm {person_list[1]} years old")
person_list.append(input("whats your DOB?"))
print(f" hmmmm i was born on the date {person_list[2]}")
person_list.append(float(input("whats your height?")))
print(f" I am {person_list[3]}cm tall")