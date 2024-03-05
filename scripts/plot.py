import re
import glob
import subprocess
import os
import sys
import json
import plotext as plx
import numpy as np
import ast

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
        
    print()
    print("======================================================================\n")
    title = ">> Evaluation results for " + str(tool) + " / " + sut + " (" + str(runs) + " runs)"
    print(title)
    #print()
    print("\nNum of Inputs:\t {}  ({:.2f})".format(round(np.mean(n_inputs)), np.std(n_inputs)))
    print("Accept Invalid:\t {}  ({:.2f})".format(round(np.mean(accept_invalid)), np.std(accept_invalid)))
    print("Reject Valid:\t {}  ({:.2f})".format(round(np.mean(reject_valid)), np.std(reject_valid)))
    print("Branch Coverage: {}  ({:.2f})".format(round(np.mean(final_coverages)), np.std(final_coverages)))
    print("Crashes:\t {}  (SUM)".format(round(np.sum(crashes))))

if __name__ == '__main__': 
    main()
