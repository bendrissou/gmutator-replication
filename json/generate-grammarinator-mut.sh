RUN=$1
RUNTIME=$2
LANG=$3
SUT=$4
S=${RUN} # seed index
TIME=0
TOOL=grammarinator+mutations
GFILE=JSON.g4
INTERVAL=$5
THRESHOLD=${INTERVAL}

rm -f ../results/run-${RUN}-${TOOL}-${SUT}.txt
touch ../results/run-${RUN}-${TOOL}-${SUT}.txt

cd ${TOOL} 
grammarinator-process ../${GFILE} &> /dev/null #--no-actions

end=$((SECONDS+$RUNTIME))
start=$((SECONDS))

while [ $SECONDS -lt $end ]; do
    grammarinator-generate JSONGenerator.JSONGenerator -r json -o tests/input_${RUN}_${SUT}.in -d 60 -n 1 --random-seed ${S} --sys-path . -j=1
    ((TIME=SECONDS-start))
    cd ../../scripts
    python3 mutate-strings.py ${RUN} ${LANG} ${SUT} ${S}
    GET_COV=false
    if [ $TIME -ge $THRESHOLD ] ; then
    	GET_COV=true
    	((THRESHOLD=THRESHOLD+INTERVAL))
    fi
    python3 evaluate-input.py ${RUN} ${TIME} ${TOOL} ${LANG} ${SUT} ${S} ${GET_COV}
    cd ../${LANG}/${TOOL}
    ((S=S+3))
done


