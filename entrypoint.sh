#!/bin/bash 

git pull -f

if [ $# -gt 0 ]; then
    echo "Executing additional commands: $@"
    "$@"
else
    sleep 100000
fi