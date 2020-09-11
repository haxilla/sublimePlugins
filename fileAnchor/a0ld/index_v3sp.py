# sublime
import sublime,sublime_plugin
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
		return thisAnchor


class SortAnchors(sublime_plugin.WindowCommand):

	def __init__(self,window):
		self.window=window

	def run(self,thisAnchor):
		#print(thisAnchor)
		self.projectFolders(thisAnchor)

	def projectFolders(self,thisAnchor):
		#print(thisAnchor)
		return thisAnchor

anchor='/fileAnchor.json'
result=MatchAnchors(anchor).anchorSearch()
print(result)
