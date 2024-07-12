# Gmutator code and experiments

This is the code repository for the [paper](https://dl.acm.org/doi/10.1145/3605157.3605170) "Grammar Mutation for Testing Input Parsers (Registered Report)". The paper evaluates three input generation techniques: Grammarinator, Grammarinator+Mutations, and Gmutator. The latter two are built on top of [Grammarinator](https://github.com/renatahodovan/grammarinator); a grammar-based input generator.

## Gmutator

Our tool, Gmutator, first mutates the input grammar, then the mutant grammar is fed to Grammarinator, to generate program inputs. 

A grammar mutation is a small change to an input grammar, that when applied, it alters the input space of the grammar. The goal is to generate new inputs that are not represented by the source grammar. Our implementation can be found in [gmutate.py](./scripts/gmutate.py).

## Grammarinator+Mutations

The second technique, Grammarinator+Mutations, takes as input a Grammarinator generated string, applies string mutations, and produces a new mutated string.

A string mutation is a blind mutation applied to a string at the character or byte level. The approach is implemented in [mutate-strings.py](./scripts/mutate-strings.py).


## Requirements

We recommend using the docker image stored in [the artefact](https://doi.org/10.5281/zenodo.10781796), which contains the following dependencies and more:
* **Python**: >= 3.7
* **grammarinator**: >= 19.3
* **antlr**: = 4.13.0
* **antlr4-python3-runtime**: = 4.13.0
* **plotext**: for plotting graphs on terminal.

**Minimum Hardware Requirements:**
* **CPU**: >= 14 cores
* **Memory**: >= 16 G
* **Disk**: >= 252 G

It is important to satisfy the above hardware requirements for a smooth run. We execute multiple tasks in parallel, and the compilation tasks consume significant amounts of memory.

## Getting started

Install the following software:

* Docker

Download the artefact file `artefact.tar.gz` from Zenodo:
```
https://doi.org/10.5281/zenodo.10781796
```

Check the file hash:

```sh
md5sum artefact.tar.gz
07a989e49909dc4f2487b9320b07bceb  artefact.tar.gz
```

### Importing the image

Execute the following command to load the docker image:

```sh
tar -xzf artefact.tar.gz
cd gmutator-replication
docker load -i image.tar
Loaded image: gmutator-replication:all
```

### Bring up the virtual container

The following command will bring up the virtual container, and access the container.

```sh
docker run --name gmutator-replication --network none -it gmutator-replication:all /bin/bash
```

## Evaluation

We selected antlr grammars for four input formats, derived from the [antlr repository](https://github.com/antlr/grammars-v4). Target input formats are:

* JSON
* LUA 
* URL 
* XML

For each grammar, we selected 3 systems under test (SUTs) that consume the inputs expressed by the grammar. In total we have 12 SUTs:

* cjson
* parson
* simdjson
* luac
* luajit
* py-lua-parser
* aria2
* curl
* wget
* fast-xml-parser
* libxml2
* pugixml

All SUTs are included in the docker image, and can be found in folder `/home/gmutator-replication/bench`.

The SUTs are used as benchmarks to assess the performance of three tools:
* **Grammarinator**: A blackbox grammar-based input generator
* **Grammarinator+mutations**: Grammarinator, supplemented with a string mutation feature, that applies mutations to the strings produced by Grammarinator
* **Gmutator**: Grammarinator, supplemented with a grammar mutation feature, that applies mutations to the input grammar consumed by Grammarinator

The goal is test how effective each tool is, at testing computer programs and input parsers in particular. We developed a testing framework that enables us to measure the following:
* **Parsing discrepancies**: Detect inputs that are not derivable by the grammar, but are accepted by one of the corresponding SUTs. Additionally, record inputs that are accepted by one SUT, but not by other SUTs in the same category.
* **Code coverage**: We measure branch coverage achieved for every tool/SUT pair.
* **Program crashes**: For all SUT runs, record any instance of  a crash and the crashing input.

## How to run

For example, to run experiments for two json SUTs: cjson and parson, 4 seconds time generation each, 1 repetition, and all three tools. We do the following:
```sh
make TIME=4 RUNS=1 TOOLS='grammarinator grammarinator+mutations gmutator' SUTS='cjson parson' LANG=json
```

Output:
```
> Generation run 1: cjson / grammarinator ... 
  Compiling SUT ... 
  Generating inputs ... 

> Generation run 1: cjson / grammarinator+mutations ... 
  Compiling SUT ... 
  Generating inputs ... 

> Generation run 1: cjson / gmutator ... 
  Compiling SUT ... 
  Generating inputs ... 

> Generation run 1: parson / grammarinator ... 
  Compiling SUT ... 
  Generating inputs ... 

> Generation run 1: parson / grammarinator+mutations ... 
  Compiling SUT ... 
  Generating inputs ... 

> Generation run 1: parson / gmutator ... 
  Compiling SUT ... 
  Generating inputs ... 

======================================================================

>> Evaluation results for grammarinator / cjson (1 runs)

Num of Inputs:   7  (0.00)
Accept Invalid:  0  (0.00)
Reject Valid:  0  (0.00)
Branch Coverage: 0  (0.00)
Crashes:   0  (SUM)

======================================================================

>> Evaluation results for grammarinator+mutations / cjson (1 runs)

Num of Inputs:   7  (0.00)
Accept Invalid:  0  (0.00)
Reject Valid:  0  (0.00)
Branch Coverage: 0  (0.00)
Crashes:   0  (SUM)

======================================================================

>> Evaluation results for gmutator / cjson (1 runs)

Num of Inputs:   5  (0.00)
Accept Invalid:  0  (0.00)
Reject Valid:  0  (0.00)
Branch Coverage: 0  (0.00)
Crashes:   0  (SUM)

======================================================================

>> Evaluation results for grammarinator / parson (1 runs)

Num of Inputs:   6  (0.00)
Accept Invalid:  0  (0.00)
Reject Valid:  0  (0.00)
Branch Coverage: 0  (0.00)
Crashes:   0  (SUM)

======================================================================

>> Evaluation results for grammarinator+mutations / parson (1 runs)

Num of Inputs:   6  (0.00)
Accept Invalid:  2  (0.00)
Reject Valid:  0  (0.00)
Branch Coverage: 0  (0.00)
Crashes:   0  (SUM)

======================================================================

>> Evaluation results for gmutator / parson (1 runs)

Num of Inputs:   5  (0.00)
Accept Invalid:  2  (0.00)
Reject Valid:  0  (0.00)
Branch Coverage: 0  (0.00)
Crashes:   0  (SUM)
```

After execution completes, we output final code branch coverage, crashes found and the number of parsing dicrepancies detected. The results are stored in files under folder `results`. Each file stores results of 1 run / 1 SUT / 1 tool. Correspondigly, file names have the following format: RUN-TOOL-SUT.txt e.g `run-1-gmutator-cjson.txt` stores evalaution data of the first run for every input generated by Gmutator, and executed by cjson. Lets take a look inside the file.

```sh
head results/run-1-gmutator-cjson.txt
```

Output:
```
[1, 'gmutator', 'json', '1', 'cjson', 0, 0, 0, -1, 1]
[2, 'gmutator', 'json', '4', 'cjson', 0, 0, 0, -1, 1]
[2, 'gmutator', 'json', '7', 'cjson', 0, 0, 0, -1, 0]
[3, 'gmutator', 'json', '10', 'cjson', 0, 0, 0, -1, 1]
[4, 'gmutator', 'json', '13', 'cjson', 0, 0, 0, -1, 0]
```
Each line in of the form:

[time(s), tool, format, seed, SUT, accept_invalid, reject_valid, crashes, coverage, SUT_valid]

The coverage is 0 initially, because `gcovr` was neved invoked. This is due to the long time interval between gcovr invocations (default interval is 600 seconds). We can change configuration by editing the `config` file. Default configurations. Let's change configurations to the following:

```
GEN_TIME=36 # default generation time (in seconds)
COV_INTERVAL=6 # time interval between gcovr invocations (in seconds)
INPUTS_PER_GRAMMAR=4 # number of inputs to generate from each mutated grammar 
REPS=1 # number of repetitions (runs)
```

Next, we can run the new experiment, this time on all three json SUTs:
```sh
make TOOLS='grammarinator grammarinator+mutations gmutator' SUTS='cjson parson simdjson' LANG=json
```


After running the experiments as above, we can output the results for a specific target, with the following command:
```sh
cd scripts
python3 plot.py gmutator json parson 1
```
This shows the performance of gmutator tool on a json parser (parson), for one run:
```
>> Evaluation results for gmutator / parson (1 runs)

Num of Inputs:   45  (0.00)
Accept Invalid:  8  (0.00)
Reject Valid:  1  (0.00)
Branch Coverage: 26  (0.00)
Crashes:   0  (SUM)
```

To compare the number of parsing discrepancies found by a given tool, on different SUTs of the same input format (all SUTs of the target format should be run first). Run the following:
```sh
cd scripts
python3 sut-diff.py grammarinator cjson 1
```

In the above example, we do differential testing on all of the three json SUTs, on grammarinator-generated inputs, and on one run of input generation. It's important that the corresponding result files are present.

## Reproduce results

The provided docker image contains the artefact used in the paper. To reproduce the experiment results reported in the paper, first make sure you are using the default configurations.

 ```sh
cat config
```

Output:
```
GEN_TIME=86400 # default generation time (in seconds)
COV_INTERVAL=600 # time interval between gcovr invocations (in seconds)
INPUTS_PER_GRAMMAR=40 # number of inputs to generate from each mutated grammar 
REPS=3 # number of repetitions (runs)
 ```

Next, run:

```sh
make all-parallel
```

Our experiments require (4 input formats) × (3 SUTs per input format) × (3 generation tools) × (3 repeat runs) × (24 h per repeat run) = 2,592 hours of CPU time.


The make command will launch 12 tmux sessions in parallel. So expect around 9 days for the experiments to complete.

Once completed, you can view the results of each SUT run. The following command outputs all results for cjson:

```sh
make -B results LANG=json SUTS=cjson 
```

## Reuse Gmutator

Gmutator is impelemented in [gmutate.py](./scripts/gmutate.py) script. In this section, we want to demonstrate how we can apply Gmutator to any antlr grammar. Therefore, as an example, we will use an antlr grammar for the CSV language `CSV.g4`. First obtain the grammar file, then place it in the root direcotry of the project.

 ```sh
cat CSV.g4
```

Output:
```
grammar CSV;

csvFile
    : hdr row+ EOF
    ;

hdr
    : row
    ;

row
    : field (',' field)* '\r'? '\n'
    ;

field
    : TEXT
    | STRING
    |
    ;

TEXT
    : ~[,\n\r"]+
    ;

STRING
    : '"' ('""' | ~'"')* '"'
    ; // quote-quote is an escaped quote
 ```


Next, setup some directories:

 ```sh
mkdir -p csv/gmutator/mutant-g
cp CSV.g4 csv
 ```

Then, execute Gmutator. Gmutator takes as arguments the source grammar, the destination folder, and a seed integer:

 ```sh
cd scripts
python3 gmutate.py ../csv/CSV.g4 mutant-g 1
cd ../csv
```

In cases where the antlr grammar is composed of two files: parser and lexer files. The python command above is the same, except that we add a fourth parameter, which is the lexer file path.

Now, let's examine the mutations applied:

```sh
diff CSV.g4 gmutator/mutant-g/CSV.g4
```

Output:
```
4c4
<     : hdr row+ EOF
---
>     : (hdr | field) (row | hdr)+ EOF
16c16
<     : TEXT
---
>     : TEXT*
```

We can run the same steps to apply Gmutator to other anltr grammars.

