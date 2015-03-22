#!/bin/sh
cd ${0%/*} || exit 1    # run from this directory

# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

# Make 3D mesh in slab of cells.
#cd wingMotion_snappyHexMesh
runApplication blockMesh
transformPoints -scale '(1 1 4.9)'
#runApplication topoSet
runApplication surfaceFeatureExtract
runApplication snappyHexMesh -overwrite
runApplication extrudeMesh
runApplication createPatch -overwrite
transformPoints -translate '(0 0 -0.99)'
paraFoam

# ----------------------------------------------------------------- end-of-file
