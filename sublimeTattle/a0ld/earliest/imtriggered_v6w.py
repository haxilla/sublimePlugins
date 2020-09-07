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

# EVENT LISTENER AS SHOWN IN FUNCTION ();
# other plugin used sublime_plugin.textCommand
class ImTriggeredCommand(sublime_plugin.EventListener):

	clicks=0

	## ACTION - WHAT TAKES PLACE
	## EVERY INTERVAL
	def action() :
	    global keyCount
	    global idle
	    global t
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

	# start action every x sectond
	inter=setInterval(1,action)
	# start threading time
	t=threading.Timer(10,inter.cancel)
	
	def on_modified(self,view):
		#debug
		#print(self.clicks)
		#increment
		self.clicks+=1

		global keyCount
		global idle
		idle=0
		keyCount=self.clicks