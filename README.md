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

You can start by running a small-scale test. For example:

```sh
make all TIME=60 RUNS=1 TOOLS='grammarinator+mutations gmutator' SUTS='cjson'
```

This command sequentially runs the `cjson` System Under Test (SUT) with the Gmutator and Grammarinator+mutations tools, each for 60 seconds. The execution includes a post-processing step to process and display the results.

Output:
```
> Generation run 1: cjson / grammarinator+mutations
  Compiling SUT ... 
  Generating inputs ... 

> Generation run 1: cjson / gmutator
  Compiling SUT ... 
  Generating inputs ... 

++ Processing results ... 

>> Processing results for grammarinator+mutations / cjson (1 runs)

>> Processing results for gmutator / cjson (1 runs)

>> Processing differential coverage for: cjson parson simdjson aria2 curl wget luac luajit libxml2 pugixml 

>> Processing differential coverage for py-lua-parser 

>> Processing differential coverage for fast-xml-parser 

++ Done processing results. 


>> Results for Table 2 and Figure 3 in paper >> 

=============================================================================
         |                          Grammarinator                           |
-----------------------------------------------------------------------------
         |  inputs  | accept-invalid |  reject-valid  | coverage | crashes  |
-----------------------------------------------------------------------------
cjson    |       -1 |             -1 |             -1 |       -1 |       -1 |
parson   |       -1 |             -1 |             -1 |       -1 |       -1 |
simdjson |       -1 |             -1 |             -1 |       -1 |       -1 |
luac     |       -1 |             -1 |             -1 |       -1 |       -1 |
luajit   |       -1 |             -1 |             -1 |       -1 |       -1 |
py-lua   |       -1 |             -1 |             -1 |       -1 |       -1 |
aria2    |       -1 |             -1 |             -1 |       -1 |       -1 |
curl     |       -1 |             -1 |             -1 |       -1 |       -1 |
wget     |       -1 |             -1 |             -1 |       -1 |       -1 |
fast-xml |       -1 |             -1 |             -1 |       -1 |       -1 |
libxml2  |       -1 |             -1 |             -1 |       -1 |       -1 |
pugixml  |       -1 |             -1 |             -1 |       -1 |       -1 |

=============================================================================
         |                             Gmutator                             |
-----------------------------------------------------------------------------
         |  inputs  | accept-invalid |  reject-valid  | coverage | crashes  |
-----------------------------------------------------------------------------
cjson    |      105 |              1 |              1 |        0 |        0 |
parson   |       -1 |             -1 |             -1 |       -1 |       -1 |
simdjson |       -1 |             -1 |             -1 |       -1 |       -1 |
luac     |       -1 |             -1 |             -1 |       -1 |       -1 |
luajit   |       -1 |             -1 |             -1 |       -1 |       -1 |
py-lua   |       -1 |             -1 |             -1 |       -1 |       -1 |
aria2    |       -1 |             -1 |             -1 |       -1 |       -1 |
curl     |       -1 |             -1 |             -1 |       -1 |       -1 |
wget     |       -1 |             -1 |             -1 |       -1 |       -1 |
fast-xml |       -1 |             -1 |             -1 |       -1 |       -1 |
libxml2  |       -1 |             -1 |             -1 |       -1 |       -1 |
pugixml  |       -1 |             -1 |             -1 |       -1 |       -1 |

=============================================================================
         |                               G+M                                |
-----------------------------------------------------------------------------
         |  inputs  | accept-invalid |  reject-valid  | coverage | crashes  |
-----------------------------------------------------------------------------
cjson    |      100 |              1 |              0 |        0 |        0 |
parson   |       -1 |             -1 |             -1 |       -1 |       -1 |
simdjson |       -1 |             -1 |             -1 |       -1 |       -1 |
luac     |       -1 |             -1 |             -1 |       -1 |       -1 |
luajit   |       -1 |             -1 |             -1 |       -1 |       -1 |
py-lua   |       -1 |             -1 |             -1 |       -1 |       -1 |
aria2    |       -1 |             -1 |             -1 |       -1 |       -1 |
curl     |       -1 |             -1 |             -1 |       -1 |       -1 |
wget     |       -1 |             -1 |             -1 |       -1 |       -1 |
fast-xml |       -1 |             -1 |             -1 |       -1 |       -1 |
libxml2  |       -1 |             -1 |             -1 |       -1 |       -1 |
pugixml  |       -1 |             -1 |             -1 |       -1 |       -1 |


>> Results for Table 4 in paper >> 

================================
  Differential Line Coverage   |
--------------------------------
         | Gmutator |   G+M    |
--------------------------------
cjson    |       84 |       13 |
parson   |       -1 |       -1 |
simdjson |       -1 |       -1 |
luac     |       -1 |       -1 |
luajit   |       -1 |       -1 |
py-lua   |       -1 |       -1 |
aria2    |       -1 |       -1 |
curl     |       -1 |       -1 |
wget     |       -1 |       -1 |
fast-xml |       -1 |       -1 |
libxml2  |       -1 |       -1 |
pugixml  |       -1 |       -1 |

```

Results are first produced in file `results.json`, then printed in tables as shown above. Entries with a value of -1 indicate missing or incomplete evaluations.


