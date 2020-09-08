
#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

# sublime
import sublime, sublime_plugin
# my
from .my.classes import setInterval
# variables
selfClicks=0
keyCount=0
idle=1

# runs a nonstop tally on keypresses
# uses a global variable to store changes
class keyPresses(sublime_plugin.EventListener): 
	#EVENT LISTENER INSIDE FUNCTION(sublime_plugin.###)

	# default
	clicks=0
	# methods
	def on_modified(self,view):
		# increment
		self.clicks+=1
		# global
		global keyCount
		global idle
		global selfClicks
		# variables
		idle=0
		keyCount=self.clicks
		selfClicks=self.clicks
		#print(keyCount,self.clicks)
	def get_keyCount():
		return keyCount


#timed function that checks in 
#on the keypresses at preset intervals
def action():
	thisKeyCount=keyPresses.get_keyCount()
	print("thisKeyCount",thisKeyCount)

## HOW OFTEN?
thisInterval=setInterval.setInterval(5,action);
#print(thisInterval)


