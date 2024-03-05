import re
import glob
import subprocess
import sys
import json
import random

def read_sut(lang, sut_name):
    rfile=open('../suts.json',"r")
    string = rfile.read()
    rfile.close()
   
    suts = json.loads(string)[lang]
    return next(item for item in suts if item["name"] == sut_name)

def validate(lang, name):
    grammar_accepted = True
    try:
        batcmd="python3 " + "../" + lang + "/parser/parse.py " + name
        result = subprocess.check_output(batcmd, shell=True, stderr=subprocess.STDOUT)
        output = result.decode("utf-8",'ignore')
        if 'line' in output:
            grammar_accepted = False

    except subprocess.CalledProcessError as grepexc:
        if grepexc.returncode == 1:
            grammar_accepted = False  
        else:
            grammar_accepted = False
            print("Python crash here >> " + grepexc.output.decode("utf-8",'ignore'))
            print(name)
            
    return grammar_accepted

def bash_command(sut_folder, exe_cov, name, sut_name):
    if sut_name == 'py-lua-parser':
        cmd = "coverage run -a --branch --data-file='../" + sut_folder + "/.coverage' ../" + sut_folder + "/" + exe_cov + " " + name
        # coverage run -a --branch --data-file='../bench/lua/py-lua-parser/.coverage' ../bench/lua/py-lua-parser/bin/luaparser example.lua
    elif sut_name == 'aria2':
        cmd = './../' + sut_folder + '/' + exe_cov + ' "$(cat ' + name + ')"'
    elif sut_name == 'curl':
        cmd = './../' + sut_folder + '/' + exe_cov + ' "$(cat ' + name + ')" --max-time 3'
    elif sut_name == 'wget':
        cmd = './../' + sut_folder + '/' + exe_cov + ' "$(cat ' + name + ')" --timeout=3 --tries=1'
    elif sut_name == "fast-xml-parser":
        # Delete whitespaces in xml string
        subprocess.run(["./delete-xml-ws.sh " + name], shell=True)
        coverage_cmd = "./../" + sut_folder + "/node_modules/nyc/bin/nyc.js " + "--reporter=text-summary --clean=false --cwd " +  "../" + sut_folder
        cmd = coverage_cmd + " ./../" + sut_folder + "/" + exe_cov + " -v " + name
    elif sut_name == "pugixml":
        # Delete whitespaces in xml string
        subprocess.run(["./delete-xml-ws.sh " + name], shell=True)
        # Must call executable from origin directory
        cmd = "cd ../" + sut_folder + "/build/make-g++-coverage-standard-c++11 && ./test " + "../../../../" + name
    elif sut_name == "libxml2":
        # Delete whitespaces in xml string
        subprocess.run(["./delete-xml-ws.sh " + name], shell=True)
        cmd = "./../" + sut_folder + "/" + exe_cov + " " + name
    elif sut_name == "luac":
        #cmd = "./../" + sut_folder + "/" + exe_cov + " -o ../" + sut_folder + "/luac.out " + name
        cmd = "timeout 3s ./../" + sut_folder + "/" + exe_cov + " " + name
    elif sut_name == "luajit":
        #cmd = "cd ../" + sut_folder + "/src && ./luajit" + " -b ../../../" + name + " luajit.out"
        cmd = "timeout 3s ./../" + sut_folder + "/" + exe_cov + " " + name
    else:
        cmd = "./../" + sut_folder + "/" + exe_cov + " " + name
    return cmd

def analyse_feedback(exit_code, output, sut_name):   
    if sut_name == 'aria2': 
       return analyse_feedback_aria2(exit_code, output, sut_name)
    elif sut_name == 'curl': 
       return analyse_feedback_curl(exit_code, output, sut_name)
    elif sut_name == 'wget': 
       return analyse_feedback_wget(exit_code, output, sut_name)
    elif sut_name == 'luac' or sut_name == 'luajit': 
       return analyse_feedback_lua(exit_code, output, sut_name)
    else:
       return exit_code

def analyse_feedback_lua(exit_code, output, sut_name):
    semantic_error_message = "stack traceback"
    if exit_code == 0:
        # Valid lua input
        return 0
    elif semantic_error_message in output:
        # Valid lua input
        return 0
    else:
        return exit_code
         
