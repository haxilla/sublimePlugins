class SublimeOutput():

	def __init__(self,fileID=None):
		self.fileID=fileID

	def showPanel(self):
		fileID=self.fileID
		return str(fileID)+" READY FOR MORE"