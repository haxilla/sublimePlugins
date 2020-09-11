import sublime,sublime_plugin
# takes a qualifier argument
# to pass off 
class FileName(sublime_plugin.WindowCommand):

	def run(self):
		#set
		#print(dir(self.window.active_view()))
		global currentFile
		currentFile=self.window.active_view().file_name()
		
#gets current file
sublime.active_window().run_command("current_file")