"""
Copyright 2023 Bachir Bendrissou

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import numpy as np
import re
import glob
import subprocess
import os
import sys
import json
import argparse

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=3)

def update_results(data, sut, tool, new_value):
    path = sut + '/' + tool + '/unique-coverage'
    keys = path.split('/')
    d = data
    for key in keys[:-1]:
        d = d[key]
    d[keys[-1]] = new_value

def get_source_files(sut_folder):
    batcmd="gcovr -r " + sut_folder
    result = subprocess.check_output(batcmd, shell=True, stderr=subprocess.STDOUT)
    output = result.decode("utf-8",'ignore')
    all_source_files = output.split('\n')

    # find and delete lines that contain error or warning messages
    delete_i = []
    i = 0
    for line in all_source_files:
        if line == '':
            delete_i.append(i)
        elif re.search('(WARNING)', line, re.IGNORECASE):
            delete_i.append(i)
        elif re.search('cannot open', line, re.IGNORECASE):
            delete_i.append(i)
        elif re.search('could not open', line, re.IGNORECASE):
            delete_i.append(i)
        elif re.search('gcovr could not infer', line, re.IGNORECASE):
            delete_i.append(i)
        i += 1
    # delete lines in reverse order
    for index in sorted(delete_i, reverse=True):
        del all_source_files[index]
    source_files = all_source_files[6:-3]
    return source_files


def get_file_missed_lines(line):
    line_data = line.split()
    
    # In case there are no missed lines reported
    if len(line_data) < 5: return []    
    
    missed_lines = line_data[-1]
    missed_lines = missed_lines.split(',')
    
    # We need to break intervals into lists: 1-3 -> 1,2,3
    delete_i = []
    for i in range(0, len(missed_lines)):
        try:
            missed_lines[i] = int(missed_lines[i])
        except ValueError as ve:
            #print("delete: ", missed_lines[i])
            delete_i.append(i)
            r = missed_lines[i].split('-')
            r = [int(j) for j in r]
            k=r[0]
            while (k<=r[1]):
                missed_lines.append(k)
                k+=1
    # delete intervals in reverse order
    for index in sorted(delete_i, reverse=True):
        del missed_lines[index]
    #missed_lines = [int(i) for i in missed_lines]
    return missed_lines

def coverage_diff(lines_a, lines_b):
    # Find missing lines which are in A but not in B
    # i.e Find lines missed by A, but covered by B
    diff = list(set(lines_a) - set(lines_b))
    return sorted(diff)

def determine_language(sut_value=None):
    # Determine the language based on the SUT value
    language_map = {
        'cjson': 'json',
        'parson': 'json',
        'simdjson': 'json',
        'luac': 'lua',
        'luajit': 'lua',
        'py-lua-parser': 'lua',
        'aria2': 'url',
        'curl': 'url',
        'wget': 'url',
        'fast-xml-parser': 'xml',
        'libxml2': 'xml',
        'pugixml': 'xml',
    }

    language = language_map.get(sut_value)

    if language:
        return language
    else:
        raise ValueError(f"Error: Unknown SUT {sut_value}")



def main():
    parser = argparse.ArgumentParser(description='Shows the difference in coverage of an SUT by two different tools.')
    parser.add_argument('--sut', type=str, required=True, help='Name of system under test.')
    parser.add_argument('--runs', type=int, required=True, help='Number of runs.')

    args = parser.parse_args()

    # Access the parsed arguments
    sut = args.sut
    runs = args.runs
    lang = determine_language(sut)

    all_runs_cov_1 = []
    all_runs_cov_2 = []

    for run in range(1, runs+1):
        source_1 = '../bench/' + lang + '/run-' + str(run) + '-grammarinator+mutations-' + sut
        source_2 = '../bench/' + lang + '/run-' + str(run) + '-gmutator-' + sut

        uniq_total_num_1 = 0
        uniq_total_num_2 = 0
    
        source_files_1 = get_source_files(source_1)
        source_files_2 = get_source_files(source_2)
    
        files_count = len(source_files_1)

        for i in range(files_count):
            line = source_files_1[i]
            missed_lines_1 = get_file_missed_lines(line)
        
            line = source_files_2[i]
            missed_lines_2 = get_file_missed_lines(line)
            
            uniq_lines_1 = coverage_diff(missed_lines_2, missed_lines_1)
            uniq_lines_2 = coverage_diff(missed_lines_1, missed_lines_2)
            
            uniq_num_1 = len(uniq_lines_1) 
            uniq_num_2 = len(uniq_lines_2) 
            
            if uniq_num_1 == uniq_num_2 == 0: continue
            uniq_total_num_1 += uniq_num_1
            uniq_total_num_2 += uniq_num_2
            
        print()
        print("Total unique line coverage ({}): ".format(source_1), uniq_total_num_1)
        print("Total unique line coverage ({}): ".format(source_2), uniq_total_num_2)
        all_runs_cov_1.append(uniq_total_num_1)
        all_runs_cov_2.append(uniq_total_num_2)
    
    file_path = '../results.json'
    data = load_json(file_path)

    # Edit results data
    update_results(data, sut, "g+m", round(np.mean(all_runs_cov_1)))
    update_results(data, sut, "gmutator", round(np.mean(all_runs_cov_2)))

    # Save the modified data back to the file
    save_json(data, file_path)


if __name__ == '__main__': 
    main()