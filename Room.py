from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import GeomNode,NodePath
from panda3d.core import LVector3

from random import randrange

roomsize = [160,100,40] #room size x, y, z
wt = 0.05 #wall thickness

room = [
    [0,0,0],[0,0,1],[0,1,0],[0,1,1],
    [1,0,0],[1,0,1],[1,1,0],[1,1,1],
    [wt,wt,wt],[wt,wt,1],[wt,1-wt,wt],[wt,1-wt,1],
    [1-wt,wt,wt],[1-wt,wt,1],[1-wt,1-wt,wt],[1-wt,1-wt,1]
]

def generaterooms():
    rooms = randrange(1,2**16)
    roomlist = []
    for x in [2**y for y in range(16)]:
        roomlist.append(x & rooms)
    roomcount = 0
    rooms = render.attachNewNode('rooms')
    room = makeRoom()
    for i in range(len(roomlist)):
        if roomlist[i]:
            roomcount += 1
            x = i % 4
            y = i // 4
            roomlist[i] = rooms.attachNewNode(f'room{i}')
            roomlist[i].setPos(x*roomsize[0],y*roomsize[1],0)
            roomlist[i].attachNewNode(room)
            roomlist[i].setTwoSided(True)

    if roomcount < 4:
        return generaterooms()
    return roomlist

def issides(x1,x2,x3,x4):
    for i in range(len(x1)):
        if x1[i] == x2[i] and x1[i] == x3[i] and x1[i] ==  x4[i]:
            return True
    return False

# You can't normalize inline so this is a helper function
def normalized(*args):
    myVec = LVector3(*args)
    myVec.normalize()
    return myVec

def makeSquare(x1, y1, z1, x2, y2, z2):
    format = GeomVertexFormat.getV3n3cpt2()
    vdata = GeomVertexData('square', format, Geom.UHDynamic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')

    # make sure we draw the sqaure in the right plane
    if x1 != x2:
        vertex.addData3(x1, y1, z1)
        vertex.addData3(x2, y1, z1)
        vertex.addData3(x2, y2, z2)
        vertex.addData3(x1, y2, z2)

        normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
        normal.addData3(normalized(2 * x2 - 1, 2 * y1 - 1, 2 * z1 - 1))
        normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
        normal.addData3(normalized(2 * x1 - 1, 2 * y2 - 1, 2 * z2 - 1))

    else:
        vertex.addData3(x1, y1, z1)
        vertex.addData3(x2, y2, z1)
        vertex.addData3(x2, y2, z2)
        vertex.addData3(x1, y1, z2)

        normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
        normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z1 - 1))
        normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
        normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z2 - 1))

    # adding different colors to the vertex for visibility
    color.addData4f(1.0, 0.0, 0.0, 1.0)
    color.addData4f(0.0, 1.0, 0.0, 1.0)
    color.addData4f(0.0, 0.0, 1.0, 1.0)
    color.addData4f(1.0, 0.0, 1.0, 1.0)

    texcoord.addData2f(0.0, 1.0)
    texcoord.addData2f(0.0, 0.0)
    texcoord.addData2f(1.0, 0.0)
    texcoord.addData2f(1.0, 1.0)

    # Quads aren't directly supported by the Geom interface
    # you might be interested in the CardMaker class if you are
    # interested in rectangle though
    tris = GeomTriangles(Geom.UHDynamic)
    tris.addVertices(0, 1, 3)
    tris.addVertices(1, 2, 3)

    square = Geom(vdata)
    square.addPrimitive(tris)
    return square

def getsides():
    sides = []
    for h in range(2):
        for i in range(h*8,2**(3+h)-3):
            for j in range(i+1,2**(3+h)-2):
                for k in range(j+1,2**(3+h)-1):
                    if room[i][2] == 1 and room[j][2] == 1 and room[k][2] == 1:
                            continue
                    for l in range(k+1,2**(3+h)):
                        if issides(room[i],room[j],room[k],room[l]):
                            sides.append([room[i],room[j],room[k],room[l]])
    # for i in [[1,3,10,11],[1,5,10,14],[5,7,14,15],[3,7,11,15]]:
        # sides.append([room[i[0]],room[i[1]],room[i[2]],room[i[3]]])
    return sides

def makeRoom(): #include portals to other rooms
    snode = GeomNode('room')
    faces = getsides()

    for i in faces:
        square = makeSquare((i[0][0])*roomsize[0],i[0][1]*roomsize[1],i[0][2]*roomsize[2],(i[3][0])*roomsize[0],i[3][1]*roomsize[1],i[3][2]*roomsize[2])
        snode.addGeom(square)
        
    return snode