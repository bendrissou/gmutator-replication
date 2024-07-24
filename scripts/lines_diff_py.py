import json
import sys
import subprocess
import numpy as np

def execute_command(tool, run):
    path_folder = "'../bench/lua/run-" + str(run) + "-" + tool + "-py-lua-parser/luaparser/*'"
    path_data_file = "'../bench/lua/run-" + str(run) + "-" + tool + "-py-lua-parser/.coverage'"
    command = "coverage json --pretty-print -o coverage-" + tool + ".json --include=" + path_folder + " --data-file=" + path_data_file
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=3)

def update_results(data, tool, new_value):
    path = 'py-lua-parser/' + tool + '/unique-coverage'
    keys = path.split('/')
    d = data
    for key in keys[:-1]:
        d = d[key]
    d[keys[-1]] = new_value


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
        i+=1
        unique_coverage[file] = lines1 - lines2

    return unique_coverage

def count_unique_lines(unique_coverage):
    return {file: len(lines) for file, lines in unique_coverage.items()}

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py RUNS")
        sys.exit(1)

    runs = sys.argv[1]
    json_file_path1 = "coverage-grammarinator+mutations.json"
    json_file_path2 = "coverage-gmutator.json"

    all_runs_cov_1 = []
    all_runs_cov_2 = []

    for run in range(1, int(runs)+1):
        execute_command("grammarinator+mutations", run)
        execute_command("gmutator", run)

        coverage1 = extract_coverage_info(json_file_path1)
        coverage2 = extract_coverage_info(json_file_path2)

        unique_coverage1 = find_unique_lines(coverage1, coverage2)
        unique_coverage2 = find_unique_lines(coverage2, coverage1)

        unique_counts1 = count_unique_lines(unique_coverage1)
        unique_counts2 = count_unique_lines(unique_coverage2)

        total_unique_lines_1 = 0
        total_unique_lines_2 = 0

        #print("Unique lines covered by coverage1 but not by coverage2:")
        for file, count in unique_counts1.items():
            #print(f'{file}: {count} unique lines')
            total_unique_lines_1 += count

        #print("\nUnique lines covered by coverage2 but not by coverage1:")
        for file, count in unique_counts2.items():
            #print(f'{file}: {count} unique lines')
            total_unique_lines_2 += count

        all_runs_cov_1.append(total_unique_lines_1)
        all_runs_cov_2.append(total_unique_lines_2)

    file_path = '../results.json'
    data = load_json(file_path)

    # Edit results data
    update_results(data, "g+m", round(np.mean(all_runs_cov_1)))
    update_results(data, "gmutator", round(np.mean(all_runs_cov_2)))

    # Save the modified data back to the file
    save_json(data, file_path)

if __name__ == "__main__":
    main()