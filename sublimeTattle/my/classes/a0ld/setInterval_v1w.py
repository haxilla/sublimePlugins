######################################
# File is a good example of how to edit
# functions to accept more parameters

# import
import time, threading

## HOW OFTEN
class setInterval :

	def __init__(self,interval,action,keyCount,idle) :
	    self.interval=interval
	    self.action=action;
	    self.stopEvent=threading.Event()
	    self.keyCount=keyCount
	    self.idle=idle
	    thread=threading.Thread(target=self.__setInterval)
	    thread.start()

	def __setInterval(self) :
	    keyCount=self.keyCount
	    idle=self.idle
	    nextTime=time.time()+self.interval
	    while not self.stopEvent.wait(nextTime-time.time()) :
	        nextTime+=self.interval
	        self.action(keyCount,idle)

	def cancel(self) :
	    #if idle > 2:
	    print("im done...")
	    self.stopEvent.set()
