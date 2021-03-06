# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import math
ami_radius = 2.5
theta = math.pi
i = theta/2
j = 0 ; k = 0 ; l = 0 ; m = 0 # dummy indices
boundingbox_negative_x = -4*(ami_radius)  
boundingbox_positive_x = 4*(ami_radius)
boundingbox_negative_y = -4*(ami_radius)
boundingbox_positive_y = 4*(ami_radius)
rotor_cells = [10, 1, 10]    # Number of cells in rotor
stator_cells = [10, 1, 10]    # Number of cells in stator
rotor_grading = [1, 1, 1]    # Mesh grading of rotor
stator_grading = [1, 1, 1]    # Mesh grading of stator
X = [0]
Y = [0]
Z = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
v1 = []; v2 = []; v3 = []; v4 = []; v5 = []; v6 = []; v7 = []; v8 = []; # Lists to hold block vertices
edge_x = []; edge_y = [];    # Lists to hold edge values
rotor_face1 = []; rotor_face2 = []; rotor_face3 = []; rotor_face4 = []; # Lists to hold rotor ami face vertices
stator_face1 = []; stator_face2 = []; stator_face3 = []; stator_face4 = []; # Lists to hold stator ami face vertices
front1 = []; front2 = []; front3 = []; front4 = []; front5 = []; front6 = []; front7 = []; front8 = [] # Lists to hold front face vertices
back1 = []; back2 = []; back3 = []; back4 = []; back5 = []; back6 = []; back7 = []; back8 = []; # Lists to hold back face vertices

def vertex(x,y,z): #Function to print vertexes in OpenFoam format :: (x y z)
    v = '(' + str(x) + ' ' + str(y) + ' ' + str(z) + ')'
    return v

def face(x,y,z,p): #Function to print vertexes in OpenFoam format :: (x y z p)
    f = '(' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(p) + ')'
    return f

def block(x,y,z,p,q,r,s,t): #Function to print block in OpenFoam format :: hex (1 2 3 4 5 6 7 8)
    b = 'hex' + ' ' + '(' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(p) + ' ' + str(q)\
    + ' ' + str(r) + ' ' + str(s) + ' ' + str(t) + ')'
    return b

def edges(): # Function to print edges in OpenFoam format :: edge <vertex1> <vertex2> (x y z)
    print 'edges'
    print '('
    for j in range(1,6):
        print '    arc ' + str(j) + ' ' + str(j+1) + ' ' + '(' + str(edge_x[j]) + ' ' +\
        str(edge_y[j]) + ' ' + str(Z[j])+')' + '     //e' + str(j)
    print '    arc ' + str(6) + ' ' + str(1) + ' ' + '(' + str(edge_x[5]) + ' ' +\
        str(edge_y[5]) + ' ' + str(Z[5])+')' + '     //e' + str(6)
    for k in range(0,5):
        print '    arc ' + str(k+14) + ' ' + str(k+15) + ' ' + '(' + str(edge_x[k]) + ' ' +\
        str(edge_y[k]) + ' ' + str(-Z[k])+')' + '     //e' + str(k+7)
    print '    arc ' + str(19) + ' ' + str(14) + ' ' + '(' + str(edge_x[5]) + ' ' +\
        str(edge_y[5]) + ' ' + str(Z[5])+')' + '     //e' + str(12)
    for j in range(0,5):
        print '    arc ' + str(j+26) + ' ' + str(j+27) + ' ' + '(' + str(edge_x[j]) + ' ' +\
        str(edge_y[j]) + ' ' + str(Z[j])+')' + '     //e' + str(j + 13)
    print '    arc ' + str(31) + ' ' + str(26) + ' ' + '(' + str(edge_x[5]) + ' ' +\
        str(edge_y[5]) + ' ' + str(Z[5])+')' + '     //e' + str(18)
    for k in range(0,5):
        print '    arc ' + str(k+32) + ' ' + str(k+33) + ' ' + '(' + str(edge_x[k]) + ' ' +\
        str(edge_y[k]) + ' ' + str(-Z[k])+')' + '     //e' + str(k+19)
    print '    arc ' + str(37) + ' ' + str(32) + ' ' + '(' + str(edge_x[5]) + ' ' +\
        str(edge_y[5]) + ' ' + str(Z[5])+')' + '     //e' + str(24)
    print ');'
        #return e

