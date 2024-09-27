"""Research:

What is encoding vs serialising (very quick, two or three dot points to understand the difference)
Work out which one of them are you doing with the subtasks below
Starting code:

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
Subtasks:

Convert this Python dictionary into a JSON-formatted string
Convert this Python dictionary to a JSON file
Extra guidance:

Use the json library
Write any other code necessary to test things converted correctly
Use Gen AI (ChatGPT or Google Gemini) to help speed up this task as much as you need to.  However what's important is that:
You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
Make sure you get your head around what your code does + add your own comments to explain each part of the code
"""
# Import the json module for serialization
import json

# Create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Subtask 1: Convert the dictionary into a JSON-formatted string
# json.dumps() converts the dictionary to a JSON string
servers_json_string = json.dumps(servers_dict, indent=4)  # 'indent=4' formats the string for readability

# Print the JSON string to verify the conversion
print("JSON String Output:")
print(servers_json_string)

# Subtask 2: Convert the dictionary into a JSON file
# json.dump() writes the dictionary to a JSON file
with open("servers.json", "w") as json_file:
    json.dump(servers_dict, json_file, indent=4)  # 'indent=4' formats the JSON file for readability

# Print confirmation that the file has been created
print("JSON file 'servers.json' has been created.")
