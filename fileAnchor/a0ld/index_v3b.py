# sublime
import sublime,sublime_plugin
import os
#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

# takes a qualifier argument
# to pass off 
class MatchAnchors:

	def __init__(self,anchor):
		self.anchor=anchor

	def anchorSearch(self):
		thisAnchor=self.anchor
		sublime.active_window().run_command("sort_anchors",{"thisAnchor": thisAnchor})

class SortAnchors(sublime_plugin.WindowCommand):

	def __init__(self,window):
		self.window=window

	def run(self,thisAnchor):
		#print(thisAnchor)
		self.projectFolders(thisAnchor)

	def projectFolders(self,thisAnchor):
		#folders inside project
		project_data=self.window.project_data()
		#print(project_data)
		#defaults
		enabledSites={}
		disabledSites={}
		#iterate through the project_data
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
				enabledSites['checkPath']=thisPath
				enabledSites['enabled']=True

			else:
			# add to not disabled
				disabledSites['thisPath']=thisPath
				disabledSites['fileAnchor']=thisAnchor
				disabledSites['checkPath']=checkPath
				disabledSites['enabled']=False

			# set reply
			reply={
				"enabledSites":enabledSites,
				"disabledSites":disabledSites}

		#reply
		#print(reply)
		return reply

anchor='/fileAnchor.json'
result=MatchAnchors(anchor).anchorSearch()
print(result)

"""
Crib Notes
"""
