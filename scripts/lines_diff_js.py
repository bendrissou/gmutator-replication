import xml.etree.ElementTree as ET
import json
import sys
import subprocess
import numpy as np

def execute_command(tool, run):
    folder_name = "run-" + str(run) + "-" + tool + "-fast-xml-parser"
    command = "../bench/xml/" + folder_name + "/node_modules/nyc/bin/nyc.js report --reporter=clover --cwd ../bench/xml/" + folder_name
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output_file = "../bench/xml/" + folder_name + "/coverage/clover.xml"
    return parse_coverage(output_file)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=3)

def update_results(data, tool, new_value):
    path = 'fast-xml-parser/' + tool + '/unique-coverage'
    keys = path.split('/')
    d = data
    for key in keys[:-1]:
        d = d[key]
    d[keys[-1]] = new_value

def parse_coverage(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    coverage_data = {}

    # Iterate through each package
    for package in root.findall(".//package"):
        # Iterate through each file in the package
        for file in package.findall("file"):
            file_name = file.get("name")
            covered_lines = set()

            # Iterate through each line in the file
            for line in file.findall("line"):
                line_num = int(line.get("num"))
                count = int(line.get("count"))

                # If the line is covered (count > 0), add it to the set
                if count > 0:
                    covered_lines.add(line_num)

            # Add the file and its covered lines to the dictionary
            if file_name in coverage_data:
                coverage_data[file_name].update(covered_lines)
            else:
                coverage_data[file_name] = covered_lines

    return coverage_data

def find_unique_lines(coverage1, coverage2):
    unique_coverage = {}

    all_files_1 = coverage1.keys()
    all_files_2 = list(coverage2.keys())
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
        coverage_data_1 = execute_command("grammarinator+mutations", run)
        coverage_data_2 = execute_command("gmutator", run)

        uniq_lines_run_1 = find_unique_lines(coverage_data_1, coverage_data_2)
        uniq_lines_run_2 = find_unique_lines(coverage_data_2, coverage_data_1)

        unique_counts1 = count_unique_lines(uniq_lines_run_1)
        unique_counts2 = count_unique_lines(uniq_lines_run_2)

        total_unique_lines_1 = 0
        total_unique_lines_2 = 0

        for file, count in unique_counts1.items():
            total_unique_lines_1 += count

        for file, count in unique_counts2.items():
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