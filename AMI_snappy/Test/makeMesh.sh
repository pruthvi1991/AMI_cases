#!/bin/sh
cd ${0%/*} || exit 1    # run from this directory

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions
cp -r ../rotor rotor
cp -r ../stator stator
mergeMeshes -overwrite stator/ rotor/
mv stator/ pimpleDyMFoam_AMI/
cd pimpleDyMFoam_AMI/
rm -r log*
mv _clean.sh clean.sh
mv system/createPatchDict_postmerged system/createPatchDict
runApplication createPatch -overwrite
runApplication topoSet
paraFoam

# ----------------------------------------------------------------- end-of-file
