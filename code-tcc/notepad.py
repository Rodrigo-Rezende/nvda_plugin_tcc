# Add-on development first example

import globalPluginHandler
import tones # We want to hear beeps.

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_doBeep(self, gesture):
		tones.beep(440, 1000)  # Beep a standard middle A for 1 second.

	__gestures={
		"kb:NVDA+A": "doBeep"
	}