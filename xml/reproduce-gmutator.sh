LANG=xml
S=$1 # seed index
TOOL=gmutator
GFILE_P=XMLParser.g4
GFILE_L=XMLLexer.g4

SG=${S}
ITER=0
MOD=0
((ITER=(S-1)/3))
((MOD=ITER%40))
if [ $MOD -ne 0 ]
then
((SG=S-3*MOD))
fi

cd ${TOOL}
rm -rf mutant*
mkdir mutant-run-${S}
cd ../../scripts
python3 gmutate.py ../${LANG}/${GFILE_P} mutant-run-${S} ${SG} ../${LANG}/${GFILE_L}

cd ../${LANG}/${TOOL}
grammarinator-process mutant-run-${S}/${GFILE_P} mutant-run-${S}/${GFILE_L} &> /dev/null

grammarinator-generate XMLGenerator.XMLGenerator -r document -o tests/input_${S}.in -d 20 -n 1 --random-seed ${S} --sys-path . -j=1 -s grammarinator.runtime.simple_space_serializer &> /dev/null
