#!/bin/sh
cd ${0%/*} || exit 1    # run from this directory

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

cd rotor/
./cleanCase.sh 
./run.sh
cd ../stator/
./cleanCase.sh
./run.sh
cd ../Test/
./clean.sh
./makeMesh.sh
# ----------------------------------------------------------------- end-of-file
