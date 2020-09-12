
import sublime

global siteList_g
global currentFile_g
siteList_g=None
currentFile_g=None
thisAnchor='/fileAnchor.json'

class PluginStart:
	
	def __init__(self):
		self.currentFile_g	= currentFile_g
		self.siteList_g		= siteList_g

	# SETS 2 GLOBAL VARIABLES
	def setGlobals(self):
		pass

	def getSiteList(self):
		sublime.active_window().run_command\
		("match_anchors",{"thisAnchor": thisAnchor})

	def getCurrentFile(self):
		# creates **GLOBAL** currentFile_g
		sublime.active_window().run_command("this_file")

	def showPanel(self):
		# opens panel
		sublime.active_window().run_command\
		("show_panel", {"panel": "console"})

