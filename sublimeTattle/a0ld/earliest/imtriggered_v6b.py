import sublime
import sublime_plugin
import requests
import json
import time, threading
StartTime=time.time()
global keyCount
keyCount=0
global idle
idle=0
global t
t=12

def plugin_loaded():
	sublime.active_window().run_command("show_panel", {"panel": "console"})

# EVENT LISTENER AS SHOWN IN FUNCTION ();
# other plugin used sublime_plugin.textCommand
class ImTriggeredCommand(sublime_plugin.EventListener):

	clicks=0
	def on_modified(self,view):
		global keyCount
		global idle
		#increment
		self.clicks+=1
		idle=0
		keyCount=self.clicks

class setInterval :
	def __init__(self,interval,action) :
	    self.interval=interval
	    self.action=action
	    self.stopEvent=threading.Event()
	    thread=threading.Thread(target=self.__setInterval)
	    thread.start()

	def __setInterval(self) :
	    nextTime=time.time()+self.interval
	    while not self.stopEvent.wait(nextTime-time.time()) :
	        nextTime+=self.interval
	        self.action()

	def cancel(self) :
	    #if idle > 2:
	    print("im done...")
	    self.stopEvent.set()

## ACTION - WHAT TAKES PLACE
## EVERY INTERVAL
def action() :

	#set globals
	global keyCount
	global idle
	global inter
	global t

	#check keyCount
	if keyCount < 1:
		idle+=1

	#print
	print("-----")
	print("keyCount")
	print(keyCount)
	print("------")
	#print
	print("******")
	print("IDLE")
	print(idle)
	print("******")

	# check idle
	# cant run every bit of code 
	# every time idle is high
	# need to find a way to 
	# initiate ONCE 

	if idle>5:

		# start threading time
		# will run inter.cancel() in x seconds
		# inter (set as global)
		print("STOP ME - YOUR IDLE")
		if t is not 12:
			print("NOT 12 - YOURE IDLE")
			t.start()

		else:
			print(t)
			print("starting Timer Now...")
			#new instance
			t=threading.Timer(10,inter.cancel)

	else:
		#
		print("IM WORKING!!")
		#cancel existing
		if t is not 12:
			print("cancelling...")
			t.cancel()
			t=12
		else:
			print("t line99")


# start action every x sectond
global inter
inter=setInterval(1,action)

# check if idle
if idle>5:
	if t is not 12:
		t.cancel()

	t=threading.Timer(10,inter.cancel)
	t.start()

else:
	print("canceling timer")
	if t is not 12:
		t.cancel()
	
	t=threading.Timer(10,inter.cancel)