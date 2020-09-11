# sublime
import sublime,sublime_plugin
#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

# takes a qualifier argument
# to check for the file named
# in the function
class MaidenVoyage:

	def __init__(self,anchor):
		self.anchor=anchor

	def anchorSearch(self):
		thisAnchor=self.anchor
		sublime.active_window().run_command("get_window",{"thisAnchor": thisAnchor})


class GetWindowCommand(sublime_plugin.WindowCommand):

	def __init__(self,window):
		self.window=window

	def run(self,thisAnchor):
		print(thisAnchor)
		return thisAnchor
		#self.projectFolders(thisAnchor)

	def projectFolders(self,thisAnchor):
		window=self.window
		
        
anchor='/fileAnchor.json'
result=MaidenVoyage(anchor).anchorSearch()
#print(result)

"""
CRIB NOTES 

class name(object):
	def __init__(self, name):
		self.name = name
	def PrintName(self):
		print self.name

a = name('bob')
a.PrintName()
bob

"""
