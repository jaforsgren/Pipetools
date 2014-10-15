import maya.cmds as cmds
import os.path
import shutil


"""
=======================================================
TODO
+interface, of course
+ability to collect to alternativ folder
+redundancies, comparing filesizes and creationdates in case of clash, asking user which to use.
=======================================================
"""





def fixpath(string):
	string = string.replace("\\","/")
	return string

def imgpath(img):
	imgfile = img.split("/")[-1]	
	workspacepath = cmds.workspace(q=True,dir=True)
	imgfolder = cmds.workspace("images",q=True,fre=True)
	imgfullpath = os.path.join(workspacepath,imgfolder,imgfile)
	imgfullpath = fixpath(imgfullpath)
	return imgfullpath

def recursiveShaderSearch(shader): 
     layeredShaderName = ""          
     shaders = cmds.listConnections(shader,d=False, s=True)    
     if shaders != None:
         for i in shaders:            
            if cmds.nodeType(i) == "file":
                oldfilepath= cmds.getAttr( i+'.fileTextureName')
                newfilepath= imgpath(oldfilepath)
                relativepath = cmds.workspace("images",q=True,fre=True) +"/"+newfilepath.split("/")[-1]
                
                #check if new folder exists, if not, create it.           
                if not os.path.exists( os.path.dirname(newfilepath) ):
                	os.mkdir(os.path.dirname(newfilepath) )
                	print "CREATING FOLDER ",os.path.dirname(newfilepath)
                #check if file doesnt exist in new folder
                if not os.path.exists( newfilepath ):
                	print "copying" ,oldfilepath, "to", newfilepath 
                	shutil.copyfile( oldfilepath, newfilepath)
                else:
					print"file already exists, switch to that one..."

                cmds.setAttr( i+'.fileTextureName', newfilepath, type = "string")          
                

            elif cmds.nodeType(i) == "layeredShader":
                #controling that this isnt some kind of wierd looping connection                
                if ( i == layeredShaderName) and ( layeredShaderName != "" ):
                    print "MATCHED DUCPLICATE INPUT", layeredShaderName                                             
                else:
                    layeredShaderName = i                    
                    recursiveShaderSearch(i,layeredShaderName)
                    layeredShaderName = i                               
            else:
            	try:
            		recursiveShaderSearch(i,layeredShaderName)
            	except:	                             
                	#print "end of line for nodes" 
                	pass

"""
shader= cmds.ls(sl=True, l =True)
recursiveShaderSearch(shader,layeredShaderName)
"""