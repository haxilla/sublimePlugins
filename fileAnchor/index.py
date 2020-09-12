# sublime
import sublime,os
from .my.classes import anchorValidate
from pathlib import Path

# wait until load then enter
def plugin_loaded():
	thisAnchor='/fileAnchor.json'
	status=FileAnchor(thisAnchor).projectData()
	print(status)

# startup
class FileAnchor():

	#initialize
	def __init__(self,thisAnchor):
		self.thisAnchor=thisAnchor

	# lists all folders in project
	def projectData(self):
		#calling sublime
		projectData=sublime.active_window().project_data()
		#error
		if projectData==None:
			return "error-line26-index.py"
		
		#print(projectData)
		result=self.matchAnchors(projectData)
		return result

	def currentFile(self):
		#currentFile=dir(sublime.active_window().active_view().file_name())
		currentFile=sublime.active_window().active_view().file_name()
		return currentFile

	# search for fileAnchor.json in root 
	# to enable or disable
	def matchAnchors(self,projectData):
		# set anchor
		thisAnchor=self.thisAnchor
		# defaults
		enabledSites={}
		disabledSites={}
		# loop
		if projectData==None:
			return "error-line44-index.py"
	
		for x in projectData['folders']:
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

		# get currentFile 
		currentFile=self.currentFile()
		if currentFile==None:
			return "error line 81 index.py"

		# send enabled sites to check
		# for fileAnchor stamp on current file
		disCount=0
		enCount=0
		for x in siteList:
			#count & dispatch if enabled
			if x=='disabledSites':
				disCount+=1
			if x=='enabledSites':
				enCount+=1
				#send for validation
				#print(currentFile)
				anchorValidate.AnchorValidate(currentFile).stampCheck()

		#debug
		#print(disCount,enCount,siteList,currentFile)