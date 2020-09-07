import sublime
import sublime_plugin
import requests
import json
import time, threading
StartTime=time.time()

# EVENT LISTENER AS SHOWN IN FUNCTION ();
# other plugin used sublime_plugin.textCommand
class ImTriggeredCommand(sublime_plugin.EventListener):
	##
	clicks=0
	clicksTrigger=10

	def action() :
	    print('action ! -> time : {:.1f}s'.format(time.time()-StartTime))


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
	        self.stopEvent.set()

	# start action every 0.6s
	inter=setInterval(15,action)
	print('just after setInterval -> time : {:.1f}s'.format(time.time()-StartTime))

	# will stop interval in 5s
	t=threading.Timer(100,inter.cancel)
	t.start()


	def on_modified(self,view):
		#debug
		#print(self.clicks)
		#increment
		self.clicks+=1
		#when count goes up
		if(self.clicks >= self.clicksTrigger):
			#default
			self.clicks=0
			#debug
			#print("imTriggered!")
			#setURL
			theURL='https://www.remstage.test/admin/sublimeTattle'
			#send http request
			page=requests.get(theURL,verify=False)
			#full result set in json
			j_results=json.loads(page.text)
			#get variables
			var1=j_results['one']
			var2=j_results['two']
			print(page)

			#print(var1,var2)
			#print(r)
			#ewr=r.json()
			#from pprint import pprint
			#pprint(r.json())
			#resp_dict = json.loads(newr)
			#check=resp_dict['two']
			#print("check")


