S=$1
TOOL=grammarinator+mutations
GFILE=JSON.g4

cd ${TOOL} 
grammarinator-process ../${GFILE} &> /dev/null #--no-actions

grammarinator-generate JSONGenerator.JSONGenerator -r json -o tests/input_${S}.in -n 1 --random-seed ${S} --sys-path . -j=1

cd ../../scripts
python3 mutate-string-reproduce.py json ${S}


