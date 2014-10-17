import maya.cmds as cmds

coloroutput = cmds.ls(sl=True)[0]+'.outColor'
upstreaminput = cmds.listConnections(cmds.ls(sl=True),d=True, s=False,p=True)[-1]

def createNetwork(coloroutput,upstreaminput):
	# Create 
	remapHSV = cmds.shadingNode('remapHsv', asUtility=True)
	#nodeRamp = cmds.shadingNode('ramp', asTexture=True)
	#

	node = remapHSV
	# createNetwork(node)
	# Make connections	

	for i in ['.value','.color','input']:
		try:
			cmds.connectAttr( coloroutput, node+i, f=True)
		except:
			pass	
	
	for i in ['.outColor','outValue','output']:
		try:
			cmds.connectAttr( node+i,upstreaminput, f=True)
		except:
			pass			

createNetwork(coloroutput,upstreaminput)




