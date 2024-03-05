import re
import glob
import subprocess
import os
import sys
import json

def main():
    grammar_file = '../' + sys.argv[1]
    #grammar_file =  '../json/JOSN.g4'

    rfile=open(grammar_file,"r")
    string = rfile.read()
    rfile.close()
    
    my_list = re.findall(r"'([^ '][^ ']+)'", string)
    print("\nList: ", my_list)
    
    for e in my_list:
    	if '\\' in e: my_list.remove(e)
    
    my_list = json.dumps(my_list)
    print("\nList: ", my_list)
    
    lst = grammar_file.split('/')
    folder = lst[1]
    wfile=open('../'+folder +"/tokens.json","w")
    wfile.write(my_list)
    wfile.close()
    
if __name__ == '__main__': 
    main()
