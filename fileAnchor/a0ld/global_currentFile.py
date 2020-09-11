import sublime,sublime_plugin

def plugin_loaded():
	#opens console on load
	#opens console on load
	sublime.active_window().run_command("file_name")
	print(currentFile_v)
# takes a qualifier argument
# to pass off 
class FileName(sublime_plugin.WindowCommand):

	def run(self):
		#set
		#print(dir(self.window.active_view()))
		global currentFile_v
		currentFile_v=self.window.active_view().file_name()
		
