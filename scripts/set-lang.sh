#!/bin/bash

# Read SUT value from the environment or argument
SUT=${1:-$SUT}

# Determine the language based on the SUT value
case "$SUT" in
    cjson)
        echo "json"
        ;;
    parson)
        echo "json"
        ;;
    simdjson)
        echo "json"
        ;;
    luac)
        echo "lua"
        ;;
    luajit)
        echo "lua"
        ;;
    py-lua-parser)
        echo "lua"
        ;;
    aria2)
        echo "url"
        ;;
    curl)
        echo "url"
        ;;
    wget)
        echo "url"
        ;;
    fast-xml-parser)
        echo "xml"
        ;;
    libxml2)
        echo "xml"
        ;;
    pugixml)
        echo "xml"
        ;;

    *)
        echo "Error: Unknown SUT $SUT"
        exit 1
        ;;
esac
