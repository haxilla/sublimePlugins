import sublime
import sublime_plugin
from .classes import testClass

def plugin_loaded():
	
	sublime.active_window().run_command("show_panel", {"panel": "console"})
	newTest=testClass.TestClass()
	valz=newTest.testMe()

	print("Im watching you...")
	print(valz)


  
