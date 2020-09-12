#<! 12345 #!>

import re

class AnchorValidate:

	def __init__(self,currentFile_g,siteList_g):
		self.currentFile_g=currentFile_g
		self.siteList_g=siteList_g

	def siteSort(self):	
		#set
		siteList_g		= self.siteList_g
		currentFile_g	= self.currentFile_g
		#loop
		for x in siteList_g:
			#count & dispatch if enabled
			if x=='disabledSites':
				disCount+=1
			if x=='enabledSites':
				enCount+=1
				# anchorStampCheck
				self.stampCheck()


	def stampCheck(self):
		#set currentFile
		currentFile_g=self.currentFile_g
		#read currentFile
		with open(currentFile_g,'r') as thisFile:
			#read file
			content=thisFile.read()
			#if anchor brackets
			if "#<!" in content and "!>#" in content.split():
				#get value between
				fileID=re.search('#<!(.*)!>#',content)
				#return 
				return fileID.group(1)
			else:
				self.line_prepender(currentFile_g,'#<! 12345 #!>')

	def line_prepender(self,filename,line):
	    with open(filename, 'r+') as f:
	        content = f.read()
	        f.seek(0, 0)
	        f.write(line.rstrip('\r\n') + '\n' + content)


