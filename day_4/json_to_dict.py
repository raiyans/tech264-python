"""
Use Gen AI (ChatGPT or Google Gemini) to help speed up this task as much as you need to.  However what's important is that:
You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
Make sure you get your head around what your code does + add your own comments to explain each part of the code
Steps:

Create a new file servers.json and add this JSON to it:

{
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
Create a file called parse_json_to_dict.py and add code to it to: Steps:

Use 'with' to open the file created above

Parse contents the JSON file into a Python dictionary named "servers"

Print out the type of "servers"

Print out the dictionary record with the key "server1"

Print out the dictionary record with the key "server2"

Print all of the keys and values. Output should be:

Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
  Record key and sub value: 'hostname' = 'web-server-1'
  Record key and sub value: 'ip_address' = '192.168.1.1'
  Record key and sub value: 'role' = 'web'
  Record key and sub value: 'status' = 'active'
Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
  Record key and sub value: 'hostname' = 'db-server-1'
  Record key and sub value: 'ip_address' = '192.168.1.2'
  Record key and sub value: 'role' = 'database'
  Record key and sub value: 'status' = 'maintenance'
"""

import json

# Step 1: Open and read the JSON file using 'with' to automatically handle file closing
with open('servers.json', 'r') as json_file:
    # Step 2: Parse the contents of the JSON file into a Python dictionary
    servers = json.load(json_file)

# Step 3: Print out the type of "servers" to verify it's a dictionary
print(f"Type of 'servers': {type(servers)}")  # Should output <class 'dict'>

# Step 4: Print out the dictionary record with the key "server1"
print(f"Record for 'server1': {servers['server1']}")

# Step 5: Print out the dictionary record with the key "server2"
print(f"Record for 'server2': {servers['server2']}")

# Step 6: Print all the keys and values, including nested keys
for server_key, server_value in servers.items():
    # Print the top-level key and the entire dictionary as its value
    print(f"Key and value: '{server_key}' = '{server_value}'")

    # Iterate through the inner dictionary (e.g., hostname, ip_address)
    for record_key, record_value in server_value.items():
        print(f"  Record key and sub value: '{record_key}' = '{record_value}'")
