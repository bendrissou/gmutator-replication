source ../config
RUN=$1
RUNTIME=$2
LANG=$3
SUT=$4
S=${RUN} # seed index
I=0 # Iteration. Used to track the number of inputs generated thus far.
TIME=0
TOOL=gmutator
GFILE=Lua.g4
INTERVAL=$5
THRESHOLD=${INTERVAL}

rm -f ../results/run-${RUN}-${TOOL}-${SUT}.txt
touch ../results/run-${RUN}-${TOOL}-${SUT}.txt

cd ${TOOL}

end=$((SECONDS+$RUNTIME))
start=$((SECONDS))

while [ $SECONDS -lt $end ]; do
    # Generate a new mutant grammar, if enough inputs have been generated.
    if (( $I % $INPUTS_PER_GRAMMAR == 0 ))
    then
    rm -rf mutant-run-${RUN}-${SUT}
    mkdir mutant-run-${RUN}-${SUT}
    cd ../../scripts
    python3 gmutate.py ../${LANG}/${GFILE} mutant-run-${RUN}-${SUT} ${S}

    cd ../${LANG}/${TOOL}/mutant-run-${RUN}-${SUT}
    grammarinator-process ${GFILE} &> /dev/null
    cd ..
    fi
    cd mutant-run-${RUN}-${SUT}

    grammarinator-generate LuaGenerator.LuaGenerator -r chunk -d 20 -o ../tests/input_${RUN}_${SUT}.in -n 1 --random-seed ${S} --sys-path . -s grammarinator.runtime.simple_space_serializer -j=1 &> /dev/null
    EXIT_CODE=$?
    
    # In case there was a fatal error, and no input got generated, we move to the next iteration.
    if [ $EXIT_CODE -ne 0 ]; then
        echo 'EXIT code not equal 0 !'
        ((S=S+3))
        ((I=I+1))
        cd ..
        continue
    fi

    ((TIME=SECONDS-start))

    cd ../../../scripts
    GET_COV=false
    if [ $TIME -ge $THRESHOLD ] ; then
    	GET_COV=true
    	((THRESHOLD=THRESHOLD+INTERVAL))
    fi
    python3 evaluate-input.py ${RUN} ${TIME} ${TOOL} ${LANG} ${SUT} ${S} ${GET_COV}
    cd ../${LANG}/${TOOL}
    ((S=S+3))
    ((I=I+1))
done

