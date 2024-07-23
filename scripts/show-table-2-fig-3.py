import json

TOOLS = {
    "grammarinator": "Grammarinator",
    "gmutator": "Gmutator",
    "g+m": "G+M",
}

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to print the table
def print_table(data, tool):
    headers = ["", TOOLS[tool] , ""]
    sub_headers = ["", "inputs", "accept-invalid", "reject-valid", "coverage", "crashes"]
    rows = []

    for sut in data:
        short_sut = sut.replace("-parser", "")
        row = [short_sut]
        row.extend([
            data[sut][tool]["inputs"],
            data[sut][tool]["accept-invalid"],
            data[sut][tool]["reject-valid"],
            data[sut][tool]["total-coverage"],
            data[sut][tool]["crashes"]
        ])
        rows.append(row)

    print()
    print("=" * 77)
    # Print the headers
    print(f"{' ':<8} | {TOOLS[tool]:^64} |")
    print("-" * 77)
    print(f"{sub_headers[0]:<8} | {sub_headers[1]:^8} | {sub_headers[2]:^14} | {sub_headers[3]:^14} | {sub_headers[4]:^8} | {sub_headers[5]:^8} |")
    print("-" * 77)

    # Print the rows
    for row in rows:
        print(f"{row[0]:<8} | {row[1]:>8} | {row[2]:>14} | {row[3]:>14} | {row[4]:>8} | {row[5]:>8} |")

# Load JSON data
file_path = '../results.json'  # Update with your file path
data = load_json(file_path)

# Print the table
print_table(data, "grammarinator")
print_table(data, "gmutator")
print_table(data, "g+m")
