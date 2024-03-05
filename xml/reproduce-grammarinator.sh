S=$1 # seed index
TOOL=grammarinator
GFILE_P=XMLParser.g4
GFILE_L=XMLLexer.g4

cd ${TOOL}
grammarinator-process ../${GFILE_P} ../${GFILE_L} &> /dev/null #--no-actions

grammarinator-generate XMLGenerator.XMLGenerator -r document -o tests/input_${S}.in -d 20 -n 1 --random-seed ${S} --sys-path . -j=1 -s grammarinator.runtime.simple_space_serializer
