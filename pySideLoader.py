# 
# Heavily based on https://github.com/fredrikaverpil/pyVFX-boilerplate/blob/master/boilerplate.py by Fredrik Averpil
# 


import os
import sys
import xml.etree.ElementTree as xml
from cStringIO import StringIO	

# Settings
# =========================================================

sys.dont_write_bytecode = True									# Do not generate .pyc files			
# Maya settings
launchAsDockedWindow = False									# False = opens as free floating window, True = docks window to Maya UI
# Nuke settings
launchAsPanel = False										# False = opens as regular window, True = opens as panel
parentToNukeMainWindow = True									# True = makes window stay on top of Nuke
# Site-packages location:
site_packages_Win = r'C:\Users\jforsgren.OFFICE\Dropbox\Workgroups\DEV\Nuke\site-packages'		# Location of site-packages containing PySide and pysideuic and/or PyQt and SIP, example: C:/Python26/Lib/site-packages'	

sys.dont_write_bytecode = True



#
# Run mode 
# =========================================================

runMode = 'standalone'
try:
	import maya.cmds as cmds
	import maya.OpenMayaUI as omui
	import shiboken
	runMode = 'maya'
except:
	pass
try:
	import nuke
	from nukescripts import panels
	runMode = 'nuke'	
except:
	pass
if (site_packages_Win != '') and ('win' in sys.platform) and not site_packages_Win in sys.path : sys.path.append( site_packages_Win )


from PySide import QtCore, QtGui, QtUiTools
import pysideuic


#
# Classes and Functions 
# =========================================================

class Setup:
	def __init__(self,infile):
		
		self.file = infile
		filename = self.file.split("\\")[-1]
		filename = filename.split(".")[0]				
		self.uiFile = os.path.join(os.path.dirname(self.file),'UI',filename+'.ui')
		print "\n\n======== PySide Loader Setup UI using %s \n======== Setup running in %s \n\n" %(self.uiFile,runMode)
	

	def loadUiType(self):
		parsed = xml.parse(self.uiFile)
		widget_class = parsed.find('widget').get('class')
		form_class = parsed.find('class').text

		with open(self.uiFile, 'r') as f:
			o = StringIO()
			frame = {}

			
			pysideuic.compileUi(f, o, indent=0)
			pyc = compile(o.getvalue(), '<string>', 'exec')
			exec pyc in frame

			#Fetch the base_class and form class based on their type in the xml from designer
			self.form_class = frame['Ui_%s'%form_class]
			self.base_class = eval('QtGui.%s'%widget_class)

		return self.form_class, self.base_class

	def wrapinstance(self,ptr, base=None):
		
		if ptr is None:
			return None
		ptr = long(ptr) #Ensure type
		if globals().has_key('shiboken'):
			if base is None:
				qObj = shiboken.wrapInstance(long(ptr), QtCore.QObject)
				metaObj = qObj.metaObject()
				cls = metaObj.className()
				superCls = metaObj.superClass().className()
				if hasattr(QtGui, cls):
					base = getattr(QtGui, cls)
				elif hasattr(QtGui, superCls):
					base = getattr(QtGui, superCls)
				else:
					base = QtGui.QWidget
			return shiboken.wrapInstance(long(ptr), base)
		elif globals().has_key('sip'):
			base = QtCore.QObject
			return sip.wrapinstance(long(ptr), base)
		else:
			return None

	def maya_main_window(self):
		main_window_ptr = omui.MQtUtil.mainWindow()
		return self.wrapinstance( long( main_window_ptr ), QtGui.QWidget )	# Works with both PyQt and PySide


	
def mode():
	return runMode

def setwindowTitle(self,infile):
	windowTitle =  infile.split("\\")[-1].split(".")[0].split(".py")[0]	
	windowObject = windowTitle
	self.setObjectName(windowObject)
	self.setWindowTitle(windowTitle)
	# print "======== setting windowTitle to %s" %windowTitle


def getComponents(form,*args):
	components =''
	if args:
		for i in args:		
			components = form.findChildren("QtGui."+i)
	else: 			
		components = form.findChildren()
	return components	






