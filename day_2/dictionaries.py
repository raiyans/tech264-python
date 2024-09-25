"""
Make a dictionary called "student_1" containing the following information:
name: susan
stream: tech
completed_lessons: 4 (should be saved as an integer not a string)
completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up"

Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with?
Print the dictionary to the screen
Print its data type to the screen to check it's a dictionary
Print the value for the key-value pair having the key "stream"
Print the value for 'completed_lesson_names' - check you can see the list of 3 items
Print the data type for the value for 'completed_lesson_names' - check it is a list
Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
Change the value of "completed_lessons" to 3 (an integer not string). Make sure you change was successful by printing your dictionary to the screen again.
Delete "data_types" from the list under the key 'completed_lesson_names'
Use the keys() method on your dictionary to list all the keys
"""

"""
A dictionary in Python stores data as key-value pairs. Each key is unique and immutable, and it is associated with a value, which can be any data type.

Example:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
Keys: "name", "age", "city"
Values: "Alice", 30, "New York"

You access values using their keys.
"""


student_1 = {"name": "susan",
             "stream": "tech",
             "completed_lessons": 4,
             "completed_lesson_names": ["variables", "data_types", "set up"]}

print(student_1)
print(type(student_1))
print(student_1["stream"])
print(student_1["completed_lesson_names"])
print(type(student_1["completed_lesson_names"]))
print(student_1["completed_lesson_names"][0])
student_1["completed_lessons"] = 3
print(student_1)
student_1["completed_lesson_names"].remove("data_types")
print(student_1)