def vertices(): #Function to print vertices in OpenFoam format :: vertices (<  >);
    print 'vertices'
    print '('
    for j in range(0,7):
        print '    ' + vertex(X[j], Y[j], Z[j]) + '      //v' +str(j)+ ' ~rotor_stator_interface_top'
    for j in range(7,13):
        print '    ' + vertex(X[j], Y[j], Z[j]) + '      //v' +str(j)+ ' ~bounding_box_top'
    for j in range(0,7):
        print '    ' + vertex(X[j], Y[j], -Z[j]) + '     //v' +str(j+13) + ' ~rotor_stator_interface_bottom'
    for j in range(7,13):
        print '    ' + vertex(X[j], Y[j], -Z[j]) + '     //v' +str(j+13)+ ' ~bounding_box_bottom'
    for j in range(1,7):
        print '    ' + vertex(X[j], Y[j], +Z[j]) + '     //v' +str(j+25)+ ' ~stator_rotor_interface_top'
    for j in range(1,7):
        print '    ' + vertex(X[j], Y[j], -Z[j]) + '     //v' +str(j+31)+ ' ~stator_rotor_interface_bottom'
    print ');'
    
def blocks(): #Function to print blocks in OpenFoam format :: blocks (<  >);
    print 'blocks'
    print '('
    for j in range(0,5):
        print '    ' + block(v7[j], v8[j], v5[j], v6[j], v3[j], v4[j], v1[j], v2[j])\
        + ' (' + str(rotor_cells[0]) + ' ' + str(rotor_cells[1]) + ' ' + str(rotor_cells[2]) + ')' \
        + ' simpleGrading ' + '(' + ' ' + str(rotor_grading[0]) + ' ' + str(rotor_grading[1]) \
        + ' ' + str( rotor_grading[2]) + ')' + ' //' + 'b' + str(j+1) + ' ~rotor'
    print '    hex (' + str(0) + ' ' + str(0) + ' ' + str(13) + ' ' + str(13) + ' ' + str(1)\
    + ' ' + str(6) + ' ' + str(19) + ' ' + str(14) + ')' + ' (' + str(rotor_cells[0]) + ' ' \
    + str(rotor_cells[1]) + ' ' + str(rotor_cells[2]) + ')' + ' simpleGrading ' + '(' \
    + str(rotor_grading[0]) + ' ' + str(rotor_grading[1]) + ' ' + str(rotor_grading[2]) \
    + ')' + '  ' '//b12' + ' ~rotor'
    for j in range(5,10):
        print '    ' + block(v1[j], v2[j], v3[j], v4[j], v5[j], v6[j], v7[j], v8[j])\
        + ' (' + str(stator_cells[0]) + ' ' + str(stator_cells[1]) + ' ' + str(stator_cells[2]) + ')' \
        + ' simpleGrading ' + '(' + str(stator_grading[0]) + ' ' + str(stator_grading[1]) \
        + ' ' + str(stator_grading[2]) + ')' + ' //' + 'b' + str(j+1) + ' ~stator'
    print '    hex (' + str(37) + ' ' + str(32) + ' ' + str(26) + ' ' + str(31) + ' ' + str(25)\
    + ' ' + str(20) + ' ' + str(7) + ' ' + str(12) + ')' + ' (' + str(stator_cells[0]) + ' ' \
    + str(stator_cells[1]) + ' ' + str(stator_cells[2]) + ')' + ' simpleGrading ' + '(' \
    + str(stator_grading[0]) + ' ' + str(stator_grading[1]) + ' ' + str(stator_grading[2]) \
    + ')' + '  ' '//b11' + ' ~stator'
    print ');'

def boundaries():
    print 'boundary\n('
    print '    inlet\n    {\n        type patch;\n        faces\n        ( \n        \
    (22 21 8 9)        \n        );\n    }\n\n    outlet\n    {\n        type patch;\n        \
faces\n        ( \n            (24 25 12 11)        \n        );\n    }\
\n\n    topandbottom\n    {\n        type patch;\n\n        faces\n        ( \n            (25 20 7 12)\n        \
    (24 23 10 11)\n            (20 21 8 7)\n            (23 22 9 10)\n        );\n    }'
    ami()
    
def ami():
    print '\n    AMI1\n    {\n        type     cyclicAMI;\n        neighbourPatch  AMI2;\n        \
transform    noOrdering;'  
    print '        faces\n        ('
    for j in range(0,5):
        print '            ' + face(rotor_face1[j], rotor_face2[j], rotor_face3[j], rotor_face4[j]) +\
        ' ' + '// rotor_face' + str(j+1) 
    print '            ' + '(' + str(14) + ' ' + str(19) + ' ' + str(6) + ' ' + str(1) + ')' + ' ' +\
    '// rotor_face' + str(6)
    print '        );\n    }'
    print '\n    AMI2\n    {\n        type     cyclicAMI;\n        neighbourPatch  AMI1;\n        \
transform    noOrdering;'  
    print '        faces\n        ('
    for j in range(0,5):
        print '            ' + face(stator_face1[j], stator_face2[j], stator_face3[j], stator_face4[j]) +\
        ' ' + '// stator_face' + str(j+1) 
    print '            ' + '(' + str(32) + ' ' + str(37) + ' ' + str(31) + ' ' + str(26) + ')' + ' ' +\
    '// stator_face' + str(6)
    print '        );\n    }'
    
