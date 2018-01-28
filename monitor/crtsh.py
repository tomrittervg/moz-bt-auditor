#!/usr/bin/env python

from monitor import Monitor

import re
import feedparser

class CRTshMonitor(Monitor):
	def __init__(self):
		#super(CRTshMonitor, self).__init__()
		pass
	
	def poll(self):
		self.crtsh = feedparser.parse('https://crt.sh/atom?q=%25fx-trans.net')

		entries = []
		for e in self.crtsh['entries']:
			sans = e['summary_detail']['value'][0 : e['summary_detail']['value'].find('<br')]
			sans = sans.split(" ")
			if len(sans) != 3:
				print "Got an odd number of SANS when I expected 3: " + str(sans)
				continue
			try:
				sans.remove("&nbsp;")
				sans.remove("invalid.stage.fx-trans.net")
			except:
				print "Tried to remove &nbsp; and invalid.stage.fx-trans.net but got an exception..."
				continue
			entries.append(sans[0])
		return entries


if __name__ == "__main__":
	m = CRTshMonitor()
	m.poll()