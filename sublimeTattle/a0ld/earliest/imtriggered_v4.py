import sublime
import sublime_plugin
import requests
import json
import time, threading
StartTime=time.time()

# EVENT LISTENER AS SHOWN IN FUNCTION ();
# other plugin used sublime_plugin.textCommand
class ImTriggeredCommand(sublime_plugin.EventListener):

	clicks=0
	idle=0

	def action() :
	    global thisCount
	    global idle

	    if thisCount < 1:
		    idle+=1
	    else:
		    idle=0

	print("count")
	print(thisCount)
	print("idle")
	print(idle)
	thisCount=0
	#print('action ! -> time : {:.1f}s'.format(time.time()-StartTime))

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

	    def reval(self):
	        if idle > 10:
	            print("OK")
	            self.stopEvent.set()
	        else:
	            print("zzzz")

	    def cancel(self) :
	        self.stopEvent.set()

	# start action every 0.6s
	inter=setInterval(1,action)
	print('just after setInterval -> time : {:.1f}s'.format(time.time()-StartTime))

	# will stop interval in 5s
	t=threading.Timer(10,inter.cancel)
	t.start()

	def on_modified(self,view):
	    #debug
	    #print(self.clicks)
	    #increment
	    self.clicks+=1
	    global thisCount
	    global idle
	    thisCount=self.clicks
	    if thisCount < 1:
	        idle+=1


