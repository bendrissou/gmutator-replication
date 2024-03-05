S=$1 # seed index
TOOL=grammarinator
GFILE=url.g4

cd ${TOOL}
grammarinator-process ../${GFILE} &> /dev/null #--no-actions
grammarinator-generate urlGenerator.urlGenerator -r url -o tests/input_${S}.in -n 1 --random-seed ${S} --sys-path . -j=1
