import sublime
import sublime_plugin

def plugin_loaded():
  sublime.active_window().run_command("show_panel", {"panel": "console"})
  print("Im watching you...")