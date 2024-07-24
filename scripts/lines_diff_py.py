import json
import sys

def extract_coverage_info(json_file_path):
    with open(json_file_path, 'r') as file:
        coverage_data = json.load(file)
    
    covered_lines = {}

    files_info = coverage_data.get('files', {})
    for file_path, details in files_info.items():
        executed_lines = set(details.get('executed_lines', []))
        covered_lines[file_path] = executed_lines

    return covered_lines

def find_unique_lines(coverage1, coverage2):
    unique_coverage = {}

    all_files_1 = coverage1.keys()
    all_files_2 = list(coverage2.keys())
    #print("file count 1", len(list(all_files_1)))
    #print("file count 2", len(list(all_files_2)))
    i = 0
    for file in all_files_1:
        lines1 = coverage1.get(file, set())
        lines2 = coverage2.get(all_files_2[i], set())
        print("\nfile name", all_files_2[i])
        i+=1
        #print("lines1", lines1)
        #print("lines2", lines2)
        unique_coverage[file] = lines1 - lines2
        print("unique_coverage lines1", unique_coverage[file])

    return unique_coverage

def count_unique_lines(unique_coverage):
    return {file: len(lines) for file, lines in unique_coverage.items()}

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <coverage1.json> <coverage2.json>")
        sys.exit(1)

    json_file_path1 = sys.argv[1]
    json_file_path2 = sys.argv[2]

    coverage1 = extract_coverage_info(json_file_path1)
    coverage2 = extract_coverage_info(json_file_path2)

    unique_coverage1 = find_unique_lines(coverage1, coverage2)
    unique_coverage2 = find_unique_lines(coverage2, coverage1)

    unique_counts1 = count_unique_lines(unique_coverage1)
    unique_counts2 = count_unique_lines(unique_coverage2)

    total_unique_lines_1 = 0
    total_unique_lines_2 = 0

    print("Unique lines covered by coverage1 but not by coverage2:")
    for file, count in unique_counts1.items():
        print(f'{file}: {count} unique lines')
        total_unique_lines_1 += count

    print("\nUnique lines covered by coverage2 but not by coverage1:")
    for file, count in unique_counts2.items():
        print(f'{file}: {count} unique lines')
        total_unique_lines_2 += count

    print()
    print("total_unique_lines_1: ", total_unique_lines_1)
    print("total_unique_lines_2: ", total_unique_lines_2)

if __name__ == "__main__":
    main()