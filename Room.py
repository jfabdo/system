from panda3d.core import GeomNode,NodePath
from panda3d.core import CollisionNode, CollisionPlane, Point3, Plane

from random import randrange
from open_source.makesquare import makeSquare

roomsize = [30,30,30] #room size x, y, z
wt = 0.05 #wall thickness



room = [
    [0,0,0],[0,0,1],[0,1,0],[0,1,1],
    [1,0,0],[1,0,1],[1,1,0],[1,1,1],
    [wt,wt,wt],[wt,wt,1],[wt,1-wt,wt],[wt,1-wt,1],
    [1-wt,wt,wt],[1-wt,wt,1],[1-wt,1-wt,wt],[1-wt,1-wt,1]
]

def generaterooms():
    totalrooms = randrange(2**5-1,2**16)
    roomlist = []
    for x in [2**y for y in range(16)]:
        roomlist.append(x & totalrooms)
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
        rooms.detach()
        return generaterooms()
    return roomlist

# def issides(x1,x2,x3,x4):
#     for i in range(len(x1)):
#         if x1[i] == x2[i] and x1[i] == x3[i] and x1[i] ==  x4[i]:
#             return True
#     return False

# def getsides():
#     sides = []
#     for h in range(1):
#         for i in range(h*8,2**(3+h)-3):
#             for j in range(i+1,2**(3+h)-2):
#                 for k in range(j+1,2**(3+h)-1):
#                     if room[i][2] == 1 and room[j][2] == 1 and room[k][2] == 1:
#                             continue
#                     for l in range(k+1,2**(3+h)):
#                         if issides(room[i],room[j],room[k],room[l]):
#                             sides.append([room[i],room[j],room[k],room[l]])
#     # for i in [[1,3,10,11],[1,5,10,14],[5,7,14,15],[3,7,11,15]]:
#         # sides.append([room[i[0]],room[i[1]],room[i[2]],room[i[3]]])
#     return sides

def getsides():
    sides = [
        [0,1,2,3],
        [0,2,4,5],
        [2,3,5,7],
        [0,1,4,6],
        [4,5,6,7]
    ]

    for i in sides:
        for j in range(len(i)):
            i[j] = room[i[j]]
    
    return sides

def makeRoom(): #include portals to other rooms
    snode = GeomNode('room')
    faces = getsides()

    for i in faces:
        square = makeSquare((i[0][0])*roomsize[0],i[0][1]*roomsize[1],i[0][2]*roomsize[2],(i[3][0])*roomsize[0],i[3][1]*roomsize[1],i[3][2]*roomsize[2])
        snode.addGeom(square)

    return snode