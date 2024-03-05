import re
import glob
import subprocess
import os
import sys
import json
import plotext as plx
import numpy as np
import ast
from statistics import mean

def read_suts(lang):
    rfile=open('../suts.json',"r")
    string = rfile.read()
    rfile.close()
   
    suts = json.loads(string)[lang]
    return [item["name"] for item in suts]

def read_file(path):
    try:
        with open(path, 'r') as filei:
            lines = filei.readlines()
            return lines
    except FileNotFoundError:
        print("Error: missing a report file!")
        print(path)
        exit(-1)
    
    
def main():
    tool = sys.argv[1]
    lang = sys.argv[2]
    runs = int(sys.argv[3])
    
    sut_1_accept_num = []
    sut_2_accept_num = []
    sut_3_accept_num = []
    
    suts_names = read_suts(lang)

    results_all_runs = []
    discrepancies = []
    input_number = []
    for run in range(1, runs+1):
        sut1_report_path = '../results/run-' + str(run) + '-' + tool + '-' + suts_names[0] + '.txt'
        sut2_report_path = '../results/run-' + str(run) + '-' + tool + '-' + suts_names[1] + '.txt'
        sut3_report_path = '../results/run-' + str(run) + '-' + tool + '-' + suts_names[2] + '.txt'
        
        one_run = [read_file(sut1_report_path), read_file(sut2_report_path), read_file(sut3_report_path)]
        results_all_runs.append(one_run)
        
        line_n = len(one_run[0])
        for a in one_run:
            n = len(a)
            if n < line_n: line_n = n

        input_number.append(line_n)
        sut_1_accept_num.append(0)
        sut_2_accept_num.append(0)
        sut_3_accept_num.append(0)
        discrepancies.append(0)
        i = run - 1
        for ln in range(line_n):
            current_line_sut_1 = ast.literal_eval(one_run[0][ln].rstrip())
            sut_1_accept_num[i] += current_line_sut_1[9]
            
            current_line_sut_2 = ast.literal_eval(one_run[1][ln].rstrip())
            sut_2_accept_num[i] += current_line_sut_2[9]

            current_line_sut_3 = ast.literal_eval(one_run[2][ln].rstrip())
            sut_3_accept_num[i] += current_line_sut_3[9]

            if not (current_line_sut_1[9] == current_line_sut_2[9] == current_line_sut_3[9]):
                discrepancies[i] += 1
              

    # Reading entries
    title = "Differential testing across " + lang + " SUTs. (" + tool + ")"
    print("======================================================================")
    print(title)
    print("======================================================================")
    print("\nNumber of inputs: ", mean(input_number))
    print("\nNumber of discrepancies: ", mean(discrepancies))
    print()
    print("Number of inputs accepted by " + suts_names[0] + ": ", mean(sut_1_accept_num))
    print("Number of inputs accepted by " + suts_names[1] + ": ", mean(sut_2_accept_num))
    print("Number of inputs accepted by " + suts_names[2] + ": ", mean(sut_3_accept_num))
    print()
    

    
if __name__ == '__main__': 
    main()
