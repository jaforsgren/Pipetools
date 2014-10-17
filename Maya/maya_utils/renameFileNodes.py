def renameFileNodes():
	for i in cmds.ls(sl=True):
		if cmds.nodeType(i) =="file":
			name = cmds.getAttr( i+'.fileTextureName')
			name = os.path.basename(name).split('/')[-1].split('.')[0]
			try:
			    cmds.rename(i,name)
			except:
			    cmds.rename(i,"_"+name)

renamefilenodes()