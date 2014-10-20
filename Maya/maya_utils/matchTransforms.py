import maya.cmds as cmds

sel = cmds.ls(sl=True, type="transform")

if (len(sel)) > 1:
    
    target= sel[0]
    objs = sel[1:]
    p = cmds.getAttr(target+".translate")
    r = cmds.getAttr(target+".rotate")
    s = cmds.getAttr(target+".scale")   
    
    #print p[0]      
 
    for obj in objs:
        cmds.setAttr("%s.translate"%obj, p[0][0], p[0][1], p[0][2])
        cmds.setAttr("%s.rotate"%obj, r[0][0], r[0][1], r[0][2])
        cmds.setAttr("%s.scale"%obj, s[0][0], s[0][1], s[0][2])
        
  