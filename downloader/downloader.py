#!/usr/bin/env python

import os
import shutil
import hashlib

class Downloader:
	def __init__(self):
		if not os.path.exists(self._data_dir()):
			os.mkdir(self._data_dir())

	def _data_dir(self):
		return os.path.join(os.path.dirname(__file__), "data")

	def _get_download_location(self, tag, version, filename):
		destination = os.path.join(self._data_dir(), tag, version, filename)
		if not os.path.exists(os.path.dirname(destination)):
			os.makedirs(os.path.dirname(destination))
		return destination

	def _check_existing_file_hash(self, file, expected_hash):
		sha256 = hashlib.sha256()
		with open(file, "rb") as infile:
			for chunk in iter(lambda: infile.read(4096), b""):
				sha256.update(chunk)
		return sha256.hexdigest() == expected_hash


	def download(self, tag, version):
		pass

	def hash(self, tag, version):
		pass

	def empty_storage(self, tag, version):
		shutil.rmtree(os.path.join(self._data_dir(), tag, version))