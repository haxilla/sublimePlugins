import sublime,sublime_plugin,os

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

class ThisFile(sublime_plugin.WindowCommand):

	def run(self):
		#set
		#print(dir(self.window.active_view()))
		global currentFile_g
		currentFile_g=self.window.active_view().file_name()