
#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})

# sublime
import sublime, sublime_plugin
# mysql
import mysql.connector

# my
from .my.classes import setInterval
# variables
selfClicks=0
keyCount=0
idle=1

mydb = mysql.connector.connection.MySQLConnection(
	host="localhost",
	user="root",
	password="l34gu31290",
	database="remuserdb"
)

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM allorders LIMIT 1")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
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
	def get_idle():
		return idle

#timed function that checks in 
#on the keypresses at preset intervals
def action():
	global idle
	global keyCount
	keyCountNow=keyPresses.get_keyCount()
	idleNow=keyPresses.get_idle()
	if keyCountNow > 0:
		idle=0
		idleNow=0
	else:
		idle+=1
		idleNow=idle

	#save data to database


	#reset value to 0

	# cancel the action if
	# idleCount exceeds threshhold
	
	
######################################
## HOW OFTEN?						##
## 1m  60 	##	2m 120	## 	4m 240 	##
## 10m 600  ## 15m 900	## 30m 1800	##

thisInterval=setInterval.setInterval(15,action);