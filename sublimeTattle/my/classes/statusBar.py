#<! 43 !>#
import sublime

class StatusBar:

	def __init__(self,view,keyCount):
		self.view=view
		self.keyCount=keyCount
		
	def keyCount_statusBar(self):
		#self.view.set_status('WordCount', self.makePlural('Word', ws['count'] ))
		#self.view_id,key,value
		self.view.set_status('keyCount',str(self.keyCount))

'''

'''