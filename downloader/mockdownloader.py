#!/usr/bin/env python

from downloader import Downloader

import os
import hashlib
import requests

class MockDownloader(Downloader):
	def __init__(self):
		Downloader.__init__(self)

	def download(self, tag, version):
		directory = "https://ftp.mozilla.org/pub/" + tag + "/releases/" + version + "/"
		
		filelisting = directory + "SHA256SUMS"
		print "Downloading", tag, version, "from", filelisting
		r = requests.get(filelisting)
		files = r.text.split("\n")
		print "  Found", len(files), "files"
		
		filedestination = self._get_download_location(tag, version, "SHA256SUMS")
		with open(filedestination, "wb") as outfile:
			outfile.write(r.text)

	def hash(self, tag, version):
		hashesfile = self._get_download_location(tag, version, "SHA256SUMS")
		
		hashes = []
		f = open(hashesfile, "r")
		for l in f.readlines():
			hashes.append(l.split(" ")[0])
		return hashes

	# Do not delete anything in the mock downloader
	def empty_storage(self, tag, version):
		pass