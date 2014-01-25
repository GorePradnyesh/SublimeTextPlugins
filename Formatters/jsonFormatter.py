import sublime, sublime_plugin
import json

class JsonformatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			lines = region_text.splitlines()

			newlines= []
			for line in lines:
				jsonLine = json.loads(line)
				if 'exception' in jsonLine.keys():
					content = jsonLine['timestamp']+": "+jsonLine['message'] + ", STACKTRACE:"+ str(jsonLine['exception'])+ "\n"
				else:
					content = jsonLine['timestamp']+" : "+jsonLine['message'] + "\n"
				newlines.append(content)
			replaced_string  = ''.join(newlines)
			self.view.replace(edit, region, replaced_string)