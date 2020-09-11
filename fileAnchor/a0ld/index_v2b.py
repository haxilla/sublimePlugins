# sublime
import sublime,sublime_plugin
#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

# takes a qualifier argument
# to check for the file named
# in the function
class FileAnchorQualify:

	def __init__(self,anchor):
		self.anchor=anchor

	def anchorSearch(self):
		thisAnchor=self.anchor
		return thisAnchor

	def beachComb(self,window):
		theBeach=GetWindowCommand.projectFolders()


class GetWindowCommand(sublime_plugin.WindowCommand):

	#how to call without using run command
	sublime.active_window().run_command("get_window",{"qualifier": "qv"})
	
	def __init__(self,window):
		self.window=window

	def run(self,qualifier):
		self.projectFolders(qualifier)

	def projectFolders(self,qualifier):
		print(qualifier)
        
anchor='/fileAnchor.json'
result=FileAnchorQualify(anchor).anchorSearch()
print(result)

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
