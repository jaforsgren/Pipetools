import maya.cmds as cmds

'''
=============================================
TODO
ramp function


prewiew-ramp function


==============================================
'''

def createNetwork(utilnode):

	for sel in cmds.ls(sl=True):

		upstreaminput = cmds.listConnections(sel,d=True, s=False,p=True)[-1]

		# Create 
		node = cmds.shadingNode(utilnode, asUtility=True)
		
		# Make connections	
		for i in ['.value','.color','input']:
			for y in ['.outColor','outValue','output']: # ugly! there must be some way of returning the selected nodes outputted attributes?
				try:
					cmds.connectAttr( sel+y, node+i, f=True)
				except:
					pass	
		
		for i in ['.outColor','outValue','output']:
			try:
				cmds.connectAttr( node+i,upstreaminput, f=True)
			except:
				pass			

createNetwork('remapColor') #remapValue (doesnt work yet),remapHSV,remapColor

