
# 
# Tool Template
# 
import sys
import pySideLoader
from PySide import QtCore, QtGui, QtUiTools
import pysideuic


reload (pySideLoader)
sys.dont_write_bytecode = True


#
# INTERFACE
# =========================================================

# settings
launchAsDockedWindow = False					# False = opens as free floating window, True = docks window to Maya UI, Panel in Nuke
styleSheet = ''									# External StyleSheet to use, not working right now

app = pySideLoader.Setup(__file__)
form, base = app.loadUiType()

class HelloWorld(form,base):
	def __init__(self, parent=None):
		super(HelloWorld, self).__init__(parent)
		self.setupUi(self)
		pySideLoader.setwindowTitle(self,__file__)
	
		# INIT UI ACCESSS	
		# ========================================================='

		# Access the UI
		# Example:
		# self.listWidget.addItem('Hello world')



	# Methods
	# =========================================================
			
	def foo(self):
		pass



global gui

if pySideLoader.mode() == "maya":	
	gui = HelloWorld( app.maya_main_window() )
elif pySideLoader.mode() == "nuke":
	gui = HelloWorld( parent=QtGui.QApplication.activeWindow() )		
gui.show() 

# =========================================================

