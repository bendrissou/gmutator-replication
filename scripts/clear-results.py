import json

filepath="../results.json"

def reset_numerical_values(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (int, float)):
                data[key] = -1
            else:
                reset_numerical_values(value)
    elif isinstance(data, list):
        for item in data:
            reset_numerical_values(item)
    return data

# Load JSON data from a file
with open(filepath, 'r') as file:
    data = json.load(file)

# Reset numerical values
reset_data = reset_numerical_values(data)

# Save the modified data back to the file
with open(filepath, 'w') as file:
    json.dump(reset_data, file, indent=3)
