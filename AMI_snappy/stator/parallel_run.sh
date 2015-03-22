#!/bin/sh
cd ${0%/*} || exit 1    # run from this directory

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

cp -r 0_org/* 0/
#runApplication mapFields ../simple -sourceTime latestTime -consistent
runApplication decomposePar
runParallel `getApplication` 4
runApplication reconstructPar
paraFoam

# ----------------------------------------------------------------- end-of-file
