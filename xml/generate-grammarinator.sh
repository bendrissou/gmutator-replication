RUN=$1
RUNTIME=$2
LANG=$3
SUT=$4
S=${RUN} # seed index
TIME=0
TOOL=grammarinator
GFILE_P=XMLParser.g4
GFILE_L=XMLLexer.g4
INTERVAL=$5
THRESHOLD=${INTERVAL}

rm -f ../results/run-${RUN}-${TOOL}-${SUT}.txt
touch ../results/run-${RUN}-${TOOL}-${SUT}.txt

cd ${TOOL}
grammarinator-process ../${GFILE_P} ../${GFILE_L} &> /dev/null #--no-actions

end=$((SECONDS+$RUNTIME))
start=$((SECONDS))

while [ $SECONDS -lt $end ]; do
    grammarinator-generate XMLGenerator.XMLGenerator -r document -o tests/input_${RUN}_${SUT}.in -d 60 -n 1 --random-seed ${S} --sys-path . -j=1 -s grammarinator.runtime.simple_space_serializer
    ((TIME=SECONDS-start))
    cd ../../scripts
    GET_COV=false
    if [ $TIME -ge $THRESHOLD ] ; then
    	GET_COV=true
    	((THRESHOLD=THRESHOLD+INTERVAL))
    fi
    python3 evaluate-input.py ${RUN} ${TIME} ${TOOL} ${LANG} ${SUT} ${S} ${GET_COV}
    cd ../${LANG}/${TOOL}
    ((S=S+3))
done

cd ..