def frontandback():
    print '    frontandback\n    {\n        type empty;\n        faces\n        ('
    for j in range(0,5):
        print '            ' + face(front1[j], front4[j], front2[j], front3[j]) + ' ' \
        + '    // rotor_front_face' + str(4*j + 1)
    print '            ' + '(' + str(0) + ' ' + str(0) + ' ' + str(6) + ' ' + str(1) + ')' \
    + ' ' + '    // rotor_front_face' + str(21)
    for j in range(0,5):
        print '            ' + face(front5[j], front6[j], front7[j], front8[j]) + ' ' \
        + '    // stator_front_face' + str(4*j + 2)
    print '            ' + '(' + str(31) + ' ' + str(12) + ' ' + str(7) + ' ' + str(26) + ')' \
    + ' ' + '    // stator_front_face' + str(22)
    for j in range(0,5):
        print '            ' + face(back1[j], back4[j], back2[j], back3[j]) + ' ' \
        + '    // rotor_back_face' + str(4*j + 3)
    print '            ' + '(' + str(13) + ' ' + str(13) + ' ' + str(19) + ' ' + str(14) + ')' \
    + ' ' + '    // rotor_back_face' + str(23)
    for j in range(0,5):
        print '            ' + face(back5[j], back6[j], back7[j], back8[j]) + ' ' \
        + '    // stator_back_face' + str(4*j + 4)
    print '            ' + '(' + str(32) + ' ' + str(37) + ' ' + str(25) + ' ' + str(20) + ')' \
    + ' ' + '    // stator_back_face' + str(24)
    print '        );\n    }\n);'
   
while j<6:
    X.append(ami_radius*math.cos(i))
    Y.append(ami_radius*math.sin(i))
    #Z.append(0.1)
    edge_x.append(ami_radius*math.cos(i + (theta/6)))
    edge_y.append(ami_radius*math.sin(i + (theta/6)))
    i = i + theta/3
    j = j + 1
    #print vertex(X[j-1], Y[j-1], Z[j-1]) + '  //v' + str(j)

X.append(0), X.append(boundingbox_negative_x), X.append(boundingbox_negative_x), X.append(0)
X.append(boundingbox_positive_x), X.append(boundingbox_positive_x)
Y.append(boundingbox_positive_y), Y.append(boundingbox_positive_y), Y.append(boundingbox_negative_y)
Y.append(boundingbox_negative_y), Y.append(boundingbox_negative_y), Y.append(boundingbox_positive_y)

while k<5: # Looping over rotor_stator_interface vertices to define blocks. 
    v5.append(13),        v6.append(13),       v7.append(0)
    v8.append(0),         v1.append(k + 14),   v2.append(k + 15)
    v3.append(k + 2),     v4.append(k + 1)
    k = k + 1
    
for j in range(32,37): # Looping over stator_rotor_interface vertices to define blocks.
    v1.append(j),         v2.append(j + 1),    v3.append(j - 5)
    v4.append(j - 6),    v5.append(j - 12),    v6.append(j - 11)
    v7.append(j - 24),     v8.append(j - 25)
    
while l<6: # Looping over rotor and stator ami interface to define sliding boundary.
    rotor_face1.append(l+15),    rotor_face2.append(l+14),    rotor_face3.append(l+1)
    rotor_face4.append(l+2)
    stator_face1.append(l+33),    stator_face2.append(l+32),    stator_face3.append(l+26)
    stator_face4.append(l+27)
    l = l + 1
    
while m<6: # Looping over front and back to define empty boundary condition.
    front1.append(0),     front2.append(m+1),    front3.append(m+2),    front4.append(0)
    front5.append(m+26),  front6.append(m+7),    front7.append(m+8),    front8.append(m+27)
    back1.append(13),     back2.append(m+14),    back3.append(m+15),    back4.append(13)
    back5.append(m+33),   back6.append(m+32),    back7.append(m+20),    back8.append(m+21)
    m = m + 1
    
vertices()
print ''
blocks()
print ''
edges()
print ''
boundaries()
print ''
frontandback()
