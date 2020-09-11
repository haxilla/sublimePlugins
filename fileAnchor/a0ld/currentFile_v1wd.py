import sublime,sublime_plugin,os
# takes a qualifier argument
# to pass off 
class CurrentFile(sublime_plugin.WindowCommand):

	def run(self):
		#set
		#print(dir(self.window.active_view()))
		thisFile=self.window.active_view().file_name()
		print(thisFile)
		#print(self.window.active_view().file_name())
		#print(self.view.file_name())

sublime.active_window().run_command("current_file")