def analyse_feedback_aria2(exit_code, output, sut_name):
    network_error_messages = ["Failed to connect", "Failed to establish connection"]
    if exit_code == 19:
        # Valid url input
        return 0
    elif any(msg in output for msg in network_error_messages):
        # Valid url input
        return 0
    else:
        return exit_code

def analyse_feedback_curl(exit_code, output, sut_name):
    if exit_code == 7 or exit_code == 6:
        # Valid url input
        return 0
    elif exit_code == 3:
        # Invalid
        return 1
    else:
        return exit_code
        
def analyse_feedback_wget(exit_code, output, sut_name):
    if exit_code in [0, 4]:
        # Valid url input
        return 0
    elif exit_code in [1]:
        # Invalid
        return 1
    else:
        return exit_code
              
def coverage_js(result):
    output = result.decode("utf-8",'ignore')
    line = output.split('\n')[-5]
    cov = line.split()[2][:-1]
    return float(cov)
    
def coverage_py(sut_name, sut_folder):
    # coverage report --include='../luaparser/*' --data-file='.coverage'
    cmd = "coverage report --include='../" + sut_folder + "/luaparser/*' --data-file='../" + sut_folder + "/.coverage'"
    result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    output = result.decode("utf-8",'ignore')
    line = output.split('\n')[-2]
    cov = line.split()[-1][:-1]
    return int(cov)
    
def coverage(sut_name, sut_folder, result):        
    if sut_name == "fast-xml-parser": return coverage_js(result)
    if sut_name == 'py-lua-parser': return coverage_py(sut_name, sut_folder)

    if sut_name == 'libxml2':
        batcmd="cd ../" + sut_folder + " && " + "gcovr -r . --branches" + " --exclude-directories=python --exclude-directories=doc -e=.*test.*.c -e=.*suite.*.c"
    else: 
        batcmd="gcovr -r ../" + sut_folder + " --branches"

    result = subprocess.check_output(batcmd, shell=True, stderr=subprocess.STDOUT)
    output = result.decode("utf-8",'ignore')
    line = output.split('\n')[-3]
    cov = line.split()[-1][:-1]
    return int(cov)
    
def main():
    run = sys.argv[1]
    time = sys.argv[2]
    tool = sys.argv[3]
    lang = sys.argv[4]
    sut_name = sys.argv[5]
    seed = sys.argv[6]
    get_cov = sys.argv[7]

    result_file = '../results/run-' + run + '-' + tool + '-' + sut_name + '.txt'
    sut = read_sut(lang, sut_name)
    sut_folder = 'bench/' + lang + '/run-' + run + '-' + tool + '-' + sut_name
    #exe = 'bench/' + lang + '/run-' + run + '-' + tool + '-' + sut_name + '/' + sut["exe_cov"]   
    exe_cov = sut["exe_cov"]
    grammar_accepted = True  
     
    name = '../' + lang + '/' + tool + '/tests/input_' + run + '_' + sut_name + '.in'

    batcmd = bash_command(sut_folder, exe_cov, name, sut_name)

    grammar_accepted = validate(lang, name)
    record = [int(time), tool, lang, seed, sut_name, 0, 0, 0, -1, 0]
    # Record: [time, tool, lang, seed, sut, accept_invalid, reject_valid, crash, coverage, sut_valid]
    # Example: [5, baseline-1, json, 3, parson, 0, 0, 0, -1, 0]
    try:
        sut_accepted = True

        result = subprocess.check_output(batcmd, shell=True, stderr=subprocess.STDOUT)
        # valid input
        record[9] = 1
        if not grammar_accepted:
            # accept_invalid case
            record[5] = 1

    except subprocess.CalledProcessError as grepexc:
        result = grepexc.output
        output = grepexc.output.decode("utf-8",'ignore')
        code = analyse_feedback(grepexc.returncode, output, sut_name)
        if code in [0, 124]:
            # valid url input
            record[9] = 1
            if not grammar_accepted:
                # accept_invalid case
                record[5] = 1
        elif code == 1:
            if grammar_accepted:
                # reject_valid case
                record[6] = 1

        else:
            print(sut_name + " Crash (diff-test-g) >> " + output)
            print(grepexc.returncode)
            record[7] = code

    # Get coverage every n seconds
    if get_cov == 'true':
        record[8] = coverage(sut_name, sut_folder, result)
        
    row = str(record) + '\n'
    text_file = open(result_file, "a")
    text_file.write(row)
    text_file.close()
    
if __name__ == '__main__': 
    main()
