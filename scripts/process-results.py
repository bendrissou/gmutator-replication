import re
import glob
import subprocess
import os
import sys
import json
import plotext as plx
import numpy as np
import ast

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=3)

def edit_entry(data, path, new_values):
    keys = path.split('/')
    inner_dict = data
    for key in keys[:-1]:
        inner_dict = inner_dict[key]
    inner_dict[keys[-1]].update(new_values)

def main():
    tool = sys.argv[1]
    lang = sys.argv[2]
    sut = sys.argv[3]
    runs = int(sys.argv[4])
    time = []
    coverage = []
    n_inputs = []
    accept_invalid = []
    reject_valid = []
    crashes = []
    file_paths = []
    reports = []
    ini_time = []
    last_coverage = []

    print()
    title = ">> Processing results for " + str(tool) + " / " + sut + " (" + str(runs) + " runs)"
    print(title)

    # Reading entries
    for run in range(1, runs+1):
        report_path = '../results/run-' + str(run) + '-' + tool + '-' + sut + '.txt'
        filei = open(report_path, 'r')
        lines = filei.readlines()
        reports.append(lines)
        n_inputs.append(len(lines))
        ini_time.append(-1)
        time.append([])
        coverage.append([])
        last_coverage.append(-1)
        accept_invalid.append(0)
        reject_valid.append(0)
        crashes.append(0)
        filei.close()
    
    max_line_num = max(n_inputs)
    for i in range (max_line_num):
        for j in range(runs):
            try:
                lst = ast.literal_eval(reports[j][i].rstrip())
            except IndexError:
                continue
            time[j].append(lst[0])
            accept_invalid[j] += lst[5]
            reject_valid[j] += lst[6]
            if lst[7] not in [0, 2, 28]: # interesting exit codes
                crashes[j] += 1

            if lst[8] == -1:
                # No coverage measured for the current input
                if last_coverage[j] == -1:
                    # First input generated, i.e no prior coverage data
                    last_coverage[j] = 0
                    coverage[j].append(0)
                else:
                    # Copy previous coverage data
                    coverage[j].append(last_coverage[j])
                
            else:
                # There is coverage data for the current input
                last_coverage[j] = lst[8]
                coverage[j].append(lst[8])

    final_coverages = []
    for seq in coverage:
        final_coverages.append(seq[-1])
    
    if str(tool) == 'grammarinator+mutations': tool='g+m'
    
    # Specify the path to the results json data and the new values to update
    path = sut + '/' + str(tool)
    new_values = {
        "inputs": round(np.mean(n_inputs)),
        "accept-invalid": round(np.mean(accept_invalid)),
        "reject-valid": round(np.mean(reject_valid)),
        "total-coverage": round(np.mean(final_coverages)),
        "unique-coverage": -1,
        "crashes": round(np.sum(crashes))
    }

    file_path = '../results.json'
    data = load_json(file_path)

    # Edit results data
    edit_entry(data, path, new_values)

    # Save the modified data back to the file
    save_json(data, file_path)


if __name__ == '__main__': 
    main()