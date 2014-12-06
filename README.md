AMI_cases
=========

Repository for 2D rotor-stator type meshes

Every case file in this repository has at least the following three files. 

1) Rotor : This file generates the mesh of the rotating inner part. The mesh is generated using a blockMesh file
   which is generated using a python code https://github.com/pruthvi1991/python/blob/master/rotor_blockmesh.py

2) Stator : This file generates the mesh of the stationary outer part. Same as above        
   https://github.com/pruthvi1991/python/blob/master/stator_blockmesh.py

3) Test : This file merges the rotor and stator into a single mesh. Run the script makeMesh. After this step go to 
   Test/cylinder_AMI/constant/polyMesh/boundary and add the following lines to both couple1 and couple2.
   
couple2

        {
	        type            cyclicAMI;
	        nFaces          60;
	        startFace       306735;
	        neighbourPatch	couple1; // These are the lines that need to be added to the boundary file
	        matchTolerance	0.0001;  // These are the lines that need to be added to the boundary file
	        transform	noOrdering;    // These are the lines that need to be added to the boundary file
        }
	   
4) Now we must be good to go. Run the serial_run or the parallel_run scripts. There is a topoSet command in both      the files which will select all the cells in the rotor region and mark them as a seperate cell region called       rotor.

5) You can check if the mesh is working properly by using the moveDynamicMesh command. 

Extra Information :

1) The python scripts do not generate a foam header file. You must copy paste it or you can implement it in the code itself.

2) In the rotor meshing process there is a tranformPoints command since snappyHexMesh cannot deal with cells with less than 8 vertices and my .obj file is intersecting with these 6 vertexed cells. I moved the mesh to accomodate for this. You may have to do some other tranformation.

3) The AMI-bugfixing file has a folder called simple to calculate the steady state solution and map it as the initial condition to the transient solver. This is the same process that is in the wingMotion tutorial.
