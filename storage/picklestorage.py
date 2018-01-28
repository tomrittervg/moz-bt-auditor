#!/usr/bin/env python

from storage import Storage

import os
import pickle

PICKLE_DATABASE = os.path.join(os.path.dirname(__file__), "the_pickle_database.db")

class PickleStorage(Storage):
	def __init__(self):
		if not os.path.exists(PICKLE_DATABASE):
			self.db = {}
		else:
			self.db = pickle.load(open(PICKLE_DATABASE, "rb"))

	def filter_entries(self, entries):
		result = []
		for e in entries:
			if e not in self.db:
				result.append(e)
		return result

	def store_entry(self, entry, data):
		self.db[entry] = data

	def save(self):
		pickle.dump(self.db, open(PICKLE_DATABASE, "wb"))

	def obliterate(self):
		self.db = {}
		os.remove(PICKLE_DATABASE)