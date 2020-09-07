# EVENT LISTENER AS SHOWN IN FUNCTION ();
# other plugin used sublime_plugin.textCommand
class KeyTattle(sublime_plugin.EventListener):

	clicks=0
	def on_modified(self,view):
		global keyCount
		global idle
		#increment
		self.clicks+=1
		idle=0
		keyCount=self.clicks
		print("mm hmm...")