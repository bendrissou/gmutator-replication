S=$1 # seed index
TOOL=grammarinator
GFILE=JSON.g4

cd ${TOOL}
grammarinator-process ../${GFILE} &> /dev/null #--no-actions
grammarinator-generate JSONGenerator.JSONGenerator -r json -o tests/input_${S}.in -n 1 --random-seed ${S} --sys-path . -j=1

