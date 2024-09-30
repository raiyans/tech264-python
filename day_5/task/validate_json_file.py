import yaml

def validate_yaml(file_path):
    try:
        # Open and load the YAML file
        with open(file_path, 'r') as yaml_file:
            yaml.safe_load(yaml_file)
        print(f"{file_path} is a valid YAML file.")
    except yaml.YAMLError as exc:
        print(f"Error: {file_path} is not a valid YAML file.")
        print(f"Details: {exc}")

# Test the function with your YAML file
validate_yaml('example.yaml')
