
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
totalCount=0
keyCount=0
idle=1

#MYSQL LOGIN
gitDevDB = mysql.connector.connection.MySQLConnection(
	host="localhost",
	user="root",
	password="l34gu31290",
	database="gitDev"
)

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
		global totalCount
		global keyCount
		global idle
		# variables
		idle=0
		#resets after database save
		keyCount=self.clicks
		#doesnt reset unless sublime restarts
		totalCount=self.clicks
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
	#MYSQL QUERY
	mycursor=gitDevDB.cursor()
	sql="INSERT INTO \
	sublimeTattler(keyCount,totalCount,idleCount)\
	VALUES(%s,%s,%s)"
	val=(keyCountNow,totalCount,idleNow)
	mycursor.execute(sql,val)
	gitDevDB.commit()
	print(mycursor.rowcount, "record inserted.")
	
	#reset value
	keyCount=0
	print("check for update in MySQLConnection")
	print(keyCountNow,totalCount,idleNow)

	# cancel the action if
	# idleCount exceeds threshhold
	
	
######################################
## HOW OFTEN?						##
## 1m  60 	##	2m 120	## 	4m 240 	##
## 10m 600  ## 15m 900	## 30m 1800	##

thisInterval=setInterval.setInterval(15,action);



"""
#example of fetch & loop
#fetch
myresult = mycursor.fetchall()
#loop
for x in myresult:
  print(x)
"""