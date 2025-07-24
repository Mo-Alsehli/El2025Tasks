#!/bin/bash

# Force execution from the folder where this script lives
cd "$(dirname "$0")"

examine_session() {
    local session_dir="$1"
    cd "$session_dir" || exit 1
    for file in *.py; do
        pylint --disable=C0301 "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running pylint for $file"
            exit 1
        fi
        python "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running $file"
            exit 1
        fi
        echo "[🟩] $file ran successfully"
    done
    cd ..
}

#----------------- Session 1 -----------------#
examine_session "python/session1"

#----------------- Session 2 -----------------#
# Session 2
cd python/session2 || exit 1
python lab1_get_your_location.py
if [ $? -ne 0 ]; then
    echo "[🟥] Session 2 is not Solved yet"
    exit 1
else
    examine_session "."
fi
cd ../..

# Session 3
cd python/session3 || exit 1
python lab1_dictionary_problems.py
if [ $? -ne 0 ]; then
    echo "[🟥] Session 3 is not solved yet"
else
    examine_session "."
fi
cd ../..

