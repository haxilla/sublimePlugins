#<! 12345 #!>

# sublime
import sublime,sublime_plugin,os
from .my.classes import allFolders

#print (dir(sublime.Window))
#print (sublime.Window)

def plugin_loaded():
	print(sublime.active_window().project_data())
	thisAnchor="fileAnchor.json"
	#print (sublime.Window.project_data.__dict__.values())
	#print (dir(sublime.Window))
	#newTest=dir(sublime.Window(1))
	#print(dir(sublime.Window(1).window_id))
	#print(dir(sublime.active_window().project_data()))
	
"""
xxx
crib notes

#from .my.classes import anchorValidate
#from .my.classes import pluginStart
#waits for loaded response
def plugin_loaded():
	pass

xxx
"""