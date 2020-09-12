#<! 12345 #!>

# sublime
import sublime

def plugin_loaded():
	status=MaidenVoyage.setSail()

class MaidenVoyage():

	def setSail():
		
		projectData=sublime.active_window().project_data()
