class AllFunctions():

	def __init__ (self):
		pass

	def currentFile(self):
		currentFile=sublime.active_window().active_view().file_name()
		return currentFile

