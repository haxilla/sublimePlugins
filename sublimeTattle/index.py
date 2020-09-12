#<! 12345 !>#

#waits for loaded response
def plugin_loaded():
	#opens console on load
	sublime.active_window().run_command("show_panel", {"panel": "console"})
	print("console opened by sublimeTattle")
# sublime
import sublime, sublime_plugin
# mysql
import mysql.connector
# datetime
from datetime import datetime
# my
from .my.classes import setInterval, localMySQL
# variables
totalCount=0
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
def action(startUp="0",theInterval=900):

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

	#should probably store mySQL values
	#in mySQL table and request via a method

	#requires host,user,pswd,db
	getCon=localMySQL.localMySQL\
	('localhost','root','l34gu31290','gitDev')
	
	thisCon		= getCon.newCon();
	newCon		= thisCon['thisCon']
	newCursor	= thisCon['thisCursor']

	#statement
	sql="INSERT INTO \
	sublimeTattler(keyCount,totalCount,\
	idleCount,startUp,theInterval,created_at)\
	VALUES(%s,%s,%s,%s,%s,%s)"
	#values
	val=(keyCountNow,totalCount,idleNow,\
	startUp,theInterval,datetime.now())
	#execute
	newCursor.execute(sql, val)
	#commit
	newCon.commit()
	#must convert number to string
	#to display alongside text
	#rowCount=newCursor.rowcount
	#textRowCount=str(theCursor.rowcount)
	#message
	#message="record inserted"
	#reply
	#reply=textRowCount+message
	# console debug
	# text & variable example
	print("rowcount",newCursor.rowcount)
	#return
	#return reply		
	# cancel the action if
	# idleCount exceeds threshhold


# run once on startup
# 1 indicates startUp
action(1)

# then set time
######################################
## HOW OFTEN?						##
## 1m  60 	##	2m 120	## 	4m 240 	##
## 10m 600  ## 15m 900	## 30m 1800	##

thisInterval=setInterval.setInterval(900,action);

"""
#example of fetch & loop
#fetch
myresult = mycursor.fetchall()
#loop
for x in myresult:
  print(x)
"""