import sublime
import sublime_plugin
import requests
import json
from threading import Timer
from time import sleep

# EVENT LISTENER AS SHOWN IN FUNCTION ();
# other plugin used sublime_plugin.textCommand
class ImTriggeredCommand(sublime_plugin.EventListener):
	##
	clicks=0
	clicksTrigger=10

	#
	# works
	#starttime = time.time()
	#while True:
	#    print ("tick")
	#    time.sleep(15.0 - ((time.time() - starttime) % 15.0))

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

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def hello(name):
    print ("Hello %s!" % name)

print ("starting...")
# How often to repeat & what?
# this calls def()
rt = RepeatedTimer(15, hello, "World") # it auto-starts, no need of rt.start()
try:
    sleep(500) # your long-running job goes here...
finally:
	print("ugh, im exhausted, I quit...")
    rt.stop() # better in a try/finally block to make sure the program ends!


