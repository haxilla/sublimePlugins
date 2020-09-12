#<! 12345 !>#

# for regex
# on line 28
import re

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
			print("im reading now")
			#read file
			content=thisFile.read()
			print(content)
			#if anchor brackets
			if "#<!" in content and "!>#" in content.split():
				print("FOUND A TAG")
				#get value between
				tagScan=re.search('#<!(.*)!>#',content)
				#return 
				fileID=tagScan.group(1)
				print(fileID)
				return fileID
			else:
				print("COULD NOT FILE TAG")
				self.line_prepender(currentFile,'#<! 12345 !>#')

	def line_prepender(self,filename,line):
	    with open(filename, 'r+') as f:
	        content = f.read()
	        f.seek(0, 0)
	        f.write(line.rstrip('\r\n') + '\n' + content)


