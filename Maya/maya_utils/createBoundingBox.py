import maya.cmds as cmds

def createBoundingBox():
    
    for i in cmds.ls(sl=True):
        print i
        cube = cmds.polyCube()[0]
        x1, y1, z1, x2, y2, z2 = cmds.exactWorldBoundingBox(i, calculateExactly=True)
        cmds.move(x1, '%s.f[5]' % cube, x=True)
        cmds.move(y1, '%s.f[3]' % cube, y=True)
        cmds.move(z1, '%s.f[2]' % cube, z=True)
        cmds.move(x2, '%s.f[4]' % cube, x=True)
        cmds.move(y2, '%s.f[1]' % cube, y=True)
        cmds.move(z2, '%s.f[0]' % cube, z=True) 
        cmds.rename(i+"_BBox")   

createBoundingBox()
