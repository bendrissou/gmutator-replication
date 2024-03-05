S=$1
TOOL=grammarinator
GFILE=Lua.g4

cd ${TOOL}
grammarinator-process ../${GFILE} &> /dev/null #--no-actions
grammarinator-generate LuaGenerator.LuaGenerator -r chunk -d 20 -o tests/input_${S}.in -n 1 --random-seed ${S} --sys-path . -s grammarinator.runtime.simple_space_serializer -j=1
