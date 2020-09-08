
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

# EVENT LISTENER AS SHOWN IN FUNCTION ();
# Important to Note the (sublime_plugin.EventListener)
class keyPresses(sublime_plugin.EventListener):
	# default variable
	clicks=0
	# methods
	def on_modified(self,view):
		# global
		global keyCount
		global idle
		global selfClicks
		#increment
		self.clicks+=1
		idle=0
		keyCount=self.clicks
		selfClicks=self.clicks
		print(keyCount,self.clicks)


## WHAT TO DO
def action() :
	
    if keyCount < 1:
        idle+=1
    print("-----")
    print("keyCount")
    print(keyCount)
    print("------")
    #reset
    keyCount=0
    #print('action ! -> time : {:.1f}s'.format(time.time()-StartTime))
    print("******")
    print("IDLE")
    print(idle)
    print("******")

## HOW OFTEN?
thisInterval=setInterval.setInterval(1,action);
print(thisInterval)


