#!/usr/bin/env python

from downloader import Downloader

import os
import hashlib
import requests

class RequestsDownloader(Downloader):
	def __init__(self):
		Downloader.__init__(self)

	def download(self, tag, version):
		directory = "https://ftp.mozilla.org/pub/" + tag + "/releases/" + version + "/"
		
		filelisting = directory + "SHA256SUMS"
		print "Downloading", tag, version, "from", filelisting
		r = requests.get(filelisting)
		files = r.text.split("\n")
		print "  Found", len(files), "files"
		
		for f in files:
			filehash = f[0 : 64]
			filename = f[66:]
			if not filename:
				continue
			
			print "  Examining", filename
			filedestination = self._get_download_location(tag, version, filename)

			if os.path.exists(filedestination):
				print "  File exists, checking hash..."
				if self._check_existing_file_hash(filedestination, filehash):
					print "  Hash matches, we have the file already."
					continue
				else:
					print "  Hash does not match, need to remove, then re-download the file"
					os.remove(filedestination)

			print "  Downloading to", filedestination
			r = requests.get(directory + filename, stream=True)
			with open(filedestination, "wb") as outfile:
				for chunk in r.iter_content(chunk_size=1024): 
					if chunk: # filter out keep-alive new chunks
						outfile.write(chunk)

	def hash(self, tag, version):
		raise Exception ("I'm not done!")