# sublime
import sublime,sublime_plugin
import os.path
import json
from .my.classes import getWindow

#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

class getWindowCommand(sublime_plugin.WindowCommand):
		
	def __init__(self,window):
		self.window=window
		projectData=window.project_data()
		self.projectData=projectData
		#print(projectData)

	def run(self,qualifier):
		self.projectFolders(qualifier)

	def projectFolders(self,qualifier):
		print(qualifier)



