#!/bin/sh
cd ${0%/*} || exit 1    # run from this directory

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/CleanFunctions

#cd wingMotion_snappyHexMesh
for i in 1 2 3 4 5 6 7 8 9
do
rm -r $i*
done
rm -r 0.*
#cleanCase

