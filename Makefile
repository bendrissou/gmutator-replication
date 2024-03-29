include config
SHELL := /bin/bash # Use bash syntax

########### Global Variables

SUT = all # parson
SUTS =cjson parson simdjson
TOOL = 
TOOLS = grammarinator grammarinator+mutations gmutator
LANG =xml
LANGS=json lua xml url
TIME = $(GEN_TIME)
INTERVAL = $(COV_INTERVAL)
#ORGTIME = $(GEN_TIME_OG)
RUNS = $(REPS)
RUN = 1
########### Main target

all:
	@mkdir -p results
	@r=0 ; while [[ $$r -lt $(RUNS) ]] ; do \
		((r = r + 1)) ; \
		for sut in $(SUTS) ; do \
			for tool in $(TOOLS) ; do \
				echo -e "\n> Generation run" $$r":" $$sut "/" $$tool "... " ; \
				echo -e "  Compiling SUT ... " ; \
				$(MAKE) -s compile RUN=$$r TOOL=$$tool LANG=$(LANG) SUT=$$sut &> /dev/null ; \
				echo -e "  Generating inputs ... " ; \
				$(MAKE) -s generate_$$tool RUN=$$r TOOL=$$tool TIME=$(TIME) LANG=$(LANG) SUT=$$sut ; \
			done ; \
		done ; \
	done
	@$(MAKE) -s -B results

all-parallel:
	tmux new-session -d -s cjson
	tmux send-keys -t cjson 'make LANG=json SUTS=cjson' C-m
	tmux new-session -d -s parson
	tmux send-keys -t parson 'make LANG=json SUTS=parson' C-m
	tmux new-session -d -s simdjson
	tmux send-keys -t simdjson 'make LANG=json SUTS=simdjson' C-m
	tmux new-session -d -s luac
	tmux send-keys -t luac 'make LANG=lua SUTS=luac' C-m
	tmux new-session -d -s luajit
	tmux send-keys -t luajit 'make LANG=lua SUTS=luajit' C-m
	tmux new-session -d -s py-lua-parser
	tmux send-keys -t py-lua-parser 'make LANG=lua SUTS=py-lua-parser' C-m
	tmux new-session -d -s aria2
	tmux send-keys -t aria2 'make LANG=url SUTS=aria2' C-m
	tmux new-session -d -s curl
	tmux send-keys -t curl 'make LANG=url SUTS=curl' C-m
	tmux new-session -d -s wget
	tmux send-keys -t wget 'make LANG=url SUTS=wget' C-m
	tmux new-session -d -s fast-xml-parser
	tmux send-keys -t fast-xml-parser 'make LANG=xml SUTS=fast-xml-parser' C-m
	tmux new-session -d -s libxml2
	tmux send-keys -t libxml2 'make LANG=xml SUTS=libxml2' C-m
	tmux new-session -d -s pugixml
	tmux send-keys -t pugixml 'make LANG=xml SUTS=pugixml' C-m
	
########### Test Generation
	
generate_grammarinator:
	@cd ${LANG} && ./generate-grammarinator.sh $(RUN) $(TIME) $(LANG) $(SUT) $(INTERVAL) #> /dev/null

generate_grammarinator+mutations:
	@cd ${LANG} && ./generate-grammarinator-mut.sh $(RUN) $(TIME) $(LANG) $(SUT) $(INTERVAL) #> /dev/null

generate_gmutator:
	@cd ${LANG} && ./generate-gmutator.sh $(RUN) $(TIME) $(LANG) $(SUT) $(INTERVAL) #> /dev/null

########### Show results

results:
	@for sut in $(SUTS) ; do \
		for tool in $(TOOLS) ; do \
			cd scripts && python3 plot.py $$tool $(LANG) $$sut $(RUNS) ; \
			cd .. ; \
		done ; \
	done

########### Compile SUTs

compilexxx:
	@for sut in $(SUTS) ; do \
		cd bench/${LANG}/$$sut && make cov &> /dev/null ; \
		cd ../../.. ; \
	done

compile: prepare_sut
	@if [ ${LANG} = "json" ]; then \
		cd bench/${LANG}/run-${RUN}-${TOOL}-${SUT} && make clean && make cov &> /dev/null ; \
	fi
	if [ ${SUT} = "luac" ] || [ ${SUT} = "luajit" ] || [ ${SUT} = "aria2" ] || [ ${SUT} = "curl" ] ; then \
		cd bench/${LANG}/run-${RUN}-${TOOL}-${SUT}/src && rm -f *.gcda *.gcno &> /dev/null ; \
		cd .. && make clean && make &> /dev/null ; \
	fi
	if [ ${SUT} = "wget" ] ; then \
		cd bench/${LANG}/run-${RUN}-${TOOL}-${SUT} ; \
		./configure --enable-code-coverage ; \
		make &> /dev/null ; \
	fi
	if [ ${SUT} = "libxml2" ] ; then \
		cd bench/${LANG}/run-${RUN}-${TOOL}-${SUT} && aclocal && automake --add-missing && ./configure --with-coverage && make clean && make &> /dev/null ; \
	fi
	if [ ${SUT} = "pugixml" ] ; then \
		cd bench/${LANG}/run-${RUN}-${TOOL}-${SUT} && make clean && make &> /dev/null ; \
	fi
	
prepare_sut:
	rm -rf bench/${LANG}/run-${RUN}-${TOOL}-${SUT}
	if [ ${SUT} = "wget" ] ; then \
		cd bench/${LANG} && tar -xf wget-1-21-3.tar.gz ; \
		mv wget-1.21.3 run-${RUN}-${TOOL}-${SUT} ; \
	else \
		cp -r bench/${LANG}/${SUT} bench/${LANG}/run-${RUN}-${TOOL}-${SUT} ; \
	fi
	

########### Clean
		
clean:
	rm -rf results
	for lang in $(LANGS) ; do \
		rm -rf bench/$$lang/run* ; \
		rm -rf $$lang/grammarinator/tests ; \
		rm -rf $$lang/grammarinator+mutations/tests ; \
		rm -rf $$lang/gmutator/tests ; \
	done

