import maya.cmds as cmds

sel = cmds.ls(sl=True)[0]
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
		for y in ['.outColor','outValue','output']: # ugly! there must be some way of returning the selected nodes outputted attributes?
			try:
				cmds.connectAttr( coloroutput+y, node+i, f=True)
			except:
				pass	
	
	for i in ['.outColor','outValue','output']:
		try:
			cmds.connectAttr( node+i,upstreaminput, f=True)
		except:
			pass			

createNetwork(sel,upstreaminput)




