# regex
import re, mysql.connector
import localMySQL
from datetime import datetime
#Anchor Validation / Storage
class AnchorValidate:

	def __init__(self,currentFile):
		self.currentFile=currentFile

	def stampCheck(self):
		#set currentFile
		currentFile=self.currentFile
		if currentFile==None:
			print(currentFile)
			return "error-line15-anchorValidate.py"

		#read currentFile
		with open(currentFile,'r') as thisFile:
		
			#read file
			content=thisFile.read()
			if content==None:
				return "error-line25-anchorValidate.py"

			#if anchor brackets
			if "#<!" in content and "!>#" in content.split():
				# print("TAG FOUND!")
				# get value between
				tagScan=re.search('#<!(.*)!>#',content)
				# set fileID
				fileID=tagScan.group(1)
				# error if none
				if fileID==None:
					return "error-line35-anchorValidate.php"

				print(fileID)
				return fileID

			else:

				#debug
				#print(dir(localMySQL.localConnection\
				#.LocalConnection().theLogin))

				db='gitDev'
				dataCon=localMySQL.localConnection.LocalConnection(db=db).theLogin()
				newCon=dataCon[0]
				newCursor=dataCon[1]

				#statement
				sql="INSERT INTO \
				fileAnchorPaths(fullPath,created_at)\
				VALUES(%s,%s)"
				#values
				val=(currentFile,datetime.now())
				#execute
				newCursor.execute(sql, val)
				#commit
				newCon.commit()
				#last inserted ID
				thisNewID=newCursor.lastrowid
				thisNewID_str=str(thisNewID)
				fileTag='#<!'+thisNewID+'!>#'
				#add tag to top of file
				self.line_prepender(currentFile,fileTag)

	def line_prepender(self,currentFile,line):
	    with open(currentFile, 'r+') as f:
	        content = f.read()
	        f.seek(0, 0)
	        f.write(line.rstrip('\r\n') + '\n' + content)
	        self.newAnchorMySQL(currentFile)

	def newAnchorMySQL(self,currentFile):
		print("newAnchorMySQL")
		print(currentFile)

	def getAnchorMySQL(self,currentFile):
		print("getAnchorMySQL")
		print(currentFile)
