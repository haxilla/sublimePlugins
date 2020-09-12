# import
import mysql.connector

# localMySQL.LocalMySQL
class LocalMySQL :
	# passed into whole class
	def __init__(self,host,user,pswd,db) :
		self.host=host
		self.user=user
		self.pswd=pswd
		self.db=db

	# value above available
	# to all methods
	def newCon(self):
		#MYSQL LOGIN
		thisCon = mysql.connector.connection.MySQLConnection(
			host=self.host,
			user=self.user,
			password=self.pswd,
			database=self.db
		)
		#set thisCursor
		thisCursor = thisCon.cursor()
		#reply
		reply = dict();  
		reply['thisCon'] 	= thisCon
		reply['thisCursor']	= thisCursor
		return reply