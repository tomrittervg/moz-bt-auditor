#!/usr/bin/env python

from monitor import get_monitor
from storage import get_storage
from auditor import get_auditor
from downloader import get_downloader

if __name__ == "__main__":
	monitor = get_monitor()
	storage = get_storage()
	auditor = get_auditor()
	downloader = get_downloader()

	entries = monitor.poll()
	to_process = storage.filter_entries(entries)
	for entry in to_process:
		print "To process: ", entry

		components = entry.split(".")
		version = components[2].replace("-", ".")
		tag = components[3]

		downloader.download(tag, version)
		hashes = downloader.hash(tag, version)
		result = auditor.audit(entry, hashes)
		storage.store_entry(entry, result)
		downloader.empty_storage(tag, version)
		print "\n\n"
	storage.save()