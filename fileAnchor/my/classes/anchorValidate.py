# regex
import re, localMySQL
from datetime import datetime

# The purpose of this class
# serves to check the file for a fileAnchor tag
# creates one & inserts if needed
# or retrieves the ID inside an existing tag
# in either case the action at the end should be the same

class AnchorValidate:

	def __init__(self,currentFile):
		self.currentFile=currentFile

	def stampCheck(self):
		#defaults
		anchorInsert=0
		anchorFound=0
		prependResult="TagFound"
		#set currentFile
		currentFile=self.currentFile
		#print(newCursorrrentFile)
		if currentFile==None:
			#error if none
			return "error-line25-anchorValidateline15-anchorValidate.py"

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
				anchorFound=1
				isString = isinstance(fileID, str)
				if isString is True:
					fileID=str.strip(fileID)
				# error if none
				if fileID==None:
					return "error-line45-anchorValidate.php"

			else:

				# db required
				db='gitDev'
				dataCon=localMySQL.localConnection.LocalConnection(db=db).theLogin()
				newCon=dataCon[0]
				newCursor=dataCon[1]
				# save to database
				# statement
				sql="INSERT INTO \
				fileAnchorPaths(fullPath,created_at)\
				VALUES(%s,%s)\
				ON DUPLICATE KEY \
				UPDATE saveCount = saveCount + 1;"
				#values
				val=(currentFile,datetime.now())
				#execute
				newCursor.execute(sql, val)
				#commit
				newCon.commit()

				#last inserted ID
				fileID=newCursor.lastrowid
				anchorInsert=1
				fileTag='#<! {fileID} !>#'.format(fileID=fileID)
				if(fileID==None):
					return "error-line72-anchorValidate"

				#add tag to top of file
				prependResult=self.line_prepender\
				(currentFile,fileTag)

		# returns if file prepend was used, fileID,and if
		# the file had the tag or was recently inserted
		isString = isinstance(fileID, str)
		if isString is True:
			fileID=str.strip(fileID)
		return fileID,anchorInsert,anchorFound,prependResult			

	def line_prepender(self,currentFile,line):
	    with open(currentFile, 'r+') as f:
	        content = f.read()
	        f.seek(0, 0)
	        f.write(line.rstrip('\r\n') + '\n' + content)

	    return "Success! Tag Prepended to "+currentFile


	def newAnchorMySQL(self,currentFile):
		print("newAnchorMySQL")
		print(currentFile)

	def getAnchorMySQL(self,currentFile):
		print("getAnchorMySQL")
		print(currentFile)
