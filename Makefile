include config
SHELL := /bin/bash # Use bash syntax

########### Global Variables

SUT = all # parson
SUTS =cjson parson simdjson aria2 curl wget luac luajit py-lua-parser fast-xml-parser libxml2 pugixml
STATUS_FILES = $(addprefix .done_,$(SUTS))
TOOL = 
TOOLS = grammarinator grammarinator+mutations gmutator
LANG =xml
LANGS=json lua xml url
TIME = $(GEN_TIME)
INTERVAL = $(COV_INTERVAL)
#ORGTIME = $(GEN_TIME_OG)
RUNS = $(REPS)
RUN = 1

########### Main targets

generate:
	@r=0 ; while [[ $$r -lt $(RUNS) ]] ; do \
		((r = r + 1)) ; \
		for sut in $(SUTS) ; do \
			for tool in $(TOOLS) ; do \
				lang=$$(./scripts/set-lang.sh $$sut) ; \
				if [[ $$? -ne 0 ]] ; then \
					echo "Error: Unknown SUT $$sut" >&2 ; \
					exit 1 ; \
					fi ; \
				echo -e "\n> Generation run" $$r":" $$sut "/" $$tool ; \
				echo -e "  Compiling SUT ... " ; \
				$(MAKE) -s compile RUN=$$r TOOL=$$tool LANG=$$lang SUT=$$sut &> /dev/null ; \
				echo -e "  Generating inputs ... " ; \
				$(MAKE) -s generate_$$tool RUN=$$r TOOL=$$tool TIME=$(TIME) LANG=$$lang SUT=$$sut ; \
			done ; \
		done ; \
	done

all:
	@$(MAKE) -s generate
	@$(MAKE) -s process-results
	@$(MAKE) -s show-results

all-parallel: close_tmux_sessions $(STATUS_FILES) print-info

$(STATUS_FILES):
	@touch $@
	@tmux new-session -d -s $(@:.done_%=%)
	@tmux send-keys -t $(@:.done_%=%) 'make SUTS=$(@:.done_%=%) && rm $@' C-m

wait-parallel: $(STATUS_FILES)
	@while [ -n "$$(ls .done_* 2>/dev/null)" ]; do sleep 1; done
	@echo -e "\n++ All parallel jobs are done."

post-process: wait-parallel
	@$(MAKE) -s process-results
	@$(MAKE) -s show-results

print-info:
	@echo -e "\n++ Experiments starting"
	@echo -e "\n++ Estimated execution time: $(shell echo $$((($(RUNS) * $(TIME) + 1800 * $(RUNS) + 3599) / 3600))) hour(s)"
	@echo -e "\n++ All tmux sessions started"

########### Test Generation
	
generate_grammarinator:
	@cd ${LANG} && ./generate-grammarinator.sh $(RUN) $(TIME) $(LANG) $(SUT) $(INTERVAL) #> /dev/null

generate_grammarinator+mutations:
	@cd ${LANG} && ./generate-grammarinator-mut.sh $(RUN) $(TIME) $(LANG) $(SUT) $(INTERVAL) #> /dev/null

generate_gmutator:
	@cd ${LANG} && ./generate-gmutator.sh $(RUN) $(TIME) $(LANG) $(SUT) $(INTERVAL) #> /dev/null

########### Show results

process-results:
	@echo -e "\n++ Processing results ... "
	@cd scripts && python3 clear-results.py
	@cd scripts ; \
	for sut in $(SUTS) ; do \
		for tool in $(TOOLS) ; do \
			python3 process-results.py $$tool $(LANG) $$sut $(RUNS) ; \
		done ; \
	done
	@echo -e "\n>> Processing differential coverage for: cjson parson simdjson aria2 curl wget luac luajit libxml2 pugixml "
	@cd scripts && python3 lines_diff.py --sut cjson --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut parson --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut simdjson --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut aria2 --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut curl --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut wget --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut luac --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut luajit --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut libxml2 --runs $(RUNS)
	@cd scripts && python3 lines_diff.py --sut pugixml --runs $(RUNS)
	@echo -e "\n>> Processing differential coverage for py-lua-parser "
	@cd scripts && python3 lines_diff_py.py $(RUNS)
	@echo -e "\n>> Processing differential coverage for fast-xml-parser "
	@cd scripts && python3 lines_diff_js.py $(RUNS)
	@echo -e "\n++ Done processing results. "

show-results:
	@echo -e "\n\n>> Results for Table 2 and Figure 3 in paper >> "
	@cd scripts && python3 show-table-2-fig-3.py
	@echo -e "\n\n>> Results for Table 4 in paper >> "
	@cd scripts && python3 show-table-4.py
	@echo -e "\n"

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
		
clean: close_tmux_sessions
	rm -rf results
	@cd scripts && python3 clear-results.py
	for lang in $(LANGS) ; do \
		rm -rf bench/$$lang/run* ; \
		rm -rf $$lang/grammarinator/tests ; \
		rm -rf $$lang/grammarinator+mutations/tests ; \
		rm -rf $$lang/gmutator/tests ; \
	done

close_tmux_sessions:
	@# Iterate over each session name in SUTS and kill the session if it exists
	@for session in $(SUTS); do \
		tmux has-session -t $$session 2>/dev/null && tmux kill-session -t $$session || true; \
	done
	-@rm -f .done_*
