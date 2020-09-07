import sublime
import sublime_plugin

"""
import requests
import json
import time, threading
"""
#from sublimeTattle import keyTattler
print ("hello?")

def plugin_loaded():
	sublime.active_window().run_command("show_panel", {"panel": "console"})

#def tattle(keyCount):
	#print(keyCount)