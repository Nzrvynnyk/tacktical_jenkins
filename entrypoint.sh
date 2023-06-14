#!/bin/bash 

git fetch origin master
git reset --hard origin/master

if [ $# -gt 0 ]; then
    echo "Executing additional commands: $@"
    "$@"
else
    sleep 100000
fi