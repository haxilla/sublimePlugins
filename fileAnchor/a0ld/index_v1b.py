# sublime
import sublime, sublime_plugin
import os.path
import json

#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

#How to get current fileName
import sublime, sublime_plugin

#filetastic
#fileFanatic
#fileDroid
#filezone
#cocafiles
class fileAnchorCommand(sublime_plugin.WindowCommand):

	# file must be present at siteRoot
	# to qualify
	#default='/subfiles.json'
	#qualify
	def __init__(self,window):
		self.window=window
		
	def run(self):
		print (self.window)
	

		"""
		def run(self):
			print("herro?")
			print(self.window)
		"""


		#print(self.qualifier)
		#thisWindow=self.window.project_data()
		#independent of whether anything is open or now
		#give absolute path info about folders added to project
		#print(self.window)
		#project_data=self.window.project_data()
		#defaults
		#enabledSites={}
		#disabledSites={}
		#iterate through the project_data

		"""
		for x in project_data['folders']:
			# path
			thisPath=x['path']
			# combined path
			checkPath=thisPath+subFile
			# is file present
			enabled=os.path.isfile(checkPath)
			# if TRUE read for values
			# multiple calls are being 
			# made, once per value
			if enabled:
			# add to enabled
				enabledSites['thisPath']=thisPath
				enabledSites['subFile']=subFile
				enabledSites['checkPath']=subFile
				enabledSites['enabled']=True

			else:
			# add to not disabled
				disabledSites['thisPath']=thisPath
				disabledSites['subFile']=subFile
				disabledSites['checkPath']=subFile
				disabledSites['enabled']=False

			# set reply
			reply={
				"enabledSites":enabledSites,
				"disabledSites":disabledSites}

		#reply
		#print(reply)
		return reply
	"""
	"""
	def readFile(self,validPath):
		#get the view
		with open(validPath,'r') as thisFile:
			content=thisFile.read()
			#print(content)
			self.processFile(validPath,content)
	"""

#	def processFile(self,validPath,content):

#		print(validPath,content)

#default="/subfiles.json";

#fileFanatic=fileFanatic(default).qualify()
#print(fileFanatic)
#






"""

	for e in l:              # this is my condition list
    if e + '.' in href:  # this is the mechanism to choose the right function
        return globals()['do_something_' + e]()
"""
"""
CRIB NOTES
"""
#print(project_data)
#works
#print(project_data)
# works when only 2
# does NOT scale for additions
# for x,y in project_data:
#	print (x['path'])
#	print (y['path'])

#path for project configuration file 
#project_file_name=thisWindow1.project_file_name()

#command: find_in_folder {"dirs": ["the folder path here"]}

"""

print(
	dir(thisWindow1),
	dir(thisWindow2),
	project_data,
)

"""

# to run this function enter commmand below
# into sublime console
#window.run_command("window_check")



#works but not useable for this
#storing as idea
#project_data2=thisWindow1.project_data().values()

"""
with open(checkPath) as json_file:
json_data=json.load(json_file)
for x in json_data:
print(x)
"""

"""
#independent of whether anything is open or now
thisWindow1=self.window
#attaches to last view
thisWindow2=self.window.active_view()
"""