During execution, we record code coverage, crashes found and the number of parsing dicrepancies detected. Raw results are stored in files under folder `results`. Each file stores results of 1 run / 1 SUT / 1 tool. Correspondingly, file names have the following format: RUN-TOOL-SUT.txt e.g `run-1-gmutator-cjson.txt` stores evaluation data of the first run for every input generated by Gmutator, and executed by `cjson`. Lets take a look inside the file.

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
```
[time(s), tool, format, seed, SUT, accept_invalid, reject_valid, crashes, coverage, SUT_valid]
```

The coverage is 0 initially, because `gcovr` was never invoked. This is due to the long time interval between `gcovr` invocations (default interval is 600 seconds). We can change configuration by editing the `config` file.

## Reproduce results

The provided docker image contains the artefact used in the paper. To reproduce the experiment results reported in the paper, first make sure to use the default configurations.

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

Running experiments with the above default configurations is expected to take approximately nine days. However, you can modify these settings as needed. For instance, reducing the number of repetitions to a single run will shorten the experiment duration to about three days. One run should be sufficient to reproduce the results detailed in the paper.

Next, to launch the full experiment in parallel mode, execute:

```sh
make all-parallel post-process
```

Our experiments require (4 input formats) × (3 SUTs per input format) × (3 generation tools) × (3 repeat runs) × (24 h per repeat run) = 2,592 hours of CPU time.


The make command will launch 12 tmux sessions in parallel. So expect around 9 days for the experiments to complete.

Once all threads have completed execution, the results are processed and displayed to the user automatically.

Alternatively, results can be read at a later stage by invoking the appropriate make command:


```sh
make show-results
```

The following is a sample output of a one hour run: 
```
>> Results for Table 2 and Figure 3 in paper >> 

=============================================================================
         |                          Grammarinator                           |
-----------------------------------------------------------------------------
         |  inputs  | accept-invalid |  reject-valid  | coverage | crashes  |
-----------------------------------------------------------------------------
cjson    |     5866 |              0 |             28 |       40 |        0 |
parson   |     5870 |              0 |            307 |       36 |        0 |
simdjson |     5840 |              0 |             90 |       12 |        0 |
luac     |     1578 |              0 |            101 |       36 |        0 |
luajit   |     1572 |              0 |           1463 |       22 |        0 |
py-lua   |     1334 |              0 |           1177 |       87 |        0 |
aria2    |     4746 |              0 |           1442 |        7 |        0 |
curl     |     5436 |              0 |            802 |        5 |        0 |
wget     |     5656 |              0 |            639 |       10 |        0 |
fast-xml |      631 |              0 |             23 |       48 |        0 |
libxml2  |     5383 |              0 |            580 |        3 |        0 |
pugixml  |     5477 |              0 |              0 |        7 |        0 |

=============================================================================
         |                             Gmutator                             |
-----------------------------------------------------------------------------
         |  inputs  | accept-invalid |  reject-valid  | coverage | crashes  |
-----------------------------------------------------------------------------
cjson    |     5607 |             55 |             19 |       41 |        0 |
parson   |     5604 |            307 |            171 |       38 |        0 |
simdjson |     5577 |              0 |             56 |       14 |        0 |
luac     |     2470 |              6 |             10 |       35 |        0 |
luajit   |     2454 |              0 |            488 |       22 |        0 |
py-lua   |     1951 |              1 |            285 |       88 |        0 |
aria2    |     4473 |            775 |            770 |        8 |        0 |
curl     |     4991 |            976 |            389 |        6 |        0 |
wget     |     5038 |           1022 |            278 |       11 |        0 |
fast-xml |      631 |             15 |             11 |       50 |        0 |
libxml2  |     5069 |             14 |            386 |        4 |        0 |
pugixml  |     5230 |            287 |             25 |        9 |        0 |

=============================================================================
         |                               G+M                                |
-----------------------------------------------------------------------------
         |  inputs  | accept-invalid |  reject-valid  | coverage | crashes  |
-----------------------------------------------------------------------------
cjson    |     5432 |             65 |              1 |       41 |        0 |
parson   |     5432 |           1374 |             22 |       38 |        0 |
simdjson |     5406 |              0 |              8 |       13 |        0 |
luac     |     1913 |              2 |              5 |       34 |        0 |
luajit   |     1882 |              0 |            122 |       22 |        0 |
py-lua   |     1552 |             39 |             93 |       88 |        1 |
aria2    |     4377 |           1032 |            226 |        8 |        0 |
curl     |     5048 |           1537 |            148 |        6 |        0 |
wget     |     5238 |           2423 |            102 |       11 |        0 |
fast-xml |      630 |             46 |             14 |       53 |        0 |
libxml2  |     4927 |              3 |            386 |        4 |        0 |
pugixml  |     5148 |            377 |            192 |        9 |        0 |


>> Results for Table 4 in paper >> 

================================
  Differential Line Coverage   |
--------------------------------
         | Gmutator |   G+M    |
--------------------------------
cjson    |        2 |        2 |
parson   |        3 |        3 |
simdjson |       56 |        3 |
luac     |      118 |       66 |
luajit   |       15 |       80 |
py-lua   |       10 |       13 |
aria2    |        0 |        8 |
curl     |        1 |        5 |
wget     |        0 |        0 |
fast-xml |        3 |       28 |
libxml2  |      254 |      167 |
pugixml  |       10 |       13 |
```

## Reuse Gmutator

Gmutator is impelemented in [gmutate.py](./scripts/gmutate.py) script. In this section, we want to demonstrate how we can apply Gmutator to any antlr grammar. Therefore, as an example, we will use an antlr grammar for the CSV language `CSV.g4`. First obtain the grammar file, then place it in the root directory of the project.

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

