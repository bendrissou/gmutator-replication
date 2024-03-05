S=$1 # seed index
TOOL=grammarinator+mutations
GFILE=url.g4

cd ${TOOL} 
grammarinator-process ../${GFILE} &> /dev/null #--no-actions

grammarinator-generate urlGenerator.urlGenerator -r url -o tests/input_${S}.in -n 1 --random-seed ${S} --sys-path . -j=1

cd ../../scripts
python3 mutate-string-reproduce.py url ${S}
