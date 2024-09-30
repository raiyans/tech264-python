import os
import sys
import json

def validate_json_file(filename):
    if os.path.exists(filename):
        # Open file using 'with' to ensure proper resource management
        with open(filename, "r") as file:
            try:
                # Parse the JSON file
                json.load(file)
                print("JSON file is valid!")
            except json.JSONDecodeError:
                print("ERROR: Invalid JSON format in file")
    else:
        print(f"ERROR: File '{filename}' not found")

if len(sys.argv) > 1:
    validate_json_file(sys.argv[1])
else:
    print("ERROR: No JSON file was specified to check")
    print(f"Usage: {sys.argv[0]} <JSON filename>")
# sys.argv[0] is always refering to the file name. sys.argv[1] will be start of the first argument