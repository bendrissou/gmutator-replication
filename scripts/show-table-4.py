import json

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to print the table
def print_table(data):
    headers = ["", "Differential Line Coverage " , ""]
    sub_headers = ["", "Gmutator", "G+M"]
    rows = []

    for sut in data:
        short_sut = sut.replace("-parser", "")
        row = [short_sut]
        row.extend([
            data[sut]["gmutator"]["unique-coverage"],
            data[sut]["g+m"]["unique-coverage"]
        ])
        rows.append(row)

    print()
    print("=" * 32)
    # Print the headers
    print(f"  {headers[1]:^28} |")
    print("-" * 32)
    print(f"{sub_headers[0]:<8} | {sub_headers[1]:^8} | {sub_headers[2]:^8} |")
    print("-" * 32)

    # Print the rows
    for row in rows:
        print(f"{row[0]:<8} | {row[1]:>8} | {row[2]:>8} |")

# Load JSON data
file_path = '../results.json'  # Update with your file path
data = load_json(file_path)

# Print the table
print_table(data)
