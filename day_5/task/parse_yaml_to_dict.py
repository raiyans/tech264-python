# Import necessary modules
import yaml

# Step 1: Open and parse the YAML file using 'with'
with open('example.yaml', 'r') as yaml_file:
    try:
        # Step 2: Parse the YAML contents into a Python dictionary
        data = yaml.safe_load(yaml_file)

        # Step 3: Print the data to verify successful parsing
        print(f"Parsed YAML data as dictionary: {data}")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")