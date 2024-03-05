import random
import re
import glob
import subprocess
import os
import sys
import json

tokens = []

def delete_random_sequence(s: str) -> str:
    #print("delete_random_sequence")
    """Returns s with a random sequence deleted"""
    if s == "":
        return s
    elif len(s) == 1:
        return ""
    pos_start = random.randint(0, len(s) - 2)
    pos_end = random.randint(pos_start+1, len(s) - 1)
    #print("Deleting: ", s[pos_start:pos_end])
    return s[:pos_start] + s[pos_end:]
    
def duplicate_random_sequence(s: str) -> str:
    #print("duplicate_random_sequence")
    """Returns s with a random sequence inserted"""
    if s == "":
        return s
    elif len(s) == 1:
        return s + s
    pos_start = random.randint(0, len(s) - 2)
    pos_end = random.randint(pos_start+1, len(s) - 1)
    #print(pos_start, pos_end)
    seq = s[pos_start:pos_end]
    #print("Duplicating: ", seq)
    return s[:pos_end] + seq + s[pos_end:]
    
def insert_keyword(s):
    #print("insert_keyword")
    """Returns s with a random bit flipped in a random position"""
    if s == "":
        return s
    
    new_seq = random.choice(tokens)
    pos = random.randint(0, len(s))
    #print("Inserting: ", new_seq)
    return s[:pos] + new_seq + s[pos:]
    
def mutate(s: str) -> str:
    """Return s with a random mutation applied"""
    mutators = [
        delete_random_sequence,
        duplicate_random_sequence,
        insert_keyword
    ]
    mutator = random.choice(mutators)
    # print(mutator)
    return mutator(s)
    
def read_tokens(inp_format):

    rfile=open('../'+inp_format+'/tokens.json',"r")
    string = rfile.read()
    rfile.close()

    my_list = json.loads(string)
    
    return my_list

def main():
    inp_format = sys.argv[1]
    seed = sys.argv[2]
    random.seed(seed)
    name = '../'+inp_format + '/grammarinator+mutations/tests/input_' + seed + '.in'

    total = 0
    global tokens
    tokens = read_tokens(inp_format)

    try:
        rfile=open(name,"r")
        original = rfile.read()
        rfile.close()
        
        # Apply between one and three random mutations
        n_mutations = random.randrange(1, 4)
        #print("\noriginal: ", original)
        mutated = original
        for _ in range(n_mutations):
            mutated = mutate(mutated)
            #print(str(_) + " mutated: ", mutated)

        # Write to input file
        wfile=open(name,"w")
        wfile.write(mutated)        
        wfile.close()           

    except Exception as e:
        #print("\n\n>>>>>>>")
        print(">>>>>>>  ERROR: ", str(e))
        #print(">>>>>>>")
        #print("\n\n")

            
    #print("+++ Total inputs " + str(total) + " +++")

    
if __name__ == '__main__': 
    main()
