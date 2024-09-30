import yaml
import json

# Step 1: Load the YAML file
with open('servers.yaml', 'r') as yaml_file:
    try:
        servers_dict = yaml.safe_load(yaml_file)  # Parse YAML data into a Python dictionary

        # Step 2: Convert the dictionary to JSON and write to a file
        with open('servers.json', 'w') as json_file:
            json.dump(servers_dict, json_file, indent=4)

        print("YAML file successfully converted to JSON.")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
