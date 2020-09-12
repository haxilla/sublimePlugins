
import sublime,sublime_plugin,os

class PluginStart(sublime_plugin.Window):

	def __init__(self,window,thisAnchor):
		self.thisAnchor=thisAnchor
		self.thisWindow=window
		return thisWindow

		'''
		#defaults
		enabledSites={}
		disabledSites={}
		#project folders
		project_data=self.window.project_data()
		#loop
		for x in project_data['folders']:
			# path
			thisPath=x['path']
			# combined path
			checkPath=thisPath+thisAnchor
			# is file present
			enabled=os.path.isfile(checkPath)
			# if TRUE read for values
			# multiple calls are being 
			# made, once per value
			if enabled:
			# add to enabled
				enabledSites['thisPath']=thisPath
				enabledSites['fileAnchor']=thisAnchor
				enabledSites['checkPath']=checkPath
				enabledSites['enabled']=True

			else:
			# add to not disabled
				disabledSites['thisPath']=thisPath
				disabledSites['fileAnchor']=thisAnchor
				disabledSites['checkPath']=checkPath
				disabledSites['enabled']=False

		
		# set reply
		siteList={
			"enabledSites":enabledSites,
			"disabledSites":disabledSites}

		#reply
		#print(reply)
		#print(siteList)
		return siteList
	'''
	def projectFolders(self):
		pass

	def currentFile(self):	
		pass

'''
CRIB NOTES

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



	class MatchAnchors(sublime_plugin.WindowCommand):

		def __init__(self,window):
			self.window=window

		def run(self,thisAnchor):
			#print(thisAnchor)
			self.projectFolders(thisAnchor)

		def projectFolders(self,thisAnchor):
			#print(thisAnchor)

			#defaults
			enabledSites={}
			disabledSites={}
			#project folders
			project_data=self.window.project_data()
			#loop
			for x in project_data['folders']:
				# path
				thisPath=x['path']
				# combined path
				checkPath=thisPath+thisAnchor
				# is file present
				enabled=os.path.isfile(checkPath)
				# if TRUE read for values
				# multiple calls are being 
				# made, once per value
				if enabled:
				# add to enabled
					enabledSites['thisPath']=thisPath
					enabledSites['fileAnchor']=thisAnchor
					enabledSites['checkPath']=checkPath
					enabledSites['enabled']=True

				else:
				# add to not disabled
					disabledSites['thisPath']=thisPath
					disabledSites['fileAnchor']=thisAnchor
					disabledSites['checkPath']=checkPath
					disabledSites['enabled']=False

			global siteList_g
			# set reply
			siteList_g={
				"enabledSites":enabledSites,
				"disabledSites":disabledSites}

			#reply
			#print(reply)
			#print(siteList)
			return siteList_g
	


'''
