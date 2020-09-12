# import
import mysql.connector

# localMySQL.LocalMySQL
class LocalConnection :
	# passed into whole class
	def __init__(self,\
		host='localhost',\
		user='root',\
		pswd='l34gu31290',\
		db=None) :
		#globals
		self.host=host
		self.user=user
		self.pswd=pswd
		self.db=db

	# value above available
	# to all methods
	def theLogin(self):
		if self.db==None:
			print("db REQUIRED")
			return
		#else:
		#	print(self.db)
		#	return

		#MYSQL LOGIN
		theCon = mysql.connector.connection.MySQLConnection(
			host=self.host,
			user=self.user,
			password=self.pswd,
			database=self.db
		)
		#set thisCursor
		theCursor = theCon.cursor()
		#rename for reply
		newCon=theCon
		newCursor=theCursor

		return newCon,newCursor

"""
	def whatNow:
		#debug
		#print("No tag.")
		#requires host,user,pswd,db
		getCon=localMySQL.LocalMySQL\
		('localhost','root','l34gu31290','gitDev')

		thisCon		= getCon.newCon();
		newCon		= thisCon['thisCon']
		newCursor	= thisCon['thisCursor']


		#reply
		reply = dict();  
		reply['theCon'] 	= theCon
		reply['theCursor']	= theCursor

		return reply
		

"""