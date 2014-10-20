

cameras = { "Red Epic/2k":[11.059, 5.832], 
			"Red One/4k 16":[22.12, 12.44],
			"Red One/2k 16:9":[11.06, 6.22],
			"Red Epic/2k HD":[10.368, 5.832],

			"Black Magic Cinema Camera":[15.81, 8.88],
			"Film/35mm Full Frame":[36, 18.3],
			"Film/35mm/4 perf 2.40 Extract":[20.96, 10.4],

			"Arri/Alexa 16:9 1.7":[23.76, 13.37],
			"Arri/Alexa 4:3 1.78":[23.76, 13.37],

			"Phantom/HD Gold 1080p":[24, 13.5],
			"Phantom/65 1080p":[24.42, 13.7],
			"Phantom/Flex 1080p":[18.55, 10.43],

			"Sony/F35 2.39":[22.45, 9.4],

			"Canon DSLR/7D Video":[22.3, 12.54],
			"Canon DSLR/6D Video":[35.8, 20.14],
			"Canon DSLR/5D MKII+III Video":[35.8, 20.14],
			"Canon DSLR/1DX Video":[35.8, 20.14],
			"Canon DSLR/Rebel video":[22.3, 12.54],
			}
			


def matchCameras():

	srcCam = cmds.ls(sl=True)[0]
	trgtCam = cmds.ls(sl=True)[1]

	attributes = cmds.listAttr(srcCam, write=True, hasData=True )
	for attribute in attributes:
		try:
			cmds.setAttr(trgtCam+'.'+attribut, cmds.getAttr(srcCam+'.'+attribut,) write=True)
		except:
			print "failed to match",attribute

matchCameras()			

def setAperture(camera,x,y,fl=None):
	# millimeters to inches
	x = x/25.4
	y = y/25.4
	print x,y
	# set attributes
	cmds.setAttr(camera+".horizontalFilmAperture",x)
	cmds.setAttr(camera+".verticalFilmAperture",y)
	
	if fl is not None:
		cmds.setAttr(camera+".focalLength",fl)
	
# setAperture(cmds.ls(sl=True)[0],33,33)

