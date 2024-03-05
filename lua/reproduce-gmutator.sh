LANG=lua
S=$1 # seed index
TOOL=gmutator
GFILE=Lua.g4

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
python3 gmutate.py ../${LANG}/${GFILE} mutant-run-${S} ${SG}

cd ../${LANG}/${TOOL}
grammarinator-process mutant-run-${S}/${GFILE} &> /dev/null

grammarinator-generate LuaGenerator.LuaGenerator -r chunk -d 20 -o tests/input_${S}.in -n 1 --random-seed ${S} --sys-path . -s grammarinator.runtime.simple_space_serializer -j=1 &> /dev/null
