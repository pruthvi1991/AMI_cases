#!/bin/sh
cd ${0%/*} || exit 1    # run from this directory

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions
cp -r ../rotor rotor
cp -r ../stator stator
mergeMeshes -overwrite stator/ rotor/
mv stator/ cylinder_AMI/
#cd cylinder_AMI/
#runApplication topoSet
paraFoam

# ----------------------------------------------------------------- end-of-file
