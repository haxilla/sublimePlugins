import sublime

class AllFolders(sublime.Window):

	def projectFolders(self):
		#print("hello?")
		#return dir(self.window.project_data())
		#project_data=self.window.project_data()
		return self.active_view